# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setlinerole.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_setlinerole(object):
    def setupUi(self, setlinerole):
        setlinerole.setObjectName("setlinerole")
        setlinerole.setWindowModality(QtCore.Qt.NonModal)
        setlinerole.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setlinerole.sizePolicy().hasHeightForWidth())
        setlinerole.setSizePolicy(sizePolicy)
        setlinerole.setMaximumSize(QtCore.QSize(600, 600))
        self.set_ok = QtWidgets.QPushButton(setlinerole)
        self.set_ok.setGeometry(QtCore.QRect(462, 550, 111, 35))
        self.set_ok.setMinimumSize(QtCore.QSize(0, 35))
        self.set_ok.setObjectName("set_ok")
        self.verticalLayoutWidget = QtWidgets.QWidget(setlinerole)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 541, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.select_role = QtWidgets.QComboBox(setlinerole)
        self.select_role.setGeometry(QtCore.QRect(140, 550, 171, 35))
        self.select_role.setMinimumSize(QtCore.QSize(100, 35))
        self.select_role.setObjectName("select_role")
        self.set_role_label = QtWidgets.QLabel(setlinerole)
        self.set_role_label.setGeometry(QtCore.QRect(30, 560, 81, 16))
        self.set_role_label.setText("")
        self.set_role_label.setObjectName("set_role_label")

        self.retranslateUi(setlinerole)
        QtCore.QMetaObject.connectSlotsByName(setlinerole)

    def retranslateUi(self, setlinerole):
        _translate = QtCore.QCoreApplication.translate
        setlinerole.setWindowTitle(_translate("setlinerole", "Set up multiple roles"))
        self.set_ok.setText(_translate("setlinerole", "OK"))
