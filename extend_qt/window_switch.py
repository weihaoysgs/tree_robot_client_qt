# -*- coding:utf-8 -*-
'''
file    : window_switch
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-29 17:12
IDE     : PyCharm
'''
# @author   :xxxxxx
# @FileName :main.py
# @Date     :2019/12/30
# @Time     :21:34
# @Program  :PYCHARM

# -*- coding: utf-8 -*-
'''
多窗口反复切换，只用PyQt5实现
'''
import sys  # 导入系统
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class FirstUi(QMainWindow):  # 第一个窗口类
    def __init__(self):
        super(FirstUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)  # 设置窗口大小
        self.setWindowTitle('First Ui')  # 设置窗口标题
        self.btn = QPushButton('jump', self)  # 设置按钮和按钮名称
        self.btn.setGeometry(50, 100, 100, 50)  # 前面是按钮左上角坐标，后面是窗口大小
        self.btn.clicked.connect(self.slot_btn_function)  # 将信号连接到槽

    def slot_btn_function(self):
        self.hide()  # 隐藏此窗口
        self.s = SecondUi()  # 将第二个窗口换个名字
        self.s.show()  # 经第二个窗口显示出来


class SecondUi(QWidget):  # 建立第二个窗口的类
    def __init__(self):
        super(SecondUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)  # 设置第二个窗口代码
        self.setWindowTitle('Second Ui')  # 设置第二个窗口标题
        self.btn = QPushButton('jump', self)  # 设置按钮和按钮名称
        self.btn.setGeometry(150, 150, 100, 50)  # 前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)  # 将信号连接到槽

    def slot_btn_function(self):
        self.hide()  # 隐藏此窗口
        self.f = FirstUi()  # 将第一个窗口换个名字
        self.f.show()  # 将第一个窗口显示出来


def main():
    app = QApplication(sys.argv)
    w = FirstUi()  # 将第一和窗口换个名字
    w.show()  # 将第一和窗口换个名字显示出来
    sys.exit(app.exec_())  # app.exet_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）


if __name__ == '__main__':  # 只有在本py文件中才能用，被调用就不执行
    main()