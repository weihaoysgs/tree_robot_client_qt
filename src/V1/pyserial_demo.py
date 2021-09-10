import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from ui_demo_1 import Ui_Form
import os
import struct
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.__yaw_compare_value = 1800
        self.__pitch_low_compare_value = 1955
        self.__pitch_middle_compare_value = 1840
        self.__pitch_up_compare_value = 1920
        self.__grab_servo_compare_value = 1865
        self.YAW_SERVO_ID = 1
        self.PITCH_LOW_SERVO_ID = 2
        self.PITCH_MIDDLE_SERVO_ID = 3
        self.PITCH_UP_SERVO_ID = 4
        self.GRAB_SERVO_ID = 5
        self.ADD_ONE_PUSH = 5
        self.setWindowTitle("Logistic Car Debug Assistant")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.init_five_servo_compare_value_line_edit()

    def init_five_servo_compare_value_line_edit(self):
        self.line_edit_yaw_servo_value.setText(str(self.__yaw_compare_value))
        self.line_edit_pitch_low_servo.setText(str(self.__pitch_low_compare_value))
        self.line_edit_pitch_middle.setText(str(self.__pitch_middle_compare_value))
        self.line_edit_pitch_up.setText(str(self.__pitch_up_compare_value))
        self.line_edit_grab.setText(str(self.__grab_servo_compare_value))

    def _de_init_all_servo(self):
        self.init_five_servo_compare_value_line_edit()
        time.sleep(0.2)             # 增加延时是为了下位机在接收到每一帧数据有处理的时间
        self._grab_send()
        time.sleep(0.2)
        self._pitch_up_send()
        time.sleep(0.2)
        self._pitch_middle_send()
        time.sleep(0.2)
        self._pitch_low_send()
        time.sleep(0.2)
        self._yaw_servo_value_send()
        time.sleep(0.2)
        pass
    def _generate_compare_value(self):
        yaw_compare_value = self.line_edit_yaw_servo_value.text()
        pitch_low_compare_value = self.line_edit_pitch_low_servo.text()
        pitch_middle_compare_value = self.line_edit_pitch_middle.text()
        pitch_up_compare_value = self.line_edit_pitch_up.text()
        grab_compare_value = self.line_edit_grab.text()
        generate_result = "{ " + \
                          yaw_compare_value + ", " +\
                          pitch_low_compare_value + ", " + \
                          pitch_middle_compare_value + ", " + \
                          pitch_up_compare_value + ", " + \
                          grab_compare_value + " }"
        self.line_edit_five_servo_compare_value.setText(generate_result)
        pass

    def set_back_ground_img(self):
        back_ground_image = QtGui.QPalette()
        back_ground_image.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./logo/back_img2.png")))
        self.setPalette(back_ground_image)

    def init(self):
        # 设置背景图片
        self.set_back_ground_img()
        # 显示 Logo
        self.label_logo_img.setPixmap(QPixmap("./logo/logo_logistic_car.png"))
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 各个舵机的 compare value 的 + - send 信号
        #################### Yaw Servo #######################################
        self.bt_yaw_servo_compare_value_add.clicked.connect(self._yaw_servo_compare_value_add)  # 处理 + 的信号
        self.bt_yaw_servo_compare_value_desc.clicked.connect(self._yaw_servo_compare_value_desc)  # 处理 - 的信号
        self.bt_yaw_servo_value_send.clicked.connect(self._yaw_servo_value_send)  # 将上位机设置的值发送出去
        #################### Pitch Low Servo #################################
        self.bt_pitch_low_add.clicked.connect(self._pitch_low_add)
        self.bt_pitch_low_desc.clicked.connect(self._pitch_low_desc)
        self.bt_pitch_low_send.clicked.connect(self._pitch_low_send)
        #################### Pitch Middle Servo ##############################
        self.bt_pitch_middle_add.clicked.connect(self._pitch_middle_add)
        self.bt_pitch_middle_desc.clicked.connect(self._pitch_middle_desc)
        self.bt_pitch_middle_send.clicked.connect(self._pitch_middle_send)
        #################### Pitch Low Servo #################################
        self.bt_pitch_up_add.clicked.connect(self._pitch_up_add)
        self.bt_pitch_up_desc.clicked.connect(self._pitch_up_desc)
        self.bt_pitch_up_send.clicked.connect(self._pitch_up_send)
        #################### Grab Servo ######################################
        self.bt_grab_send.clicked.connect(self._grab_send)
        self.bt_grab_add.clicked.connect(self._grab_add)
        self.bt_grab_desc.clicked.connect(self._grab_desc)
        ####################### 将 all de init 和 generate compare value 的点击事件结合
        self.bt_all_deinit.clicked.connect(self._de_init_all_servo)
        self.bt_generate_compare_value.clicked.connect(self._generate_compare_value)

    def _pitch_low_add(self):
        current_pitch_low_value = self.line_edit_pitch_low_servo.text()
        try:
            current_pitch_low_value = int(current_pitch_low_value)
            self.line_edit_pitch_low_servo.setText(str(current_pitch_low_value + self.ADD_ONE_PUSH))
            self._pitch_low_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_low_desc(self):
        current_pitch_low_value = self.line_edit_pitch_low_servo.text()
        try:
            current_pitch_low_value = int(current_pitch_low_value)
            self.line_edit_pitch_low_servo.setText(str(current_pitch_low_value - self.ADD_ONE_PUSH))
            self._pitch_low_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_low_send(self):
        if self.ser.isOpen():
            try:
                pitch_low_compare_value = int(self.line_edit_pitch_low_servo.text())
            except ValueError:
                QMessageBox.critical(self, 'wrong data', 'Please input integer')
                return None
            self.servo_serial_write(self.PITCH_LOW_SERVO_ID, pitch_low_compare_value)
        else:
            QMessageBox.critical(self, 'Wrong operation', 'Serial is not open!')
            return None
        print("current_pitch_low_value {:d}".format(pitch_low_compare_value))
        pass

    def _pitch_middle_add(self):
        current_pitch_middle_value = self.line_edit_pitch_middle.text()
        try:
            current_pitch_middle_value = int(current_pitch_middle_value)
            self.line_edit_pitch_middle.setText(str(current_pitch_middle_value + self.ADD_ONE_PUSH))
            self._pitch_middle_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_middle_desc(self):
        current_pitch_middle_value = self.line_edit_pitch_middle.text()
        try:
            current_pitch_middle_value = int(current_pitch_middle_value)
            self.line_edit_pitch_middle.setText(str(current_pitch_middle_value - self.ADD_ONE_PUSH))
            self._pitch_middle_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_middle_send(self):
        if self.ser.isOpen():
            try:
                pitch_middle_compare_value = int(self.line_edit_pitch_middle.text())
            except ValueError:
                QMessageBox.critical(self, 'wrong data', 'Please input integer')
                return None
            self.servo_serial_write(self.PITCH_MIDDLE_SERVO_ID, pitch_middle_compare_value)
        else:
            QMessageBox.critical(self, 'Wrong operation', 'Serial is not open!')
            return None
        print("pitch_middle_compare_value {:d}".format(pitch_middle_compare_value))
        pass

    def _pitch_up_add(self):
        current_pitch_up_value = self.line_edit_pitch_up.text()
        try:
            current_pitch_up_value = int(current_pitch_up_value)
            self.line_edit_pitch_up.setText(str(current_pitch_up_value + self.ADD_ONE_PUSH))
            self._pitch_up_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_up_desc(self):
        current_pitch_up_value = self.line_edit_pitch_up.text()
        try:
            current_pitch_up_value = int(current_pitch_up_value)
            self.line_edit_pitch_up.setText(str(current_pitch_up_value - self.ADD_ONE_PUSH))
            self._pitch_up_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _pitch_up_send(self):
        if self.ser.isOpen():
            try:
                pitch_up_compare_value = int(self.line_edit_pitch_up.text())
            except ValueError:
                QMessageBox.critical(self, 'wrong data', 'Please input integer')
                return None
            self.servo_serial_write(self.PITCH_UP_SERVO_ID, pitch_up_compare_value)
        else:
            QMessageBox.critical(self, 'Wrong operation', 'Serial is not open!')
            return None
        print("pitch_up_compare_value {:d}".format(pitch_up_compare_value))
        pass

    def _grab_add(self):
        current_grab_value = self.line_edit_grab.text()
        try:
            current_grab_value = int(current_grab_value)
            #self.line_edit_grab.setText(str(current_grab_value + self.ADD_ONE_PUSH))
            self.line_edit_grab.setText(str(1895))
            self._grab_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _grab_desc(self):
        current_grab_value = self.line_edit_grab.text()
        try:
            current_grab_value = int(current_grab_value)
            #self.line_edit_grab.setText(str(current_grab_value - self.ADD_ONE_PUSH))
            self.line_edit_grab.setText(str(1865))
            self._grab_send()
        except ValueError:
            QMessageBox.critical(self, 'Wrong data', 'Please input right data')
            return None
        print(True)
        pass

    def _grab_send(self):
        if self.ser.isOpen():
            try:
                grab_compare_value = int(self.line_edit_grab.text())
            except ValueError:
                QMessageBox.critical(self, 'wrong data', 'Please input integer')
                return None
            self.servo_serial_write(self.GRAB_SERVO_ID, grab_compare_value)
        else:
            QMessageBox.critical(self, 'Wrong operation', 'Serial is not open!')
            return None
        print("grab_compare_value {:d}".format(grab_compare_value))
        pass

    def _yaw_servo_compare_value_add(self):
        current_yaw_servo_compare_value = self.line_edit_yaw_servo_value.text()
        try:
            current_yaw_servo_compare_value = int(current_yaw_servo_compare_value)
            self.line_edit_yaw_servo_value.setText(str(current_yaw_servo_compare_value + 5))
            self._yaw_servo_value_send()
        except ValueError:
            QMessageBox.critical(self, 'wrong data', 'Please input integer data!')
            return None
        pass

    def _yaw_servo_compare_value_desc(self):
        current_yaw_servo_compare_value = self.line_edit_yaw_servo_value.text()
        try:
            current_yaw_servo_compare_value = int(current_yaw_servo_compare_value)
            self.line_edit_yaw_servo_value.setText(str(current_yaw_servo_compare_value - 5))
            self._yaw_servo_value_send()
        except ValueError:
            QMessageBox.critical(self, 'wrong data', 'Please input integer data!')
            return None
        pass

    def _yaw_servo_value_send(self):
        if self.ser.isOpen():
            yaw_compare_value = self.line_edit_yaw_servo_value.text()
            try:
                yaw_compare_value = int(yaw_compare_value)
            except ValueError:
                QMessageBox.critical(self, 'wrong data', 'Please input integer data!')
                return None
            self.servo_serial_write(self.YAW_SERVO_ID, yaw_compare_value)
            # self.ser.write(struct.pack('>BHB', 0x0A, yaw_compare_value, 0x0D))
            # < 低位在前，例如 256 -> 0x00 0x01 serial.write(struct.pack('>BHHB', 0x0A, int(center_x), int(center_y), 0x0D))
            print("yaw_compare_value {:d}".format(yaw_compare_value))
            pass
        else:
            QMessageBox.critical(self, 'Wrong operation', 'serial is not open')
            return None

    def servo_serial_write(self, servo_ID, compare_value):
        self.ser.write(struct.pack('>BBHB', 0x0A, servo_ID, compare_value, 0x0D))
        time.sleep(0.001)

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            input_s = self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    # ascii发送
                    input_s = (input_s + '\r\n').encode('utf-8')

                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0 :
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            if self.hex_receive.checkState():
                out_s = ''
                # 解析 JY901 的数据
                self.parse_JY901_(data)
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    def parse_JY901_(self, data):
        for i in range(0, len(data)):
            if data[i] == 0x55 and (i + 7) < len(data):
                if data[i + 1] == 0x53:
                    row_ = float((data[i + 3] << 8 | data[2]) / 32768 * 180)
                    if row_ > 180:
                        row_ = row_ - 360
                    pitch_ = float((data[i + 5] << 8 | data[4]) / 32768 * 180)
                    if pitch_ > 180:
                        pitch_ = pitch_ - 360
                    yaw_ = float((data[i + 7] << 8 | data[6]) / 32768 * 180)
                    if yaw_ > 180:
                        yaw_ = yaw_ - 360
                    self.row_line_edit.setText("  {:2f}".format(row_))
                    self.pitch_line_edit.setText("  {:2f}".format(pitch_))
                    self.yaw_line_edit.setText("  {:2f}".format(yaw_))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    LogisticCar = Pyqt5_Serial()
    LogisticCar.show()
    sys.exit(app.exec_())
