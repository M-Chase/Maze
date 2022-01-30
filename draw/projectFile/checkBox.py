# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from mazeUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class CheckBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setObjectName("Form")
        self.resize(662, 551)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(110, 140, 461, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sureBtn = QtWidgets.QPushButton(self.widget)
        self.sureBtn.setObjectName("sureBtn")
        self.gridLayout.addWidget(self.sureBtn, 3, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        self.label.setObjectName("label")
        self.arithBox = QtWidgets.QComboBox(self.splitter_3)
        self.arithBox.setObjectName("arithBox")
        self.arithBox.addItem("")
        self.arithBox.addItem("")
        self.arithBox.addItem("")
        self.gridLayout.addWidget(self.splitter_3, 2, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.width = QtWidgets.QLabel(self.splitter_2)
        self.width.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.width.setObjectName("width")
        self.width_num = QtWidgets.QSpinBox(self.splitter_2)
        self.width_num.setMinimum(5)
        self.width_num.setMaximum(20)
        self.width_num.setObjectName("width_num")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.height = QtWidgets.QLabel(self.splitter)
        self.height.setObjectName("height")
        self.height_num = QtWidgets.QSpinBox(self.splitter)
        self.height_num.setMinimum(5)
        self.height_num.setMaximum(20)
        self.height_num.setObjectName("height_num")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.heightNum=None
        self.widthNum=None
        self.arith="A*"
        self.openBool=False

        # self.sureBtn.clicked.connect(self.update)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.sureBtn.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "算法选择"))
        self.arithBox.setItemText(0, _translate("Form", "A*"))
        self.arithBox.setItemText(1, _translate("Form", "DFS"))
        self.arithBox.setItemText(2, _translate("Form", "greed"))
        self.width.setText(_translate("Form", "宽"))
        self.height.setText(_translate("Form", "高"))

    def update(self):
        self.heightNum=self.height_num.text()
        self.widthNum=self.width_num.text()
        self.arith=self.arithBox.currentText()
        self.openBool=True
        print(self.heightNum,self.widthNum,self.arith)
if __name__=='__main__':
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    main=CheckBox()
    mazeUI=Ui_Form()
    main.show()
    main.sureBtn.released.connect(main.close)
    main.sureBtn.clicked.connect(lambda :main.update())
    main.sureBtn.released.connect(mazeUI.show)

    sys.exit(app.exec_())