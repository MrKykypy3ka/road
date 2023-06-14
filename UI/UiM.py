from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, \
    QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal
from dotenv import load_dotenv, find_dotenv
from UI.forms.main_form import Ui_mainForm
from PyQt5 import QtWidgets, uic
from UI.UiL import UiL
from PyQt5.QtGui import QIcon
from socket_client import *
import os
import configparser

load_dotenv(find_dotenv())
CITY = os.getenv('CITY')
Form, Window = uic.loadUiType("UI/forms/main_form.ui")

class UiC(QtWidgets.QDialog):
    item_selected = pyqtSignal(str)
    def __init__(self, filelist, parent=None):
        super(UiC, self).__init__(parent)
        self.filelist = filelist
        self.setWindowTitle("Пример окна PyQt")
        self.setup_ui()
        self.initUI()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.addItems(self.filelist)
        layout.addWidget(self.list_widget)
        self.button = QPushButton("Получить файл")
        layout.addWidget(self.button)
        self.setLayout(layout)

    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
        self.setFixedSize(300, 450)
        self.setWindowIcon(QIcon("data/images/ico.ico"))
        self.button.clicked.connect(self.return_filename)

    def return_filename(self):
        selected_item = self.list_widget.currentItem()
        if selected_item is not None:
            self.item_selected.emit(selected_item.text())
            self.close()


class UiM(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):  # Конструктор класса
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.uil = None
        self.uic = None
        self.initUI()

    def show_list_form(self):  # Метод отображения формы создания конфигурации
        self.uil = UiL(self)
        self.uil.show()

    def show_list_edit_form(self):  # Метод отображения формы редактирования конфигурации
        try:
            filename = self.choice_data('JSON (*.json)')
            self.listForm = UiL(self)
            self.listForm.load_data(filename)
        except:
            pass

    def show_send_form(self):
        filename = self.choice_data('JSON (*.json)')
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Отправка файл на сервер")
        msg_box.setText(send_file(filename))
        msg_box.exec_()

    def choice_data(self, typefile):  # Диалоговое окно для выбора файла конфигурации
        filename, ok = QFileDialog.getOpenFileName(self, "Выберете файл конфигурации", "", typefile)
        return filename

    def initUI(self):  # Метод инициализации подписок на событие
        self.uim.addConfigButton.clicked.connect(self.show_list_form)
        self.uim.analyseButton.clicked.connect(self.show_send_form)
        self.uim.editConfigButton.clicked.connect(self.show_list_edit_form)
        self.uim.archiveButton.clicked.connect(self.open_archive)
        self.uim.infoButton.clicked.connect(self.show_user_guide)
        self.uim.settingsButton.clicked.connect(self.show_settings)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("data/images/ico.ico"))

    def show_settings(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        city = config['DEFAULT']['CITY']
        text, ok = QInputDialog().getText(self, "Выбор города", "Название:", QLineEdit.Normal, city, Qt.WindowCloseButtonHint)
        if ok and text:
            config = configparser.ConfigParser()
            config['DEFAULT'] = {'CITY': text}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)

    def open_archive(self):
        uic = UiC(get_list_data())
        uic.item_selected.connect(self.save_file)
        uic.exec_()

    def save_file(self, filename):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Получение файла")
        msg_box.setText(get_file(filename))
        msg_box.exec_()

    def show_user_guide(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Отправка файл на сервер")
        msg_box.setText("Руководство пользователя")
        msg_box.exec_()
