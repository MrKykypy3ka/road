from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc


class HoverButton(QtWidgets.QToolButton):
    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setStyleSheet('''border-image: url("imagen.jpg")''')

    def resizeEvent(self, event):
        self.setMask(QtGui.QRegion(self.rect(), QtGui.QRegion.Ellipse))
        QtWidgets.QToolButton.resizeEvent(self, event)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1210, 650, 61, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = HoverButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 550, 61, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = HoverButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 200, 61, 61))
        self.pushButton_3.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 400, 61, 61))
        self.pushButton_5.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 380, 61, 61))
        self.pushButton_6.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(1020, 70, 61, 61))
        self.pushButton_7.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(1120, 300, 61, 61))
        self.pushButton_8.setStyleSheet("background-image: url(:/icons/point1.png);background-color: rgba(255, 255, 255, 0);border: none;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 260, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 490, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(430, 340, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(790, 420, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(980, 110, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(1080, 340, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 1281, 741))
        self.label_4.setStyleSheet("background-image:url(:/icons/back.jpg);")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Инструмент планирования"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Загрузить</p><p align=\"center\">данные</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Сбор данных</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Анализ</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Проектирование</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Архив</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Визуализация</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
