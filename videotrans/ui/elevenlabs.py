# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elevenlabs.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_elevenlabsform(object):
    def setupUi(self, elevenlabsform):
        elevenlabsform.setObjectName("elevenlabsform")
        elevenlabsform.setWindowModality(QtCore.Qt.NonModal)
        elevenlabsform.resize(400, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elevenlabsform.sizePolicy().hasHeightForWidth())
        elevenlabsform.setSizePolicy(sizePolicy)
        elevenlabsform.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(elevenlabsform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(elevenlabsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.elevenlabstts_key = QtWidgets.QLineEdit(elevenlabsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elevenlabstts_key.sizePolicy().hasHeightForWidth())
        self.elevenlabstts_key.setSizePolicy(sizePolicy)
        self.elevenlabstts_key.setMinimumSize(QtCore.QSize(210, 35))
        self.elevenlabstts_key.setObjectName("elevenlabstts_key")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.elevenlabstts_key)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.set = QtWidgets.QPushButton(elevenlabsform)
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        self.set.setObjectName("set")
        self.verticalLayout_2.addWidget(self.set)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(elevenlabsform)
        QtCore.QMetaObject.connectSlotsByName(elevenlabsform)

    def retranslateUi(self, elevenlabsform):
        _translate = QtCore.QCoreApplication.translate
        elevenlabsform.setWindowTitle(_translate("elevenlabsform", "elevenlabs"))
        self.label.setText(_translate("elevenlabsform", "API_KEY"))
        self.set.setText(_translate("elevenlabsform", "OK"))
