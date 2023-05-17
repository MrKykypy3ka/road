from PyQt5.QtWidgets import QFileDialog

from dotenv import load_dotenv, find_dotenv
from UI.forms.main_form import Ui_mainForm
from PyQt5 import QtWidgets, QtCore, uic
from UI.UiL import UiL
import socket
import os


Form, Window = uic.loadUiType("UI/forms/main_form.ui")
load_dotenv(find_dotenv())
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))


def send_data(filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            with open(filename, 'rb') as f:
                file_data = f.read()
                s.sendall(file_data)
    except socket.error as error:
        print(error)


class UiM(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):  # Конструктор класса
        super(UiM, self).__init__(parent)
        self.data = None
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.initUI()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.listForm = None

    def show_list_form(self):  # Метод отображения формы создания конфигурации
        self.listForm = UiL(self)
        self.listForm.show()

    def show_list_edit_form(self):  # Метод отображения формы редактирвоания конфигурации
        filename = self.choice_data('JSON (*.json)')
        self.listForm = UiL(self)
        self.listForm.load_data(filename)

    def show_send_form(self):
        filename = self.choice_data('JSON (*.json)')
        send_data(filename)

    def choice_data(self, typefile):  # Диалоговое окно для выбора файла конфигурации
        filename, ok = QFileDialog.getOpenFileName(self, "Выберете файл конфигурации", "", typefile)
        if filename:
            return filename

    def initUI(self):  # Метод инициализации подписок на событие
        self.uim.pushButton_2.clicked.connect(self.show_list_form)
        self.uim.pushButton_5.clicked.connect(self.show_send_form)
        self.uim.pushButton_3.clicked.connect(self.show_list_edit_form)
