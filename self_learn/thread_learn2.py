# -*- coding:utf-8 -*-
'''
file    : thread
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-30 17:53
IDE     : PyCharm
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QPushButton, QLCDNumber)


class MyThread(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        self.count = 0

    def resetCount(self):
        self.count = 0

    def run(self):
        while True:
            # self.msleep(100)
            # self.count += 1
            # 当该线程开始执行之后，一直在发射该信号
            self.countChanged.emit(None)


class DemoThreadSignalSlot(QWidget):
    def __init__(self, parent=None):
        super(DemoThreadSignalSlot, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: 线程间使用信号与槽')
        # 设置窗口大小
        self.resize(360, 200)

        self.initUi()

    def initUi(self):

        mainLayout = QVBoxLayout()

        # 液晶数字显示
        self.lcd = QLCDNumber()
        mainLayout.addWidget(self.lcd)
        self.btnStart = QPushButton('开始')
        self.btnStart.setMinimumHeight(60)
        self.btnStart.clicked.connect(self.onBtnStart)
        mainLayout.addWidget(self.btnStart)

        self.setLayout(mainLayout)

        self.thread = MyThread(self)
        self.thread.countChanged.connect(self.threadPrint)
        self.start = False

    def threadPrint(self):
        print("thread")
    def onBtnStart(self):
        if not self.thread is None:
            if self.start == False:
                self.start = True
                self.btnStart.setText('结束')
                self.thread.start()
            else:
                self.start = False
                self.btnStart.setText('开始')
                if self.thread.isRunning:
                    self.thread.terminate()
                    self.thread.quit()

                #self.thread.resetCount()
                self.lcd.display(0)

    # 关闭时调用
    def closeEvent(self, event):
        if not self.thread is None:
            if (self.thread.isRunning):
                self.thread.terminate()
                self.thread.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoThreadSignalSlot()
    window.show()
    sys.exit(app.exec())