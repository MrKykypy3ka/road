from PyQt5 import uic, QtWidgets
from forms.add_Form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map

Form, Window = uic.loadUiType("forms/add_form.ui")


class UiA(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.uia.addBadRoadButton.clicked.connect(self.add_bad_road)
        self.uia.addRoadButton.clicked.connect(self.add_road)
        self.uia.addCrossroadButton.clicked.connect(self.add_crossroad)
        self.uia.addTimeButton.clicked.connect(self.add_time)

    def showEvent(self, event):
        get_map(0, 0)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    def load_map(self):
        longitude = float(self.uia.longitudeBad.text())
        latitude = float(self.uia.latitudeBad.text())
        get_map(longitude, latitude)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(f"({self.uia.longitudeBad.text()}, {self.uia.latitudeBad.text()})")
        self.load_map()
        self.uia.longitudeBad.setText("")
        self.uia.latitudeBad.setText("")

    def add_road(self):
        self.uia.roadList.addItem(f"({self.uia.longitudeRoad.text()}, {self.uia.latitudeRoad.text()})")
        self.uia.longitudeRoad.setText()
        self.uia.latitudeRoad.setText()

    def add_crossroad(self):
        self.uia.crossroadList.addItem(f"({self.uia.longitudeCrossroad.text()}, {self.uia.latitudeCrossroad.text()})")
        self.uia.longitudeCrossroad.setText()
        self.uia.latitudeCrossroad.setText()

    def add_time(self):
        self.uia.timeList.addItem(self.uia.timeEdit.time().toPyTime())

