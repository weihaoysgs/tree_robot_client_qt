# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(941, 863)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 20, 181, 321))
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
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(210, 20, 401, 241))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(210, 280, 401, 101))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.s3__send_button = QtWidgets.QPushButton(Form)
        self.s3__send_button.setGeometry(QtCore.QRect(620, 310, 61, 31))
        self.s3__send_button.setObjectName("s3__send_button")
        self.s3__clear_button = QtWidgets.QPushButton(Form)
        self.s3__clear_button.setGeometry(QtCore.QRect(620, 350, 61, 31))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(20, 340, 181, 101))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.hex_send = QtWidgets.QCheckBox(Form)
        self.hex_send.setGeometry(QtCore.QRect(620, 280, 81, 16))
        self.hex_send.setObjectName("hex_send")
        self.hex_receive = QtWidgets.QCheckBox(Form)
        self.hex_receive.setGeometry(QtCore.QRect(620, 40, 81, 16))
        self.hex_receive.setObjectName("hex_receive")
        self.s2__clear_button = QtWidgets.QPushButton(Form)
        self.s2__clear_button.setGeometry(QtCore.QRect(620, 80, 61, 31))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.timer_send_cb = QtWidgets.QCheckBox(Form)
        self.timer_send_cb.setGeometry(QtCore.QRect(230, 390, 101, 20))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 390, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dw = QtWidgets.QLabel(Form)
        self.dw.setGeometry(QtCore.QRect(420, 390, 54, 20))
        self.dw.setObjectName("dw")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 440, 221, 241))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pitch_label = QtWidgets.QLabel(self.groupBox)
        self.pitch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pitch_label.setObjectName("pitch_label")
        self.verticalLayout_4.addWidget(self.pitch_label)
        self.yaw_label = QtWidgets.QLabel(self.groupBox)
        self.yaw_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yaw_label.setObjectName("yaw_label")
        self.verticalLayout_4.addWidget(self.yaw_label)
        self.raw = QtWidgets.QLabel(self.groupBox)
        self.raw.setAlignment(QtCore.Qt.AlignCenter)
        self.raw.setObjectName("raw")
        self.verticalLayout_4.addWidget(self.raw)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pitch_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.pitch_line_edit.setObjectName("pitch_line_edit")
        self.verticalLayout_3.addWidget(self.pitch_line_edit)
        self.yaw_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.yaw_line_edit.setObjectName("yaw_line_edit")
        self.verticalLayout_3.addWidget(self.yaw_line_edit)
        self.row_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.row_line_edit.setObjectName("row_line_edit")
        self.verticalLayout_3.addWidget(self.row_line_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.ServoCtrl = QtWidgets.QGroupBox(Form)
        self.ServoCtrl.setGeometry(QtCore.QRect(220, 420, 491, 361))
        self.ServoCtrl.setObjectName("ServoCtrl")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ServoCtrl)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_yaw_servo = QtWidgets.QLabel(self.ServoCtrl)
        self.label_yaw_servo.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_yaw_servo.setObjectName("label_yaw_servo")
        self.horizontalLayout_2.addWidget(self.label_yaw_servo)
        self.line_edit_yaw_servo_value = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_yaw_servo_value.setObjectName("line_edit_yaw_servo_value")
        self.horizontalLayout_2.addWidget(self.line_edit_yaw_servo_value)
        self.bt_yaw_servo_compare_value_add = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_yaw_servo_compare_value_add.setObjectName("bt_yaw_servo_compare_value_add")
        self.horizontalLayout_2.addWidget(self.bt_yaw_servo_compare_value_add)
        self.bt_yaw_servo_compare_value_desc = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_yaw_servo_compare_value_desc.setObjectName("bt_yaw_servo_compare_value_desc")
        self.horizontalLayout_2.addWidget(self.bt_yaw_servo_compare_value_desc)
        self.bt_yaw_servo_value_send = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_yaw_servo_value_send.setObjectName("bt_yaw_servo_value_send")
        self.horizontalLayout_2.addWidget(self.bt_yaw_servo_value_send)
        self.horizontalLayout_2.setStretch(4, 3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_pitch_servo_low = QtWidgets.QLabel(self.ServoCtrl)
        self.label_pitch_servo_low.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pitch_servo_low.setObjectName("label_pitch_servo_low")
        self.horizontalLayout_3.addWidget(self.label_pitch_servo_low)
        self.line_edit_pitch_low_servo = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_pitch_low_servo.setObjectName("line_edit_pitch_low_servo")
        self.horizontalLayout_3.addWidget(self.line_edit_pitch_low_servo)
        self.bt_pitch_low_add = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_low_add.setObjectName("bt_pitch_low_add")
        self.horizontalLayout_3.addWidget(self.bt_pitch_low_add)
        self.bt_pitch_low_desc = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_low_desc.setObjectName("bt_pitch_low_desc")
        self.horizontalLayout_3.addWidget(self.bt_pitch_low_desc)
        self.bt_pitch_low_send = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_low_send.setObjectName("bt_pitch_low_send")
        self.horizontalLayout_3.addWidget(self.bt_pitch_low_send)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_pitch_middle = QtWidgets.QLabel(self.ServoCtrl)
        self.label_pitch_middle.setObjectName("label_pitch_middle")
        self.horizontalLayout_4.addWidget(self.label_pitch_middle)
        self.line_edit_pitch_middle = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_pitch_middle.setObjectName("line_edit_pitch_middle")
        self.horizontalLayout_4.addWidget(self.line_edit_pitch_middle)
        self.bt_pitch_middle_add = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_middle_add.setObjectName("bt_pitch_middle_add")
        self.horizontalLayout_4.addWidget(self.bt_pitch_middle_add)
        self.bt_pitch_middle_desc = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_middle_desc.setObjectName("bt_pitch_middle_desc")
        self.horizontalLayout_4.addWidget(self.bt_pitch_middle_desc)
        self.bt_pitch_middle_send = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_middle_send.setObjectName("bt_pitch_middle_send")
        self.horizontalLayout_4.addWidget(self.bt_pitch_middle_send)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_pitch_up = QtWidgets.QLabel(self.ServoCtrl)
        self.label_pitch_up.setObjectName("label_pitch_up")
        self.horizontalLayout_5.addWidget(self.label_pitch_up)
        self.line_edit_pitch_up = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_pitch_up.setObjectName("line_edit_pitch_up")
        self.horizontalLayout_5.addWidget(self.line_edit_pitch_up)
        self.bt_pitch_up_add = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_up_add.setObjectName("bt_pitch_up_add")
        self.horizontalLayout_5.addWidget(self.bt_pitch_up_add)
        self.bt_pitch_up_desc = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_up_desc.setObjectName("bt_pitch_up_desc")
        self.horizontalLayout_5.addWidget(self.bt_pitch_up_desc)
        self.bt_pitch_up_send = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_pitch_up_send.setObjectName("bt_pitch_up_send")
        self.horizontalLayout_5.addWidget(self.bt_pitch_up_send)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_grab = QtWidgets.QLabel(self.ServoCtrl)
        self.label_grab.setObjectName("label_grab")
        self.horizontalLayout_6.addWidget(self.label_grab)
        self.line_edit_grab = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_grab.setObjectName("line_edit_grab")
        self.horizontalLayout_6.addWidget(self.line_edit_grab)
        self.bt_grab_add = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_grab_add.setObjectName("bt_grab_add")
        self.horizontalLayout_6.addWidget(self.bt_grab_add)
        self.bt_grab_desc = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_grab_desc.setObjectName("bt_grab_desc")
        self.horizontalLayout_6.addWidget(self.bt_grab_desc)
        self.bt_grab_send = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_grab_send.setObjectName("bt_grab_send")
        self.horizontalLayout_6.addWidget(self.bt_grab_send)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_edit_five_servo_compare_value = QtWidgets.QLineEdit(self.ServoCtrl)
        self.line_edit_five_servo_compare_value.setObjectName("line_edit_five_servo_compare_value")
        self.horizontalLayout_7.addWidget(self.line_edit_five_servo_compare_value)
        self.bt_all_deinit = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_all_deinit.setObjectName("bt_all_deinit")
        self.horizontalLayout_7.addWidget(self.bt_all_deinit)
        self.bt_generate_compare_value = QtWidgets.QPushButton(self.ServoCtrl)
        self.bt_generate_compare_value.setObjectName("bt_generate_compare_value")
        self.horizontalLayout_7.addWidget(self.bt_generate_compare_value)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(710, 420, 41, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.layout_pin_remap = QtWidgets.QVBoxLayout()
        self.layout_pin_remap.setObjectName("layout_pin_remap")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.layout_pin_remap.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.layout_pin_remap.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layout_pin_remap.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layout_pin_remap.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.layout_pin_remap.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.layout_pin_remap.addWidget(self.label_9)
        self.verticalLayout_6.addLayout(self.layout_pin_remap)
        self.label_logo_img = QtWidgets.QLabel(Form)
        self.label_logo_img.setGeometry(QtCore.QRect(700, 50, 197, 235))
        self.label_logo_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo_img.setObjectName("label_logo_img")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.s3__send_button.raise_()
        self.s3__clear_button.raise_()
        self.formGroupBox.raise_()
        self.hex_send.raise_()
        self.hex_receive.raise_()
        self.s2__clear_button.raise_()
        self.timer_send_cb.raise_()
        self.lineEdit_3.raise_()
        self.dw.raise_()
        self.groupBox.raise_()
        self.ServoCtrl.raise_()
        self.groupBox_2.raise_()
        self.label_logo_img.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "????????????"))
        self.s1__lb_1.setText(_translate("Form", "???????????????"))
        self.s1__box_1.setText(_translate("Form", "????????????"))
        self.s1__lb_2.setText(_translate("Form", "???????????????"))
        self.s1__lb_3.setText(_translate("Form", "????????????"))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "????????????"))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "????????????"))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.open_button.setText(_translate("Form", "????????????"))
        self.close_button.setText(_translate("Form", "????????????"))
        self.s1__lb_6.setText(_translate("Form", "????????????"))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.verticalGroupBox.setTitle(_translate("Form", "?????????"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "?????????"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123456</p></body></html>"))
        self.s3__send_button.setText(_translate("Form", "??????"))
        self.s3__clear_button.setText(_translate("Form", "??????"))
        self.formGroupBox1.setTitle(_translate("Form", "????????????"))
        self.label.setText(_translate("Form", "????????????"))
        self.label_2.setText(_translate("Form", "????????????"))
        self.hex_send.setText(_translate("Form", "Hex??????"))
        self.hex_receive.setText(_translate("Form", "Hex??????"))
        self.s2__clear_button.setText(_translate("Form", "??????"))
        self.timer_send_cb.setText(_translate("Form", "????????????"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms/???"))
        self.groupBox.setTitle(_translate("Form", "JY901"))
        self.pitch_label.setText(_translate("Form", "pitch"))
        self.yaw_label.setText(_translate("Form", "yaw"))
        self.raw.setText(_translate("Form", "row"))
        self.ServoCtrl.setTitle(_translate("Form", "Servo Ctrl"))
        self.label_yaw_servo.setText(_translate("Form", "    Yaw     "))
        self.bt_yaw_servo_compare_value_add.setText(_translate("Form", "+"))
        self.bt_yaw_servo_compare_value_desc.setText(_translate("Form", "-"))
        self.bt_yaw_servo_value_send.setText(_translate("Form", "send"))
        self.label_pitch_servo_low.setText(_translate("Form", "Pitch Low   "))
        self.bt_pitch_low_add.setText(_translate("Form", "+"))
        self.bt_pitch_low_desc.setText(_translate("Form", "-"))
        self.bt_pitch_low_send.setText(_translate("Form", "send"))
        self.label_pitch_middle.setText(_translate("Form", "Pitch Middle"))
        self.bt_pitch_middle_add.setText(_translate("Form", "+"))
        self.bt_pitch_middle_desc.setText(_translate("Form", "-"))
        self.bt_pitch_middle_send.setText(_translate("Form", "send"))
        self.label_pitch_up.setText(_translate("Form", "  Pitch Up  "))
        self.bt_pitch_up_add.setText(_translate("Form", "+"))
        self.bt_pitch_up_desc.setText(_translate("Form", "-"))
        self.bt_pitch_up_send.setText(_translate("Form", "send"))
        self.label_grab.setText(_translate("Form", "    Grab    "))
        self.bt_grab_add.setText(_translate("Form", "grab +"))
        self.bt_grab_desc.setText(_translate("Form", "open -"))
        self.bt_grab_send.setText(_translate("Form", "send"))
        self.bt_all_deinit.setText(_translate("Form", "all deinit"))
        self.bt_generate_compare_value.setText(_translate("Form", "gengrate compare value"))
        self.groupBox_2.setTitle(_translate("Form", "Pin"))
        self.label_3.setText(_translate("Form", "H"))
        self.label_4.setText(_translate("Form", "E"))
        self.label_6.setText(_translate("Form", "F"))
        self.label_5.setText(_translate("Form", "G"))
        self.label_7.setText(_translate("Form", "D"))
        self.label_9.setText(_translate("Form", " "))
        self.label_logo_img.setText(_translate("Form", "label_logo_img"))
