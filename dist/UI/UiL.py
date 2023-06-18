from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
from UI.forms.list_form import Ui_listForm
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from UI.UiA import UiA
import datetime
import json

Form, Window = uic.loadUiType("UI/forms/list_form.ui")

class UiL(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiL, self).__init__(parent)
        self.uil = Ui_listForm()
        self.uil.setupUi(self)
        self.count_area = 0
        self.data = {}
        self.addForm = None
        self.current_area = None
        self.filename = ""
        self.initUI()


    def initUI(self):
        self.uil.addGroupButton.clicked.connect(self.add_area)
        self.uil.addTimeButton.clicked.connect(self.add_time)
        self.uil.saveButton.clicked.connect(self.save)
        self.uil.viewGroupButton.clicked.connect(self.edit_area)
        self.uil.delAreaButton.clicked.connect(self.del_area)
        self.uil.delTimeButton.clicked.connect(self.del_time)
        self.uil.groupList.itemDoubleClicked.connect(self.rename_area)
        y, m, d = map(int, str(datetime.date.today()).split('-'))
        self.uil.dateEdit.setMinimumDate(QDate(y, m, d))
        self.uil.dateEdit.setMaximumDate(QDate(y+100, 12, 31))
        self.uil.dateEdit_2.setMinimumDate(QDate(y, m, d+1))
        self.uil.dateEdit_2.setMaximumDate(QDate(y+100, 12, 31))
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)


    def add_time(self):
        self.uil.timeList.addItem(self.uil.timeEdit.text())

    def rename_area(self):
        text, ok = QInputDialog().getText(self, "Переименовать", "Имя участка:", QLineEdit.Normal, "")
        if ok and text:
            self.data[text] = self.data[self.uil.groupList.currentItem().text()]
            del self.data[self.uil.groupList.currentItem().text()]
            item_to_rename = self.uil.groupList.item(self.uil.groupList.currentRow())
            item_to_rename.setText(text)
        else:
            return

    def add_area(self):
        self.count_area += 1
        self.data[f"area {self.count_area}"] = dict()
        self.uil.groupList.addItem(f"area {self.count_area}")
        addForm = UiA(self)
        addForm.closed.connect(self.closed_addForm)
        self.current_area = f"area {self.count_area}"
        addForm.show()
        addForm.exec_()

    def edit_area(self):
        if self.uil.groupList.currentIndex().data() is not None:
            addForm = UiA(self)
            addForm.closed.connect(self.closed_addForm)
            self.current_area = self.uil.groupList.currentIndex().data()
            addForm.showEdit(self.data[self.current_area])

    def del_area(self):
        if self.uil.groupList.currentIndex().data() is not None:
            del self.data[self.uil.groupList.currentIndex().data()]
            self.uil.groupList.takeItem(self.uil.groupList.currentRow())

    def del_time(self):
        if self.uil.timeList.currentIndex().data() is not None:
            self.uil.timeList.takeItem(self.uil.timeList.currentRow())

    def closed_addForm(self, text):
        self.data[self.current_area] = text

    def load_data(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)
        self.show()
        for key in self.data:
            if key == 'settings':
                d, m, y = map(int, self.data[key]['date'][0].split('.'))
                self.uil.dateEdit.setDate(QDate(y, m, d))
                d, m, y = map(int, self.data[key]['date'][1].split('.'))
                self.uil.dateEdit_2.setDate(QDate(y, m, d))
                for elem in self.data[key]['time']:
                    self.uil.timeList.addItem(elem)
            else:
                self.uil.groupList.addItem(key)

    def save(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('.json')
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter('JSON File (*.json)')
        file_dialog.setWindowTitle('Сохранить конфигурацию')
        file_dialog.setDirectory('data/result/')
        file_dialog.selectFile(self.filename)
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            if file_path:
                with open(file_path, 'w') as json_file:
                    json.dump(self.data, json_file, indent=4)
                self.close()