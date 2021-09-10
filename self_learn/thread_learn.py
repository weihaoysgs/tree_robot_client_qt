from main_interface.main_interface_win import Ui_MainInterFace
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal,pyqtSlot
import sys
import time

class MyWin(QWidget,Ui_MainInterFace):
    """docstring for Mywine"""
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)
        self.mythread = MyThread() # 实例化自己建立的任务线程类
        self.mythread.signal.connect(self.callback) #设置任务线程发射信号触发的函数
    @pyqtSlot()
    def on_bt_cmd_clicked(self): # 这里test就是槽函数, 当点击按钮时执行 test 函数中的内容, 注意有一个参数为 self
        self.mythread.start() # 启动任务线程

    def callback(self,i): # 这里的 i 就是任务线程传回的数据
        self.bt_cmd.setText(i)

class MyThread(QThread): # 建立一个任务线程类
    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self): # 在启动线程后任务从这个函数里面开始执行
        for i in range(10):
            self.signal.emit(str(i)) #任务线程发射信号用于与图形化界面进行交互
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin() # 实例化一个窗口小部件
    mywin.setWindowTitle('Hello world!') # 设置窗口标题
    mywin.show() #显示窗口
    sys.exit(app.exec())

