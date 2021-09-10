# -*- coding:utf-8 -*-
'''
file    : process_cmd
author  : weihaoysgs@gmail.com
des     : $ the logistic process of CMD UI
date    : 2021-08-30 14:30
IDE     : PyCharm
'''
import sys
import serial.tools.list_ports

from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from cmd.cmd_ui import Ui_CMD


class CMD(QtWidgets.QWidget, Ui_CMD):
    def __init__(self):
        super(CMD, self).__init__()
        self.setupUi(self)
        self._init_common_serial_()
        self._self_init_fun()

    @pyqtSlot()
    def on_bt_back_clicked(self):
        self.close()

    def _self_init_fun(self):
        self.bt_version.clicked.connect(lambda: self.send_data('version'))

    def _init_common_serial_(self):
        self.timer_receive = QTimer()
        self.timer_transmit = QTimer()
        self.serial = serial.Serial()

        # 定时接收
        ''' 注意这里指定接受数据的显示位置 '''
        self.timer_receive.timeout.connect(lambda: self.receive_data(self.text_browser_cmd))
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

    # serial port information
    def com_information(self):
        # 显示选定的串口的详细信息
        information = self.comBox_com_select.currentText()
        if information != "":
            self.state_label.setText(self.com_dict[self.comBox_com_select.currentText()])

    # open serial
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

    # close serial
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

    # send data
    def send_data(self, data):
        print("send")
        if self.serial.isOpen():
            input_s = data
            print(input_s)
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

    # receive data
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
    cmd_app = QtWidgets.QApplication(sys.argv)
    CmdAssistant = CMD()
    CmdAssistant.show()
    sys.exit(cmd_app.exec_())
