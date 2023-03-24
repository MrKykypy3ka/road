from PyQt5 import uic, QtWidgets
from UI.list_form import Ui_listForm
from forms.UiA import UiA
import json

Form, Window = uic.loadUiType("UI/list_form.ui")

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
        self.count_area = 0
        self.data = {}

    def save_time(self):
        self.uil.timeList.addItem(self.uil.timeEdit.text())


    def new_area(self):
        if len(self.data) == self.count_area:
            self.count_area += 1
        if not self.count_area == 1:
            with open('data/data.json') as file:
                self.data = json.load(file)

        self.data[f"area {self.count_area}"] = {"bad": [], "road": [], "crossroad": []}
        with open('data/data.json', "w") as file:
            json.dump(self.data, file, separators=(', ', ': '), indent=4, ensure_ascii=False)

        self.addForm = UiA(self)
        self.addForm.show()

        if not self.addForm.exec_():
            self.uil.groupList.addItem(f"area {self.count_area}")

    def edit_area(self):
        if self.uil.groupList.currentIndex().data() is not None:
            self.addForm = UiA(self)
            self.addForm.showEdit(area=self.uil.groupList.currentIndex().data())

    def save(self):
        print([self.uil.dateEdit.text(), self.uil.dateEdit.text()])
        print([self.uil.timeList.item(i).text() for i in range(self.uil.timeList.count())])
        self.data[f"settings"] = {
            "date": [self.uil.dateEdit.text(), self.uil.dateEdit.text()],
            "time": [self.uil.timeList.item(i).text() for i in range(self.uil.timeList.count())]}
        with open('data/data.json', "w") as file:
            json.dump(self.data, file, separators=(', ', ': '), indent=4, ensure_ascii=False)
        self.close()
