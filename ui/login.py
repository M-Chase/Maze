# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.LoginDialog = QtWidgets.QPushButton(Dialog)
        self.LoginDialog.setGeometry(QtCore.QRect(70, 140, 93, 28))
        self.LoginDialog.setObjectName("LoginDialog")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 140, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.account = QtWidgets.QLineEdit(Dialog)
        self.account.setGeometry(QtCore.QRect(150, 50, 113, 21))
        self.account.setObjectName("account")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 90, 113, 21))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 72, 15))
        self.label_2.setObjectName("label_2")
        # 自定义信号
        self.LoginDialog.clicked.connect(self.processLogin)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LoginDialog.setText(_translate("Dialog", "登陆"))
        self.pushButton_2.setText(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))

    def processLogin(self):
        account=self.account.text()
        password=self.password.text()
        if(account=="123" and password=="123"):
            print("登陆成功")
            # box=QtWidgets.QMessageBox
            # button=QPushButton
            # box.information(self,"提示","登录成功", button)
            # box.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QtWidgets.QDialog()
    login_dialog=Ui_Dialog()
    login_dialog.setupUi(main)
    main.show()
    sys.exit(app.exec())