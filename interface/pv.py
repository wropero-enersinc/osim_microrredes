# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pv.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 438)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 411, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setMaximum(10000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_4.setDecimals(4)
        self.doubleSpinBox_4.setMaximum(10000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 2, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 3, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_3.setDecimals(4)
        self.doubleSpinBox_3.setMaximum(10000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 4, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_5.setFont(font)
        self.doubleSpinBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_5.setDecimals(4)
        self.doubleSpinBox_5.setMaximum(10000.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 5, 1, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_6.setFont(font)
        self.doubleSpinBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_6.setDecimals(4)
        self.doubleSpinBox_6.setMaximum(10000.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 6, 1, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_7.setFont(font)
        self.doubleSpinBox_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_7.setDecimals(4)
        self.doubleSpinBox_7.setMaximum(10000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.doubleSpinBox_7, 7, 1, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_8.setFont(font)
        self.doubleSpinBox_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_8.setDecimals(4)
        self.doubleSpinBox_8.setMinimum(-1000.0)
        self.doubleSpinBox_8.setMaximum(10000.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.doubleSpinBox_8, 8, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(30, 20, 411, 31))
        self.label_16.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Photovoltaic derating factor(%)"))
        self.label_4.setText(_translate("Dialog", "Price per kWh generated(USD/kWh)"))
        self.label_2.setText(_translate("Dialog", "Module Efficiency(%)"))
        self.label_3.setText(_translate("Dialog", "NOCT(◦C)"))
        self.label_6.setText(_translate("Dialog", "O&M factor initial investment(%)"))
        self.label_7.setText(_translate("Dialog", "Price per kW installed (USD/kW)"))
        self.label_8.setText(_translate("Dialog", "Power Temperature Coefficient (%/◦C)"))
        self.label.setText(_translate("Dialog", "Maximum Power Wp"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Parameters PV</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
