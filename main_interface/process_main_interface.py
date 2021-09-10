# -*- coding:utf-8 -*-
'''
file    : process_main_interface
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-30 15:29
IDE     : PyCharm
'''
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets

# Import self definition package and UI
from main_interface.main_interface_win import Ui_MainInterFace
from socket_imt_tx.process_socket_img import SocketImgTx
from cmd.process_cmd import CMD
from gimbal.process_gimbal import Gimbal
from self_serial.process_self_serial import SelfSerial
from socket_imt_tx.socket_camera_driver import SocketCameraDriver


class MainInterface(QtWidgets.QWidget, Ui_MainInterFace):
    def __init__(self):
        super(MainInterface, self).__init__()
        self.setupUi(self)
        self.init_all_window()

    def init_all_window(self):
        self.SOCKET_IMG_TX = SocketImgTx(SocketCameraDriver)
        self.CMD = CMD()
        self.GIMBAL = Gimbal()
        self.SELF_SERIAL = SelfSerial()
        pass

    @pyqtSlot()
    def on_bt_gimbal_clicked(self):
        self.GIMBAL.show()
        pass

    @pyqtSlot()
    def on_bt_serial_clicked(self):
        self.SELF_SERIAL.show()
        pass

    @pyqtSlot()
    def on_bt_cmd_clicked(self):
        self.CMD.show()
        pass

    @pyqtSlot()
    def on_bt_img_tx_clicked(self):
        self.SOCKET_IMG_TX.show()
        pass


if __name__ == '__main__':
    mainApp = QtWidgets.QApplication(sys.argv)
    MAIN_WINDOW = MainInterface()
    MAIN_WINDOW.show()
    sys.exit(mainApp.exec_())
