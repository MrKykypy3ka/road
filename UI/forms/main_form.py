from PyQt5 import QtCore, QtGui, QtWidgets


class HoverButton(QtWidgets.QToolButton):  # Класс для круглых кнопок
    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setStyleSheet('''border-image: url("imagen.jpg")''')

    def resizeEvent(self, event):
        self.setMask(QtGui.QRegion(self.rect(), QtGui.QRegion.Ellipse))
        QtWidgets.QToolButton.resizeEvent(self, event)


class Ui_mainForm(object):  # Класс главного окна приложения
    def setupUi(self, Dialog):  # Описание всех виджетов находящихся на окне
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1210, 650, 61, 61))
        self.pushButton.setStyleSheet("background-image: url(:/icons/que.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = HoverButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 480, 61, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = HoverButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 170, 61, 61))
        self.pushButton_3.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 350, 61, 61))
        self.pushButton_5.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(1070, 270, 61, 61))
        self.pushButton_7.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_7.setObjectName("pushButton_7")
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 225, 151, 81))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(65, 535, 161, 81))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(525, 405, 151, 81))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(1025, 325, 151, 81))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 1281, 741))
        self.label_4.setStyleSheet("background-image:url(:/icons/b.jpg);")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_7.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):  # Отображение надписей на виджетах
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Инструмент планирования"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\" style=\"line-height:0.7;\">Редактировать</p><p align=\"center\">конфигурацию </p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\" style=\"line-height:0.7;\">Сформировать</p><p align=\"center\">конфигурацию </p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><p align=\"center\" style=\"line-height:0.7;\">Анализ</p><p align=\"center\">данных </p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\" style=\"line-height:0.7;\">Архив</p><p align=\"center\">отчётов </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QDialog()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())