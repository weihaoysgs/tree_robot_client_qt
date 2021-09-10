# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gimbal_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gimbal(object):
    def setupUi(self, Gimbal):
        Gimbal.setObjectName("Gimbal")
        Gimbal.resize(804, 781)
        self.bt_back = QtWidgets.QPushButton(Gimbal)
        self.bt_back.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.bt_back.setStyleSheet("font: 9pt \"Lucida Console\";")
        self.bt_back.setObjectName("bt_back")
        self.groupBox = QtWidgets.QGroupBox(Gimbal)
        self.groupBox.setGeometry(QtCore.QRect(540, 0, 251, 681))
        self.groupBox.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_hex_send = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_hex_send.setObjectName("checkBox_hex_send")
        self.horizontalLayout.addWidget(self.checkBox_hex_send)
        self.checkBox_hex_receive = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_hex_receive.setObjectName("checkBox_hex_receive")
        self.horizontalLayout.addWidget(self.checkBox_hex_receive)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.bt_send_to_com = QtWidgets.QPushButton(self.groupBox)
        self.bt_send_to_com.setObjectName("bt_send_to_com")
        self.gridLayout.addWidget(self.bt_send_to_com, 2, 0, 1, 1)
        self.verticalLayout_Serial = QtWidgets.QVBoxLayout()
        self.verticalLayout_Serial.setObjectName("verticalLayout_Serial")
        self.formGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.formGroupBox.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_com_check = QtWidgets.QLabel(self.formGroupBox)
        self.label_com_check.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_com_check.setObjectName("label_com_check")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_com_check)
        self.bt_com_detect = QtWidgets.QPushButton(self.formGroupBox)
        self.bt_com_detect.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.bt_com_detect.setAutoRepeatInterval(100)
        self.bt_com_detect.setDefault(True)
        self.bt_com_detect.setObjectName("bt_com_detect")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bt_com_detect)
        self.label_com_select = QtWidgets.QLabel(self.formGroupBox)
        self.label_com_select.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_com_select.setObjectName("label_com_select")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_com_select)
        self.comBox_com_select = QtWidgets.QComboBox(self.formGroupBox)
        self.comBox_com_select.setObjectName("comBox_com_select")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comBox_com_select)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.label_boud_rate = QtWidgets.QLabel(self.formGroupBox)
        self.label_boud_rate.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_boud_rate.setObjectName("label_boud_rate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_boud_rate)
        self.comBox_boud_rate = QtWidgets.QComboBox(self.formGroupBox)
        self.comBox_boud_rate.setObjectName("comBox_boud_rate")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.comBox_boud_rate.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comBox_boud_rate)
        self.label_data_bit = QtWidgets.QLabel(self.formGroupBox)
        self.label_data_bit.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_data_bit.setObjectName("label_data_bit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_data_bit)
        self.comBox_data_bit = QtWidgets.QComboBox(self.formGroupBox)
        self.comBox_data_bit.setObjectName("comBox_data_bit")
        self.comBox_data_bit.addItem("")
        self.comBox_data_bit.addItem("")
        self.comBox_data_bit.addItem("")
        self.comBox_data_bit.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comBox_data_bit)
        self.label_crc_check = QtWidgets.QLabel(self.formGroupBox)
        self.label_crc_check.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_crc_check.setObjectName("label_crc_check")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_crc_check)
        self.comBox_crc_check = QtWidgets.QComboBox(self.formGroupBox)
        self.comBox_crc_check.setObjectName("comBox_crc_check")
        self.comBox_crc_check.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comBox_crc_check)
        self.label_stop_bit = QtWidgets.QLabel(self.formGroupBox)
        self.label_stop_bit.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_stop_bit.setObjectName("label_stop_bit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_stop_bit)
        self.com_box_stop_bit = QtWidgets.QComboBox(self.formGroupBox)
        self.com_box_stop_bit.setObjectName("com_box_stop_bit")
        self.com_box_stop_bit.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.com_box_stop_bit)
        self.bt_open_com = QtWidgets.QPushButton(self.formGroupBox)
        self.bt_open_com.setStyleSheet("QPushButton{\n"
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
        self.bt_open_com.setObjectName("bt_open_com")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.bt_open_com)
        self.bt_close_com = QtWidgets.QPushButton(self.formGroupBox)
        self.bt_close_com.setStyleSheet("QPushButton{\n"
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
        self.bt_close_com.setObjectName("bt_close_com")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.bt_close_com)
        self.verticalLayout_Serial.addWidget(self.formGroupBox)
        self.formGroupBox_Serial = QtWidgets.QGroupBox(self.groupBox)
        self.formGroupBox_Serial.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.formGroupBox_Serial.setObjectName("formGroupBox_Serial")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox_Serial)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_have_received = QtWidgets.QLabel(self.formGroupBox_Serial)
        self.label_have_received.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_have_received.setObjectName("label_have_received")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_have_received)
        self.lineEdit_have_received = QtWidgets.QLineEdit(self.formGroupBox_Serial)
        self.lineEdit_have_received.setObjectName("lineEdit_have_received")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_have_received)
        self.label_have_tx = QtWidgets.QLabel(self.formGroupBox_Serial)
        self.label_have_tx.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";")
        self.label_have_tx.setObjectName("label_have_tx")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_have_tx)
        self.lineEdit_have_tx = QtWidgets.QLineEdit(self.formGroupBox_Serial)
        self.lineEdit_have_tx.setObjectName("lineEdit_have_tx")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_have_tx)
        self.verticalLayout_Serial.addWidget(self.formGroupBox_Serial)
        self.gridLayout.addLayout(self.verticalLayout_Serial, 0, 0, 1, 1)
        self.textEdit_send_region = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_send_region.setObjectName("textEdit_send_region")
        self.gridLayout.addWidget(self.textEdit_send_region, 1, 0, 1, 1)
        self.textBrowser_receive_region = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_receive_region.setObjectName("textBrowser_receive_region")
        self.gridLayout.addWidget(self.textBrowser_receive_region, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Gimbal)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 60, 251, 701))
        self.groupBox_2.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_open_grab_pulse = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_open_grab_pulse.setStyleSheet("font: 10pt \"Lucida Console\";")
        self.lineEdit_open_grab_pulse.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_open_grab_pulse.setObjectName("lineEdit_open_grab_pulse")
        self.horizontalLayout_3.addWidget(self.lineEdit_open_grab_pulse)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_grab = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_grab.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.bt_grab.setObjectName("bt_grab")
        self.horizontalLayout_2.addWidget(self.bt_grab)
        self.bt_open = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_open.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.bt_open.setObjectName("bt_open")
        self.horizontalLayout_2.addWidget(self.bt_open)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(107, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.slider_pitch_up = QtWidgets.QSlider(self.groupBox_2)
        self.slider_pitch_up.setMinimum(1750)
        self.slider_pitch_up.setMaximum(1950)
        self.slider_pitch_up.setPageStep(2)
        self.slider_pitch_up.setOrientation(QtCore.Qt.Vertical)
        self.slider_pitch_up.setObjectName("slider_pitch_up")
        self.verticalLayout.addWidget(self.slider_pitch_up)
        self.slider_pitch_middle = QtWidgets.QSlider(self.groupBox_2)
        self.slider_pitch_middle.setMinimum(1750)
        self.slider_pitch_middle.setMaximum(1950)
        self.slider_pitch_middle.setPageStep(2)
        self.slider_pitch_middle.setOrientation(QtCore.Qt.Vertical)
        self.slider_pitch_middle.setObjectName("slider_pitch_middle")
        self.verticalLayout.addWidget(self.slider_pitch_middle)
        self.slider_pitch_bottom = QtWidgets.QSlider(self.groupBox_2)
        self.slider_pitch_bottom.setMinimum(1750)
        self.slider_pitch_bottom.setMaximum(1950)
        self.slider_pitch_bottom.setPageStep(2)
        self.slider_pitch_bottom.setOrientation(QtCore.Qt.Vertical)
        self.slider_pitch_bottom.setObjectName("slider_pitch_bottom")
        self.verticalLayout.addWidget(self.slider_pitch_bottom)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.slider_yaw = QtWidgets.QSlider(self.groupBox_2)
        self.slider_yaw.setMinimum(1750)
        self.slider_yaw.setMaximum(1950)
        self.slider_yaw.setSingleStep(1)
        self.slider_yaw.setPageStep(2)
        self.slider_yaw.setSliderPosition(1850)
        self.slider_yaw.setOrientation(QtCore.Qt.Horizontal)
        self.slider_yaw.setInvertedAppearance(False)
        self.slider_yaw.setInvertedControls(False)
        self.slider_yaw.setObjectName("slider_yaw")
        self.verticalLayout_3.addWidget(self.slider_yaw)
        self.bt_all_init = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_all_init.setObjectName("bt_all_init")
        self.verticalLayout_3.addWidget(self.bt_all_init)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Gimbal)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 30, 160, 791))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_pitch_up_value = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_pitch_up_value.setStyleSheet("font: 12pt \"Lucida Console\";")
        self.lineEdit_pitch_up_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pitch_up_value.setObjectName("lineEdit_pitch_up_value")
        self.verticalLayout_4.addWidget(self.lineEdit_pitch_up_value)
        self.lineEdit_pitch_mid_value = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_pitch_mid_value.setStyleSheet("font: 12pt \"Lucida Console\";")
        self.lineEdit_pitch_mid_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pitch_mid_value.setObjectName("lineEdit_pitch_mid_value")
        self.verticalLayout_4.addWidget(self.lineEdit_pitch_mid_value)
        self.lineEdit_pitch_bottom_value = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_pitch_bottom_value.setStyleSheet("font: 12pt \"Lucida Console\";")
        self.lineEdit_pitch_bottom_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pitch_bottom_value.setObjectName("lineEdit_pitch_bottom_value")
        self.verticalLayout_4.addWidget(self.lineEdit_pitch_bottom_value)
        self.lineEdit_yaw_value = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_yaw_value.setStyleSheet("font: 12pt \"Lucida Console\";")
        self.lineEdit_yaw_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_yaw_value.setObjectName("lineEdit_yaw_value")
        self.verticalLayout_4.addWidget(self.lineEdit_yaw_value)
        self.label = QtWidgets.QLabel(Gimbal)
        self.label.setGeometry(QtCore.QRect(480, 170, 72, 15))
        self.label.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Gimbal)
        self.label_2.setGeometry(QtCore.QRect(480, 670, 72, 15))
        self.label_2.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Gimbal)
        self.label_3.setGeometry(QtCore.QRect(480, 330, 72, 15))
        self.label_3.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Gimbal)
        self.label_4.setGeometry(QtCore.QRect(480, 500, 72, 15))
        self.label_4.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Gimbal)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 21, 16))
        self.label_5.setStyleSheet("font: 11pt \"Lucida Console\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_pulse = QtWidgets.QLineEdit(Gimbal)
        self.lineEdit_pulse.setGeometry(QtCore.QRect(106, 20, 251, 23))
        self.lineEdit_pulse.setStyleSheet("font: 10pt \"Lucida Console\";")
        self.lineEdit_pulse.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pulse.setObjectName("lineEdit_pulse")
        self.bt_generate_pulse = QtWidgets.QPushButton(Gimbal)
        self.bt_generate_pulse.setGeometry(QtCore.QRect(380, 20, 158, 23))
        self.bt_generate_pulse.setStyleSheet("font: 10pt \"Lucida Console\";")
        self.bt_generate_pulse.setObjectName("bt_generate_pulse")

        self.retranslateUi(Gimbal)
        self.bt_back.clicked.connect(Gimbal.close)
        QtCore.QMetaObject.connectSlotsByName(Gimbal)

    def retranslateUi(self, Gimbal):
        _translate = QtCore.QCoreApplication.translate
        Gimbal.setWindowTitle(_translate("Gimbal", "Form"))
        self.bt_back.setText(_translate("Gimbal", "Back"))
        self.groupBox.setTitle(_translate("Gimbal", "Serial"))
        self.checkBox_hex_send.setText(_translate("Gimbal", "Hex Send"))
        self.checkBox_hex_receive.setText(_translate("Gimbal", "Hex Receive"))
        self.bt_send_to_com.setText(_translate("Gimbal", "Send"))
        self.formGroupBox.setTitle(_translate("Gimbal", "串口设置"))
        self.label_com_check.setText(_translate("Gimbal", "串口检测："))
        self.bt_com_detect.setText(_translate("Gimbal", "检测串口"))
        self.label_com_select.setText(_translate("Gimbal", "串口选择："))
        self.label_boud_rate.setText(_translate("Gimbal", "波特率："))
        self.comBox_boud_rate.setItemText(0, _translate("Gimbal", "115200"))
        self.comBox_boud_rate.setItemText(1, _translate("Gimbal", "2400"))
        self.comBox_boud_rate.setItemText(2, _translate("Gimbal", "4800"))
        self.comBox_boud_rate.setItemText(3, _translate("Gimbal", "9600"))
        self.comBox_boud_rate.setItemText(4, _translate("Gimbal", "14400"))
        self.comBox_boud_rate.setItemText(5, _translate("Gimbal", "19200"))
        self.comBox_boud_rate.setItemText(6, _translate("Gimbal", "38400"))
        self.comBox_boud_rate.setItemText(7, _translate("Gimbal", "57600"))
        self.comBox_boud_rate.setItemText(8, _translate("Gimbal", "76800"))
        self.comBox_boud_rate.setItemText(9, _translate("Gimbal", "12800"))
        self.comBox_boud_rate.setItemText(10, _translate("Gimbal", "230400"))
        self.comBox_boud_rate.setItemText(11, _translate("Gimbal", "460800"))
        self.label_data_bit.setText(_translate("Gimbal", "数据位："))
        self.comBox_data_bit.setItemText(0, _translate("Gimbal", "8"))
        self.comBox_data_bit.setItemText(1, _translate("Gimbal", "7"))
        self.comBox_data_bit.setItemText(2, _translate("Gimbal", "6"))
        self.comBox_data_bit.setItemText(3, _translate("Gimbal", "5"))
        self.label_crc_check.setText(_translate("Gimbal", "校验位："))
        self.comBox_crc_check.setItemText(0, _translate("Gimbal", "N"))
        self.label_stop_bit.setText(_translate("Gimbal", "停止位："))
        self.com_box_stop_bit.setItemText(0, _translate("Gimbal", "1"))
        self.bt_open_com.setText(_translate("Gimbal", "打开串口"))
        self.bt_close_com.setText(_translate("Gimbal", "关闭串口"))
        self.formGroupBox_Serial.setTitle(_translate("Gimbal", "串口状态"))
        self.label_have_received.setText(_translate("Gimbal", "已接收："))
        self.label_have_tx.setText(_translate("Gimbal", "已发送："))
        self.groupBox_2.setTitle(_translate("Gimbal", "Servo"))
        self.bt_grab.setText(_translate("Gimbal", "Grab"))
        self.bt_open.setText(_translate("Gimbal", "Open"))
        self.bt_all_init.setText(_translate("Gimbal", "All Init"))
        self.label.setText(_translate("Gimbal", "G"))
        self.label_2.setText(_translate("Gimbal", "H"))
        self.label_3.setText(_translate("Gimbal", "F"))
        self.label_4.setText(_translate("Gimbal", "E"))
        self.label_5.setText(_translate("Gimbal", "D"))
        self.bt_generate_pulse.setText(_translate("Gimbal", "Generate Pulse"))