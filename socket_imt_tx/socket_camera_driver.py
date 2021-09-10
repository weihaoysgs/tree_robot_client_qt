# -*- coding:utf-8 -*-
'''
file    : socket_camera_driver
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-31 14:03
IDE     : PyCharm
'''
import cv2
import socket
import threading
from PyQt5 import QtGui


class SocketCameraDriver(object):
    __camera_id__ = 0
    __img_width__ = 640
    __img_height__ = 480
    __img_fps__ = 24
    __port__ = 1234
    __ip_address_bind__ = None
    __socket__ = socket.socket()
    __socket_connect_flag__ = False
    __camera_open_flag__ = False

    def __init__(self):
        self.__init_thread_signal__()

    def __get_ip_address__(self):
        pass

    def __init_thread_signal__(self):
        # 创建一个图传界面显示事件设置为未触发
        self.img_tx_thread_stopEvent = threading.Event()
        self.img_tx_thread_stopEvent.clear()

    def __connect_socket_img_tx_server__(self,ip_address):
        # self.__ip_address_bind__ = ip_address
        # print(self.__socket_connect_flag__)
        # if self.__socket_connect_flag__ == False:
        #     while True:
        #         try:
        #             self.__socket__.connect((ip_address,self.__port__))
        #             self.__socket_connect_flag__ = True
        #             break # thread complete
        #         except:
        #             print("socket connect error!")
        pass

    def receive_all_socket_data(self,soc,count):
        '''
        这种接受方法很有效，不指定每次接受多少，每次按照最大能力接收即可
        :param soc: socket
        :param count: 接收数据的个数
        :return:
        '''
        buf = bytes()
        while count:
            soc.settimeout(5)
            new_buf = soc.recv(count)
            if not new_buf:
                return None
            else:
                buf += new_buf
                count -= len(new_buf)
        return buf
    def cv_2_qt_img(self, cv_img):
        '''
        将 opencv 格式的图像转换为 qt 可以显示的图像
        :param cv_img:
        :return:
        '''
        cv_img = cv2.resize(cv_img, (self.__img_width__, self.__img_height__), interpolation=cv2.INTER_CUBIC)
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        qt_img = QtGui.QImage(cv_img[:], cv_img.shape[1], cv_img.shape[0], cv_img.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)
        qt_img = QtGui.QPixmap(qt_img)
        return qt_img

SocketCameraDriver = SocketCameraDriver()