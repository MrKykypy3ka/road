from PyQt5 import uic, QtWidgets
from forms.add_form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map

Form, Window = uic.loadUiType("forms/add_form.ui")


class UiA(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.uia.button_ok.clicked.connect(self.draw)

    def draw(self):
        longitude = float(self.uia.longitude_bad.text())
        latitude = float(self.uia.latitude_bad.text())
        get_map(longitude, latitude)
        print(longitude, latitude)
        self.uia.label_11.setPixmap(QPixmap('img.png'))
