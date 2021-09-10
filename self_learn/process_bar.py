# -*- coding:utf-8 -*-
'''
file    : process_bar
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-30 17:49
IDE     : PyCharm
'''
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QBasicTimer
import sys
from time import sleep
from myqt import loadwin, mainwin


class LoadWin(QWidget, loadwin.Ui_Form):  # 启动画面类 -----------
    def __init__(self):
        super(LoadWin, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setStyleSheet("#Form{background-color:'#4682B4'}"
                           "#label_info{background-color:'#4682B4';color:white;font-weight:600;}"
                           )  # 设置启动窗背景色和进度信息的字体样式等
        pix = QPixmap("./load_logo.png")  # 加载logo
        self.label_logo.setPixmap(pix)
        self.label_logo.setScaledContents(True)  # 图像拉伸填充
        self.timer = QBasicTimer()  # 定时器对象
        self.main_win = MainWin()  # 进度结束后要显示的主页
        self.step = 0  # 进度值
        self.proess_run()

    def proess_run(self):  # 启动进度线程
        self.cal = LoadThread()  # 线程对象
        self.cal.part_signal.connect(self.process_set_part)
        self.cal.data_signal.connect(self.show_main_win)
        self.cal.start()  # 调用线程run

    def process_set_part(self, num):
        self.step = num  # 进度从num开始
        self.progressBar.setValue(self.step)
        if num == 0:
            self.timer.start(20, self)  # 启动QBasicTimer, 每20毫秒调用一次回调函数
            self.label_info.setText("正在计算数据...")
        if num == 1:
            self.timer.stop()  # 重启，调整进度条增值速度
            self.timer.start(10, self)
            self.label_info.setText("已完成计算，等待主页加载...")

    def timerEvent(self, *args, **kwargs):  # QBasicTimer的事件回调函数
        self.progressBar.setValue(self.step)  # 设置进度条的值
        if self.step < 100:
            self.step += 1

    def show_main_win(self, mes):
        self.main_win.set_data(mes)
        self.main_win.show()
        self.close()


class LoadThread(QThread):  # 自定义计算线程类 -----------
    part_signal = pyqtSignal(int)  # 进度环节信号
    data_signal = pyqtSignal(str)  # 数据传递信号

    def __init__(self):
        super().__init__()

    def run(self):
        self.part_signal.emit(0)
        self.fun_part_one()
        self.part_signal.emit(1)
        sleep(1)  # 模拟加载耗时
        self.data_signal.emit("计算结果：2021")

    def fun_part_one(self):
        sleep(3)  # 模拟计算耗时


class MainWin(QWidget, mainwin.Ui_Form):  # 主页界面类 -----------
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

    def set_data(self, mes):  # 接收进度线程的计算结果
        self.lineEdit.setText(mes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoadWin()
    w.show()
    sys.exit(app.exec())
