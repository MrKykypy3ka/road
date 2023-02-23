from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class ClickedLabel(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

class Ui_addForm(object):
    def setupUi(self, addForm):
        addForm.setObjectName("addForm")
        addForm.resize(671, 760)
        self.addTimeButton = QtWidgets.QPushButton(addForm)
        self.addTimeButton.setGeometry(QtCore.QRect(520, 240, 141, 23))
        self.addTimeButton.setObjectName("addTimeButton")
        self.addRoadButton = QtWidgets.QPushButton(addForm)
        self.addRoadButton.setGeometry(QtCore.QRect(180, 240, 161, 23))
        self.addRoadButton.setObjectName("addRoadButton")
        self.addCrossroadButton = QtWidgets.QPushButton(addForm)
        self.addCrossroadButton.setGeometry(QtCore.QRect(350, 240, 161, 23))
        self.addCrossroadButton.setObjectName("addCrossroadButton")
        self.latitudeEdit = QtWidgets.QLineEdit(addForm)
        self.latitudeEdit.setGeometry(QtCore.QRect(60, 270, 111, 20))
        self.latitudeEdit.setObjectName("latitudeEdit")
        self.longitudeEdit = QtWidgets.QLineEdit(addForm)
        self.longitudeEdit.setGeometry(QtCore.QRect(230, 270, 111, 20))
        self.longitudeEdit.setObjectName("longitudeEdit")
        self.label = QtWidgets.QLabel(addForm)
        self.label.setGeometry(QtCore.QRect(10, 270, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addForm)
        self.label_2.setGeometry(QtCore.QRect(180, 270, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addForm)
        self.label_3.setGeometry(QtCore.QRect(10, -10, 161, 41))
        self.label_3.setObjectName("label_3")
        self.timeEdit = QtWidgets.QTimeEdit(addForm)
        self.timeEdit.setGeometry(QtCore.QRect(520, 210, 141, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_4 = QtWidgets.QLabel(addForm)
        self.label_4.setGeometry(QtCore.QRect(520, -8, 141, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(addForm)
        self.label_5.setGeometry(QtCore.QRect(180, -10, 161, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(addForm)
        self.label_6.setGeometry(QtCore.QRect(350, -10, 161, 41))
        self.label_6.setObjectName("label_6")
        self.imageMap = ClickedLabel(addForm)
        self.imageMap.setGeometry(QtCore.QRect(10, 300, 649, 449))
        self.imageMap.setText("")
        self.imageMap.setObjectName("imageMap")
        self.addBadRoadButton = QtWidgets.QPushButton(addForm)
        self.addBadRoadButton.setGeometry(QtCore.QRect(10, 240, 161, 21))
        self.addBadRoadButton.setObjectName("addBadRoadButton")
        self.badRoadList = QtWidgets.QListWidget(addForm)
        self.badRoadList.setGeometry(QtCore.QRect(10, 21, 161, 211))
        self.badRoadList.setObjectName("badRoadList")
        self.roadList = QtWidgets.QListWidget(addForm)
        self.roadList.setGeometry(QtCore.QRect(180, 20, 161, 211))
        self.roadList.setObjectName("roadList")
        self.crossroadList = QtWidgets.QListWidget(addForm)
        self.crossroadList.setGeometry(QtCore.QRect(350, 20, 161, 211))
        self.crossroadList.setObjectName("crossroadList")
        self.timeList = QtWidgets.QListWidget(addForm)
        self.timeList.setGeometry(QtCore.QRect(520, 20, 141, 181))
        self.timeList.setObjectName("timeList")
        self.coor = QtWidgets.QLabel(addForm)
        self.coor.setGeometry(QtCore.QRect(10, 320, 71, 31))
        self.coor.setObjectName("coor")
        self.saveButton = QtWidgets.QPushButton(addForm)
        self.saveButton.setGeometry(QtCore.QRect(520, 270, 141, 23))
        self.saveButton.setObjectName("saveButton")
        self.comboBox = QtWidgets.QComboBox(addForm)
        self.comboBox.setGeometry(QtCore.QRect(350, 270, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "Карта")
        self.comboBox.addItem("")

        self.retranslateUi(addForm)
        QtCore.QMetaObject.connectSlotsByName(addForm)

    def retranslateUi(self, addForm):
        _translate = QtCore.QCoreApplication.translate
        addForm.setWindowTitle(_translate("addForm", "Добавить данные"))
        self.addTimeButton.setText(_translate("addForm", "Добавить время"))
        self.addRoadButton.setText(_translate("addForm", "Добавить объезд"))
        self.addCrossroadButton.setText(_translate("addForm", "Добавить перекрёсток"))
        self.latitudeEdit.setText(_translate("addForm", "50.25958"))
        self.longitudeEdit.setText(_translate("addForm", "127.54389"))
        self.label.setText(_translate("addForm", "Долгота:"))
        self.label_2.setText(_translate("addForm", "Широта:"))
        self.label_3.setText(_translate("addForm", "<html><head/><body><p>Ремонтируемые участки</p></body></html>"))
        self.label_4.setText(_translate("addForm", "Время для сбора данных"))
        self.label_5.setText(_translate("addForm", "Улицы для объезда"))
        self.label_6.setText(_translate("addForm", "Перекрёстки для объезда"))
        self.addBadRoadButton.setText(_translate("addForm", "Добавть участок"))
        self.coor.setText(_translate("addForm", "<html>\n"
"<body>\n"
"  <style>\n"
"   p {\n"
"    margin-top: 0.1em; /* Отступ сверху */\n"
"    margin-bottom: 0.1em; /* Отступ снизу */\n"
"   }\n"
"  </style>\n"
"<p> </p>\n"
"<p> </p>\n"
"</body>\n"
"</html>"))
        self.saveButton.setText(_translate("addForm", "Сохранить"))
        self.comboBox.setItemText(0, _translate("addForm", "Карта и нагрузка"))
        self.comboBox.setItemText(2, _translate("addForm", "Нагрузка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addForm = QtWidgets.QWidget()
    ui = Ui_addForm()
    ui.setupUi(addForm)
    addForm.show()
    sys.exit(app.exec_())
