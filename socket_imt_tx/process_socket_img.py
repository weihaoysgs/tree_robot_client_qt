# -*- coding:utf-8 -*-
'''
file    : process_socket_img
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-30 14:46
IDE     : PyCharm
'''
# Qt package
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys
import threading
import cv2
import numpy as np
# Import self definition package and
from socket_imt_tx.socket_img_ui import Ui_SocketImgTx
from socket_imt_tx.socket_camera_driver import SocketCameraDriver

class SocketImgTx(QtWidgets.QWidget, Ui_SocketImgTx):
    def __init__(self,SocketCameraDriver):
        super(SocketImgTx, self).__init__()
        self.setupUi(self)
        self.socket_camera_driver = SocketCameraDriver
        self._init_all_slot_fun()

    def _init_all_slot_fun(self):
        self.bt_connect.clicked.connect(lambda :self.connect_socket_img_tx_server(str(self.lineEdit_ip_add.text())))
        pass


    def _init_thread_signal_(self):

        pass

    def connect_socket_img_tx_server(self,server_ip):
        print(server_ip)
        # self.socket_camera_driver.__connect_socket_img_tx_server__(server_ip)
        # connect_server_thread = threading.Thread(target=self.socket_camera_driver.__connect_socket_img_tx_server__(),args=(self,server_ip,))
        # connect_server_thread.setDaemon(True)
        # connect_server_thread.start()
        if self.socket_camera_driver.__socket_connect_flag__ == True:
            data_len = self.socket_camera_driver.receive_all_socket_data(self.socket_camera_driver.__socket__,16)
            # print(data_len)
            if len(data_len) == 16:
                string_img_data = self.socket_camera_driver.receive_all_socket_data(self.socket_camera_driver.__socket__,int(data_len))
                image_data = np.frombuffer(string_img_data,dtype='uint8')
                image_data = cv2.imdecode(image_data,1)
                frame = cv2.resize(image_data,(640,480))
                #self.set_img_ui(frame)
                qt_img = self.socket_camera_driver.cv_2_qt_img(frame)
                self.labe_show_img.setPixmap(qt_img)
                print(frame)

        if self.socket_camera_driver.__socket_connect_flag__ == False:
            while True:
                try:
                    self.__socket.connect((self.__ip_address,self.__port))
                except:
                    print("socket connect error!")
                else:
                    self.__socket_connect_flag = True
                    #self.__camera_timer.stop()
                    break


if __name__ == '__main__':
    socket_img_tx_app = QtWidgets.QApplication(sys.argv)
    SocketImgTx_UI = SocketImgTx(SocketCameraDriver)
    SocketImgTx_UI.show()
    sys.exit(socket_img_tx_app.exec_())
