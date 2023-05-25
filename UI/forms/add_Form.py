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
        self.addRoadButton = QtWidgets.QPushButton(addForm)
        self.addRoadButton.setGeometry(QtCore.QRect(190, 240, 171, 23))
        self.addRoadButton.setObjectName("addRoadButton")
        self.addCrossroadButton = QtWidgets.QPushButton(addForm)
        self.addCrossroadButton.setGeometry(QtCore.QRect(370, 240, 171, 23))
        self.addCrossroadButton.setObjectName("addCrossroadButton")
        self.latitudeEdit = QtWidgets.QLineEdit(addForm)
        self.latitudeEdit.setGeometry(QtCore.QRect(60, 270, 121, 20))
        self.latitudeEdit.setObjectName("latitudeEdit")
        self.longitudeEdit = QtWidgets.QLineEdit(addForm)
        self.longitudeEdit.setGeometry(QtCore.QRect(240, 270, 121, 20))
        self.longitudeEdit.setObjectName("longitudeEdit")
        self.label = QtWidgets.QLabel(addForm)
        self.label.setGeometry(QtCore.QRect(10, 270, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addForm)
        self.label_2.setGeometry(QtCore.QRect(190, 270, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addForm)
        self.label_3.setGeometry(QtCore.QRect(10, -10, 141, 41))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(addForm)
        self.label_5.setGeometry(QtCore.QRect(190, -10, 141, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(addForm)
        self.label_6.setGeometry(QtCore.QRect(370, -10, 141, 41))
        self.label_6.setObjectName("label_6")
        self.imageMap = ClickedLabel(addForm)
        self.imageMap.setGeometry(QtCore.QRect(10, 300, 649, 449))
        self.imageMap.setText("")
        self.imageMap.setObjectName("imageMap")
        self.addBadRoadButton = QtWidgets.QPushButton(addForm)
        self.addBadRoadButton.setGeometry(QtCore.QRect(10, 240, 171, 21))
        self.addBadRoadButton.setObjectName("addBadRoadButton")
        self.badRoadList = QtWidgets.QListWidget(addForm)
        self.badRoadList.setGeometry(QtCore.QRect(10, 21, 171, 211))
        self.badRoadList.setObjectName("badRoadList")
        self.roadList = QtWidgets.QListWidget(addForm)
        self.roadList.setGeometry(QtCore.QRect(190, 20, 171, 211))
        self.roadList.setObjectName("roadList")
        self.crossroadList = QtWidgets.QListWidget(addForm)
        self.crossroadList.setGeometry(QtCore.QRect(370, 20, 171, 211))
        self.crossroadList.setObjectName("crossroadList")
        self.coor = QtWidgets.QLabel(addForm)
        self.coor.setGeometry(QtCore.QRect(590, 240, 71, 31))
        self.coor.setObjectName("coor")
        self.saveButton = QtWidgets.QPushButton(addForm)
        self.saveButton.setGeometry(QtCore.QRect(550, 242, 111, 51))
        self.saveButton.setObjectName("saveButton")
        self.comboBox = QtWidgets.QComboBox(addForm)
        self.comboBox.setGeometry(QtCore.QRect(370, 270, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "Карта")
        self.comboBox.addItem("")
        self.delBadButton = QtWidgets.QPushButton(addForm)
        self.delBadButton.setGeometry(QtCore.QRect(550, 20, 111, 21))
        self.delBadButton.setObjectName("delBadButton")
        self.delCrossroadButton = QtWidgets.QPushButton(addForm)
        self.delCrossroadButton.setGeometry(QtCore.QRect(550, 80, 111, 21))
        self.delCrossroadButton.setObjectName("delCrossroadButton")
        self.delRoadButton = QtWidgets.QPushButton(addForm)
        self.delRoadButton.setGeometry(QtCore.QRect(550, 50, 111, 21))
        self.delRoadButton.setObjectName("delRoadButton")

        self.retranslateUi(addForm)
        QtCore.QMetaObject.connectSlotsByName(addForm)

    def retranslateUi(self, addForm):
        _translate = QtCore.QCoreApplication.translate
        addForm.setWindowTitle(_translate("addForm", "Добавить данные"))
        self.addRoadButton.setText(_translate("addForm", "Добавить участок"))
        self.addCrossroadButton.setText(_translate("addForm", "Добавить перекрёсток"))
        self.latitudeEdit.setText(_translate("addForm", "50.25958"))
        self.longitudeEdit.setText(_translate("addForm", "127.54389"))
        self.label.setText(_translate("addForm", "Долгота:"))
        self.label_2.setText(_translate("addForm", "Широта:"))
        self.label_3.setText(_translate("addForm", "<html><head/><body><p>Ремонтируемые участки</p></body></html>"))
        self.label_5.setText(_translate("addForm", "Объездные участки"))
        self.label_6.setText(_translate("addForm", "Группы объезда"))
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
        self.delBadButton.setText(_translate("addForm", "Удалить участок"))
        self.delCrossroadButton.setText(_translate("addForm", "Удалить группу"))
        self.delRoadButton.setText(_translate("addForm", "Удалить улицу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addForm = QtWidgets.QWidget()
    ui = Ui_addForm()
    ui.setupUi(addForm)
    addForm.show()
    sys.exit(app.exec_())
