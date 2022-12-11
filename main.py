from PyQt6 import uic, QtWidgets
from main_form import Ui_Dialog
from PyQt6.QtGui import QPixmap
import requests
import json

Form, Window = uic.loadUiType("main_form.ui")

'''class Ui(QtWidgets.QDialog, Form):
        def __init__(self):
                super(Ui, self).__init__()
                self.ui = Ui_Dialog()
                self.ui.setupUi(self)
                self.initUI()

        def buttonPresed(self):
            pass

        def initUI(self):
            self.ui.pushButton.clicked.connect(self.buttonPresed)'''


if __name__ == "__main__":
        link = 'https://routing.api.2gis.com/carrouting/6.0.0/global?key=1967db2b-de7d-46b3-b63a-ab040702a18a'
        with open("data.txt", "r") as read_file:
            data = json.load(read_file)
        with open("headers.txt", "r") as read_file:
            headers = json.load(read_file)
        print(data)
        question = requests.post(link, json=data, headers=headers)
        print(json.loads(question))
