from PyQt5.QtWidgets import QFileDialog

from UI.forms.main_form import Ui_mainForm
from PyQt5 import QtWidgets, QtCore, uic
from UI.UiL import UiL
import json


Form, Window = uic.loadUiType("UI/forms/main_form.ui")


class UiM(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.data = None
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.initUI()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.listForm = None

    def slow_list_form(self):
        self.listForm = UiL(self)
        self.listForm.show()


    def send_data(self):
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 3030))  # Подключаемся к нашему серверу.
        with open('data/result/data.json') as file:
            self.data = json.load(file)
        s.sendall(self.data)  # Отправляем фразу.
        data = s.recv(1024)  # Получаем данные из сокета.
        s.close()


    def choice_data(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Выберете файл конфигурации",
            "",
            "JSON (*.json)"
        )
        if filename:
            self.listForm = UiL(self)
            self.listForm.load_data(filename)


    def initUI(self):
        self.uim.pushButton_2.clicked.connect(self.slow_list_form)
        self.uim.pushButton_5.clicked.connect(self.send_data)
        self.uim.pushButton_3.clicked.connect(self.choice_data)
