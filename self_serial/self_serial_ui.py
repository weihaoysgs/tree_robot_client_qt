# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self_serial_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelfSerial(object):
    def setupUi(self, SelfSerial):
        SelfSerial.setObjectName("SelfSerial")
        SelfSerial.resize(941, 529)
        SelfSerial.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SelfSerial)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget = QtWidgets.QWidget(SelfSerial)
        self.widget.setStyleSheet("background-color:#eef0f6")
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_ico = QtWidgets.QLabel(self.widget)
        self.label_ico.setText("")
        self.label_ico.setObjectName("label_ico")
        self.horizontalLayout_9.addWidget(self.label_ico)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        spacerItem = QtWidgets.QSpacerItem(798, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.bt_minmise = QtWidgets.QPushButton(self.widget)
        self.bt_minmise.setStyleSheet("\n"
"QPushButton{font-family:\"Webdings\";\n"
"                   text-align:top;\n"
"                   background:#6DDF6D;border-radius:6px;\n"
"                   border:none;\n"
"                   font-size:16px;\n"
"}\n"
" QPushButton:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.bt_minmise.setObjectName("bt_minmise")
        self.horizontalLayout_9.addWidget(self.bt_minmise)
        self.bt_maxsize = QtWidgets.QPushButton(self.widget)
        self.bt_maxsize.setStyleSheet("\n"
"QPushButton{font-family:\"Webdings\";\n"
"                   text-align:top;\n"
"                   background:#f0c2eb;border-radius:6px;\n"
"                   border:none;\n"
"                   font-size:16px;\n"
"}\n"
" QPushButton:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.bt_maxsize.setObjectName("bt_maxsize")
        self.horizontalLayout_9.addWidget(self.bt_maxsize)
        self.bt_close_widget = QtWidgets.QPushButton(self.widget)
        self.bt_close_widget.setStyleSheet("\n"
"QPushButton{font-family:\"Webdings\";\n"
"                   background:#F7D674;border-radius:6px;\n"
"                   border:none;\n"
"                   font-size:16px;\n"
"\n"
"}\n"
" QPushButton:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.bt_close_widget.setObjectName("bt_close_widget")
        self.horizontalLayout_9.addWidget(self.bt_close_widget)
        self.horizontalLayout_8.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.widget_2 = QtWidgets.QWidget(SelfSerial)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label_logo_img = QtWidgets.QLabel(self.widget_2)
        self.label_logo_img.setGeometry(QtCore.QRect(720, 40, 197, 235))
        self.label_logo_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo_img.setObjectName("label_logo_img")
        self.dw = QtWidgets.QLabel(self.widget_2)
        self.dw.setGeometry(QtCore.QRect(440, 380, 54, 20))
        self.dw.setObjectName("dw")
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(230, 270, 401, 101))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.formGroupBox = QtWidgets.QGroupBox(self.widget_2)
        self.formGroupBox.setGeometry(QtCore.QRect(40, 10, 181, 321))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setStyleSheet("QPushButton{\n"
"    border:1px solid black;\n"
"    height:20px;\n"
"    border-radius:6px;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:14px;\n"
"    color:black;\n"
"    background-color:#e1e1e1\n"
"    }\n"
"\n"
" QPushButton:hover{\n"
"     background-color:#eef0f6;\n"
" }\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:#ffffff;\n"
"     }\n"
"")
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setStyleSheet("QPushButton{\n"
"    border:1px solid black;\n"
"    height:20px;\n"
"    border-radius:6px;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:14px;\n"
"    color:black;\n"
"    background-color:#e1e1e1\n"
"    }\n"
"\n"
" QPushButton:hover{\n"
"     background-color:#eef0f6;\n"
" }\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:#ffffff;\n"
"     }\n"
"")
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s2__clear_button = QtWidgets.QPushButton(self.widget_2)
        self.s2__clear_button.setGeometry(QtCore.QRect(640, 70, 61, 31))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.widget_2)
        self.verticalGroupBox.setGeometry(QtCore.QRect(230, 10, 401, 241))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout_3.addWidget(self.s2__receive_text)
        self.s3__send_button = QtWidgets.QPushButton(self.widget_2)
        self.s3__send_button.setGeometry(QtCore.QRect(640, 300, 61, 31))
        self.s3__send_button.setStyleSheet("")
        self.s3__send_button.setObjectName("s3__send_button")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 380, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.s3__clear_button = QtWidgets.QPushButton(self.widget_2)
        self.s3__clear_button.setGeometry(QtCore.QRect(640, 340, 61, 31))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.hex_send = QtWidgets.QCheckBox(self.widget_2)
        self.hex_send.setGeometry(QtCore.QRect(640, 270, 81, 16))
        self.hex_send.setObjectName("hex_send")
        self.timer_send_cb = QtWidgets.QCheckBox(self.widget_2)
        self.timer_send_cb.setGeometry(QtCore.QRect(250, 380, 101, 20))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.formGroupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.formGroupBox_2.setGeometry(QtCore.QRect(40, 330, 181, 101))
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.hex_receive = QtWidgets.QCheckBox(self.widget_2)
        self.hex_receive.setGeometry(QtCore.QRect(640, 30, 81, 16))
        self.hex_receive.setObjectName("hex_receive")
        self.bt_back = QtWidgets.QPushButton(self.widget_2)
        self.bt_back.setGeometry(QtCore.QRect(790, 270, 93, 28))
        self.bt_back.setObjectName("bt_back")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(SelfSerial)
        QtCore.QMetaObject.connectSlotsByName(SelfSerial)

    def retranslateUi(self, SelfSerial):
        _translate = QtCore.QCoreApplication.translate
        SelfSerial.setWindowTitle(_translate("SelfSerial", "Form"))
        self.label_8.setText(_translate("SelfSerial", "Logistic Car"))
        self.bt_minmise.setText(_translate("SelfSerial", "0"))
        self.bt_maxsize.setText(_translate("SelfSerial", "1"))
        self.bt_close_widget.setText(_translate("SelfSerial", "r"))
        self.label_logo_img.setText(_translate("SelfSerial", "label_logo_img"))
        self.dw.setText(_translate("SelfSerial", "ms/次"))
        self.verticalGroupBox_2.setTitle(_translate("SelfSerial", "发送区"))
        self.s3__send_text.setHtml(_translate("SelfSerial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123456</p></body></html>"))
        self.formGroupBox.setTitle(_translate("SelfSerial", "串口设置"))
        self.s1__lb_1.setText(_translate("SelfSerial", "串口检测："))
        self.s1__box_1.setText(_translate("SelfSerial", "检测串口"))
        self.s1__lb_2.setText(_translate("SelfSerial", "串口选择："))
        self.s1__lb_3.setText(_translate("SelfSerial", "波特率："))
        self.s1__box_3.setItemText(0, _translate("SelfSerial", "115200"))
        self.s1__box_3.setItemText(1, _translate("SelfSerial", "2400"))
        self.s1__box_3.setItemText(2, _translate("SelfSerial", "4800"))
        self.s1__box_3.setItemText(3, _translate("SelfSerial", "9600"))
        self.s1__box_3.setItemText(4, _translate("SelfSerial", "14400"))
        self.s1__box_3.setItemText(5, _translate("SelfSerial", "19200"))
        self.s1__box_3.setItemText(6, _translate("SelfSerial", "38400"))
        self.s1__box_3.setItemText(7, _translate("SelfSerial", "57600"))
        self.s1__box_3.setItemText(8, _translate("SelfSerial", "76800"))
        self.s1__box_3.setItemText(9, _translate("SelfSerial", "12800"))
        self.s1__box_3.setItemText(10, _translate("SelfSerial", "230400"))
        self.s1__box_3.setItemText(11, _translate("SelfSerial", "460800"))
        self.s1__lb_4.setText(_translate("SelfSerial", "数据位："))
        self.s1__box_4.setItemText(0, _translate("SelfSerial", "8"))
        self.s1__box_4.setItemText(1, _translate("SelfSerial", "7"))
        self.s1__box_4.setItemText(2, _translate("SelfSerial", "6"))
        self.s1__box_4.setItemText(3, _translate("SelfSerial", "5"))
        self.s1__lb_5.setText(_translate("SelfSerial", "校验位："))
        self.s1__box_5.setItemText(0, _translate("SelfSerial", "N"))
        self.s1__lb_6.setText(_translate("SelfSerial", "停止位："))
        self.s1__box_6.setItemText(0, _translate("SelfSerial", "1"))
        self.open_button.setText(_translate("SelfSerial", "打开串口"))
        self.close_button.setText(_translate("SelfSerial", "关闭串口"))
        self.s2__clear_button.setText(_translate("SelfSerial", "清除"))
        self.verticalGroupBox.setTitle(_translate("SelfSerial", "接受区"))
        self.s3__send_button.setText(_translate("SelfSerial", "发送"))
        self.lineEdit_3.setText(_translate("SelfSerial", "1000"))
        self.s3__clear_button.setText(_translate("SelfSerial", "清除"))
        self.hex_send.setText(_translate("SelfSerial", "Hex发送"))
        self.timer_send_cb.setText(_translate("SelfSerial", "定时发送"))
        self.formGroupBox_2.setTitle(_translate("SelfSerial", "串口状态"))
        self.label.setText(_translate("SelfSerial", "已接收："))
        self.label_2.setText(_translate("SelfSerial", "已发送："))
        self.hex_receive.setText(_translate("SelfSerial", "Hex接收"))
        self.bt_back.setText(_translate("SelfSerial", "Back"))