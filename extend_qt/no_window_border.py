# -*- coding:utf-8 -*-
'''
file    : no_window_border
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-08-29 14:41
IDE     : PyCharm
'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author：mgboy time:2020/8/5
import sys

from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QFont, QEnterEvent, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5 import QtCore

from no_window_border_ui import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self._init_main_window()  # 主窗口初始化设置
        self._initDrag()  # 设置鼠标跟踪判断扳机默认值
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self._close_max_min_icon()  # 设置 3 个按钮的图标字体
        print(self.width(), self.height())
        self.my_Qss()  # 美化
        self.widget.installEventFilter(self)  # 初始化事件过滤器
        self.widget_2.installEventFilter(self)

    def _init_main_window(self):
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)

        ########在测试时记得设置自己的图标地址
        # 设置图标
        w = self.label.width()
        h = self.label.height()
        self.pix = QPixmap(
            "../logo/logo_logistic_car.png")  # 注意修改Windows路径问题
        self.label.setPixmap(self.pix)
        self.label.setScaledContents(True)

        # 设置标题
        self.label_2.setText('我的APP')
        # 设置标题字体，大小
        self.label_2.setStyleSheet('''
                                    font-family:"方正胖娃_GBK";
                                   font-size:11px;
                                   ''')

    def _initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def _close_max_min_icon(self):
        # 设置按钮图标使用webdings特殊字体
        self.pushButton_3.setText('r')
        self.pushButton_2.setText('1')
        self.pushButton.setText('0')

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 最小化
        self.showMinimized()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        # 最大化与复原
        if self.isMaximized():
            self.showNormal()
            self.pushButton_2.setText('1')  # 切换放大按钮图标
            self.pushButton_2.setToolTip("<html><head/><body><p>最大化</p></body></html>")
        else:
            self.showMaximized()
            self.pushButton_2.setText('2')
            self.pushButton_2.setToolTip("<html><head/><body><p>恢复</p></body></html>")

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        # 关闭程序
        self.close()

    def eventFilter(self, obj, event):
        # 事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
        return super(MyWindow, self).eventFilter(obj, event)  # 注意 ,MyWindow是所在类的名称
        # return QWidget.eventFilter(self, obj, event)  # 用这个也行，但要注意修改窗口类型

    def resizeEvent(self, QResizeEvent):
        # 自定义窗口调整大小事件
        # 改变窗口大小的三个坐标范围
        self._right_rect = [QPoint(x, y) for x in range(self.width() - 5, self.width() + 5)
                            for y in range(self.widget.height() + 20, self.height() - 5)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - 5)
                             for y in range(self.height() - 5, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - 5, self.width() + 1)
                             for y in range(self.height() - 5, self.height() + 1)]

    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self.widget.height()):
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:  # QMouseEvent.pos()获取相对位置
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)

        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            #  由于我窗口设置了圆角,这个调整大小相当于没有用了
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def my_Qss(self):
        # Qss美化
        qssStyle = '''

                   QWidget#widget{
                   background-color:#eef0f6;
                   border-left:0.5px solid lightgray;
                   border-right:0.5px solid lightgray;
                   border-top:0.5px solid lightgray;
                   border-bottom:0.5px solid #e5e5e5;
                   border-top-left-radius: 5px;
                   border-top-right-radius: 5px;
                   }

                   QWidget#widget_2{
                   background-color:#ffffff;
                   border-left:0.5px solid lightgray;
                    border-right:0.5px solid lightgray;
                   border-bottom:0.5px solid #e5e5e5;
                   border-bottom-left-radius: 5px;
                   border-bottom-right-radius: 5px;
                   padding:5px 5px 5px 5px
                   }

                   QPushButton#pushButton
                   {
                   font-family:"Webdings";
                   text-align:top;
                   background:#6DDF6D;border-radius:5px;
                   border:none;
                   font-size:13px;
                   }
                   QPushButton#pushButton:hover{background:green;}

                   QPushButton#pushButton_2
                   {
                   font-family:"Webdings";
                   background:#F7D674;border-radius:5px;
                   border:none;
                   font-size:13px;
                   }
                   QPushButton#pushButton_2:hover{background:yellow;}

                   QPushButton#pushButton_3
                   {
                   font-family:"Webdings";
                   background:#F76677;border-radius:5px;
                   border:none;
                   font-size:13px;
                   }
                   QPushButton#pushButton_3:hover{background:red;}
                   '''
        self.setStyleSheet(qssStyle)


if __name__ == "__main__":
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
