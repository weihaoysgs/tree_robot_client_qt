# -*- coding:utf-8 -*-
'''
file    : process_gimbal
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-30 15:55
IDE     : PyCharm
'''
# Import package
import sys
import struct
import time
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
# import self definition package and UI
from gimbal.gimbal_ui import Ui_Gimbal
from gimbal.parameters import ServoParam


class Gimbal(QtWidgets.QWidget, Ui_Gimbal):
    '''
    初步设想还是下位机使用 DMA 接受指定长度的数据，然后进行解析处理即可
    或者说可以通过 shell 脚本，注册命令进行，但是要进行命令的解析，执行速度较慢
    '''

    def __init__(self):
        super(Gimbal, self).__init__()
        self.setupUi(self)
        self._init_common_serial_()
        self.set_slider_init_value()

    def set_slider_init_value(self):
        self.slider_yaw.setValue(ServoParam.YawInit_Value)
        self.lineEdit_yaw_value.setText(str(ServoParam.YawInit_Value))
        self.slider_pitch_middle.setValue(ServoParam.PitchMidInit_Value)
        self.lineEdit_pitch_mid_value.setText(str(ServoParam.PitchMidInit_Value))
        self.slider_pitch_up.setValue(ServoParam.PitchUpInit_Value)
        self.lineEdit_pitch_up_value.setText(str(ServoParam.PitchUpInit_Value))
        self.slider_pitch_bottom.setValue(ServoParam.PitchBottomInit_Value)
        self.lineEdit_pitch_bottom_value.setText(str(ServoParam.PitchBottomInit_Value))

    def servo_serial_write(self, servo_id, compare_value):
        if self.serial.isOpen():
            self.serial.write(struct.pack('>BHBB', servo_id, compare_value, 0x0D, 0x0A))
        else:
            pass

    def on_bt_generate_pulse_clicked(self):
        self.lineEdit_pulse.setText(str(
            "{" +
            str(self.slider_yaw.value()) + ", " +
            str(self.slider_pitch_bottom.value()) + ", " +
            str(self.slider_pitch_middle.value()) + ", " +
            str(self.slider_pitch_up.value()) + ", " +
            self.lineEdit_open_grab_pulse.text()
            + "}"
        ))
    def on_bt_all_init_clicked(self):
        self.servo_serial_write(ServoParam.YawServo_ID, ServoParam.YawInit_Value)
        time.sleep(0.001)
        self.servo_serial_write(ServoParam.PitchBottomServo_ID, ServoParam.PitchBottomInit_Value)
        time.sleep(0.001)
        self.servo_serial_write(ServoParam.PitchMidServo_ID, ServoParam.PitchMidInit_Value)
        time.sleep(0.001)
        self.servo_serial_write(ServoParam.PitchUpServo_ID, ServoParam.PitchUpInit_Value)
        time.sleep(0.001)
        self.servo_serial_write(ServoParam.GrabServo_ID, ServoParam.Grab_OpenCompareValue)
        time.sleep(0.001)
        print("de init")
        pass

    @pyqtSlot(int)
    def on_slider_yaw_valueChanged(self, value):
        self.lineEdit_yaw_value.setText(str(value))
        self.servo_serial_write(ServoParam.YawServo_ID, value)

    @pyqtSlot(int)
    def on_slider_pitch_bottom_valueChanged(self, value):
        self.lineEdit_pitch_bottom_value.setText(str(value))
        self.servo_serial_write(ServoParam.PitchBottomServo_ID, value)

    @pyqtSlot(int)
    def on_slider_pitch_middle_valueChanged(self, value):
        self.lineEdit_pitch_mid_value.setText(str(value))
        self.servo_serial_write(ServoParam.PitchMidServo_ID, value)

    @pyqtSlot(int)
    def on_slider_pitch_up_valueChanged(self, value):
        self.lineEdit_pitch_up_value.setText(str(value))
        self.servo_serial_write(ServoParam.PitchUpServo_ID, value)

    @pyqtSlot()
    def on_bt_open_clicked(self):
        self.servo_serial_write(ServoParam.GrabServo_ID, ServoParam.Grab_OpenCompareValue)
        self.lineEdit_open_grab_pulse.setText(str( ServoParam.Grab_OpenCompareValue))
    @pyqtSlot()
    def on_bt_grab_clicked(self):
        self.servo_serial_write(ServoParam.GrabServo_ID, ServoParam.Grab_GrabCompareValue)
        self.lineEdit_open_grab_pulse.setText(str(ServoParam.Grab_GrabCompareValue))
    def _init_common_serial_(self):
        self.timer_receive = QTimer()
        self.timer_transmit = QTimer()
        self.serial = serial.Serial()

        # 定时接受
        self.timer_receive.timeout.connect(lambda: self.receive_data(self.textBrowser_receive_region))
        self.bt_send_to_com.clicked.connect(lambda: self.send_data(str(self.textEdit_send_region.toPlainText())))

        self.bt_com_detect.clicked.connect(self.port_detect)
        self.comBox_com_select.currentTextChanged.connect(self.com_information)
        self.bt_open_com.clicked.connect(self.com_open)  # 注意，在槽函数中关联时不要带括号，否则会一直执行
        self.bt_close_com.clicked.connect(self.com_close)

    def port_detect(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.com_dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.comBox_com_select.clear()
        for port in port_list:
            self.com_dict["%s" % port[0]] = "%s" % port[1]
            self.comBox_com_select.addItem(port[0])
        if len(self.com_dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def com_information(self):
        # 显示选定的串口的详细信息
        information = self.comBox_com_select.currentText()
        if information != "":
            self.state_label.setText(self.com_dict[self.comBox_com_select.currentText()])

    def com_open(self):
        self.serial.port = self.comBox_com_select.currentText()
        self.serial.baudrate = int(self.comBox_boud_rate.currentText())
        self.serial.bytesize = int(self.comBox_data_bit.currentText())
        self.serial.stopbits = int(self.com_box_stop_bit.currentText())
        self.serial.parity = self.comBox_crc_check.currentText()
        try:
            self.serial.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None
        # 打开串口接收定时器，周期为2ms
        self.timer_receive.start(2)
        if self.serial.isOpen():
            self.bt_open_com.setEnabled(False)
            self.bt_close_com.setEnabled(True)
            self.formGroupBox_Serial.setTitle("串口状态（已开启）")
        self.data_num_sended = 0
        self.data_num_received = 0
        self.lineEdit_have_received.setText(str(0))
        self.lineEdit_have_tx.setText(str(0))

    # 关闭串口
    def com_close(self):
        self.timer_receive.stop()
        self.timer_transmit.stop()
        try:
            self.serial.close()
        except:
            pass
        self.bt_open_com.setEnabled(True)
        self.bt_close_com.setEnabled(False)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit_have_received.setText(str(0))
        self.data_num_sended = 0
        self.lineEdit_have_tx.setText(str(0))
        self.formGroupBox_Serial.setTitle("串口状态（已关闭）")

    # 发送数据
    def send_data(self, data):
        if self.serial.isOpen():
            input_s = data
            if input_s != "":
                # 非空字符串
                if self.checkBox_hex_send.isChecked():
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
                    print(input_s)

                num = self.serial.write(input_s)
                self.data_num_sended += num
                self.lineEdit_have_tx.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据
    def receive_data(self, textBrowser_receive_region):
        try:
            num = self.serial.inWaiting()
        except:
            self.com_close()
            return None
        if num > 0:
            data = self.serial.read(num)
            num = len(data)
            print(num)
            # hex显示
            if self.checkBox_hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.textBrowser_receive_region.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                textBrowser_receive_region.insertPlainText(data.decode('iso-8859-1'))
                print(data.decode('iso-8859-1'))
            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit_have_received.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = textBrowser_receive_region.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            textBrowser_receive_region.setTextCursor(textCursor)
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Gimbal = Gimbal()
    Gimbal.show()
    sys.exit(app.exec_())
