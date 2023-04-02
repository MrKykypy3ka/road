# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\forms\list_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listForm(object):
    def setupUi(self, listForm):
        listForm.setObjectName("listForm")
        listForm.resize(472, 251)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listForm.setWindowIcon(icon)
        self.viewGroupButton = QtWidgets.QPushButton(listForm)
        self.viewGroupButton.setGeometry(QtCore.QRect(20, 190, 131, 21))
        self.viewGroupButton.setObjectName("viewGroupButton")
        self.dateEdit_2 = QtWidgets.QDateEdit(listForm)
        self.dateEdit_2.setGeometry(QtCore.QRect(300, 80, 161, 22))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.addGroupButton = QtWidgets.QPushButton(listForm)
        self.addGroupButton.setGeometry(QtCore.QRect(20, 220, 131, 21))
        self.addGroupButton.setObjectName("addGroupButton")
        self.groupList = QtWidgets.QListWidget(listForm)
        self.groupList.setGeometry(QtCore.QRect(20, 30, 131, 151))
        self.groupList.setObjectName("groupList")
        self.dateEdit = QtWidgets.QDateEdit(listForm)
        self.dateEdit.setGeometry(QtCore.QRect(300, 30, 161, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(listForm)
        self.label_7.setGeometry(QtCore.QRect(20, 0, 141, 41))
        self.label_7.setObjectName("label_7")
        self.timeList = QtWidgets.QListWidget(listForm)
        self.timeList.setGeometry(QtCore.QRect(160, 30, 131, 151))
        self.timeList.setObjectName("timeList")
        self.addTimeButton = QtWidgets.QPushButton(listForm)
        self.addTimeButton.setGeometry(QtCore.QRect(160, 220, 131, 23))
        self.addTimeButton.setObjectName("addTimeButton")
        self.timeEdit = QtWidgets.QTimeEdit(listForm)
        self.timeEdit.setGeometry(QtCore.QRect(160, 190, 131, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_4 = QtWidgets.QLabel(listForm)
        self.label_4.setGeometry(QtCore.QRect(160, 2, 141, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(listForm)
        self.label_5.setGeometry(QtCore.QRect(300, 10, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(listForm)
        self.label_6.setGeometry(QtCore.QRect(300, 60, 161, 16))
        self.label_6.setObjectName("label_6")
        self.saveButton = QtWidgets.QPushButton(listForm)
        self.saveButton.setGeometry(QtCore.QRect(300, 170, 161, 71))
        self.saveButton.setObjectName("saveButton")
        self.delAreaButton = QtWidgets.QPushButton(listForm)
        self.delAreaButton.setGeometry(QtCore.QRect(300, 110, 161, 21))
        self.delAreaButton.setObjectName("delAreaButton")
        self.delTimeButton = QtWidgets.QPushButton(listForm)
        self.delTimeButton.setGeometry(QtCore.QRect(300, 140, 161, 21))
        self.delTimeButton.setObjectName("delTimeButton")

        self.retranslateUi(listForm)
        QtCore.QMetaObject.connectSlotsByName(listForm)

    def retranslateUi(self, listForm):
        _translate = QtCore.QCoreApplication.translate
        listForm.setWindowTitle(_translate("listForm", "Конфигурация анализа"))
        self.viewGroupButton.setText(_translate("listForm", "Редактировать"))
        self.addGroupButton.setText(_translate("listForm", "Добавть"))
        self.label_7.setText(_translate("listForm", "<html><head/><body><p>Группы участков</p></body></html>"))
        self.addTimeButton.setText(_translate("listForm", "Добавить время"))
        self.label_4.setText(_translate("listForm", "Время сбора данных"))
        self.label_5.setText(_translate("listForm", "Дата начала сбора данных"))
        self.label_6.setText(_translate("listForm", "Дата окончания сбора данных"))
        self.saveButton.setText(_translate("listForm", "Сохранить конфигурацию"))
        self.delAreaButton.setText(_translate("listForm", "Удалить группу"))
        self.delTimeButton.setText(_translate("listForm", "Удалить время"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listForm = QtWidgets.QWidget()
    ui = Ui_listForm()
    ui.setupUi(listForm)
    listForm.show()
    sys.exit(app.exec_())
