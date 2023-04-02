from PyQt5 import uic, QtWidgets
from UI.forms.list_form import Ui_listForm
from PyQt5.QtCore import *
from UI.UiA import UiA
import json

Form, Window = uic.loadUiType("UI/forms/list_form.ui")

class UiL(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiL, self).__init__(parent)
        self.uil = Ui_listForm()
        self.uil.setupUi(self)
        self.addForm = None
        self.uil.addGroupButton.clicked.connect(self.new_area)
        self.uil.addTimeButton.clicked.connect(self.save_time)
        self.uil.saveButton.clicked.connect(self.save)
        self.uil.viewGroupButton.clicked.connect(self.edit_area)
        self.uil.delAreaButton.clicked.connect(self.del_area)
        self.uil.delTimeButton.clicked.connect(self.del_time)
        self.count_area = 0
        self.data = {}
        # dateedit.setMinimumDate(QDate(1900, 1, 1))
        # dateedit.setMaximumDate(QDate(2100, 12, 31))

    def save_time(self):
        self.uil.timeList.addItem(self.uil.timeEdit.text())

    def new_area(self):
        if len(self.data) == self.count_area:
            self.count_area += 1
        if not self.count_area == 1:
            with open('data/result/data.json') as file:
                self.data = json.load(file)

        self.data[f"area {self.count_area}"] = {"bad": [], "road": [], "crossroad": []}
        with open('data/result/data.json', "w") as file:
            json.dump(self.data, file, separators=(', ', ': '), indent=4, ensure_ascii=False)

        self.addForm = UiA(self)
        self.addForm.show()

        if not self.addForm.exec_():
            self.uil.groupList.addItem(f"area {self.count_area}")

    def edit_area(self):
        if self.uil.groupList.currentIndex().data() is not None:
            self.addForm = UiA(self)
            self.addForm.showEdit(area=self.uil.groupList.currentIndex().data())

    def del_area(self):
        if self.uil.groupList.currentIndex().data() is not None:
            del self.data[self.uil.groupList.currentIndex().data()]
            self.uil.groupList.clear()
            self.uil.groupList.addItems(self.data)

    def del_time(self):
        if self.uil.timeList.currentIndex().data() is not None:
            temp = list()
            for i in range(self.uil.timeList.count()):
                temp.append(self.uil.timeList.item(i).text())
            temp.remove(self.uil.timeList.currentIndex().data())
            self.uil.timeList.clear()
            self.uil.timeList.addItems(temp)

    def save(self):
        with open('data/result/data.json') as file:
            self.data = json.load(file)
        self.data[f"settings"] = {
            "date": [self.uil.dateEdit.text(), self.uil.dateEdit.text()],
            "time": [self.uil.timeList.item(i).text() for i in range(self.uil.timeList.count())]}
        with open('data/result/data.json', "w") as file:
            json.dump(self.data, file, separators=(', ', ': '), indent=4, ensure_ascii=False)
        self.close()

    def load_data(self, filename):
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
                break
            self.uil.groupList.addItem(key)


