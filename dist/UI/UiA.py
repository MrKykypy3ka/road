import configparser

from PyQt5 import uic, QtWidgets, QtCore
from UI.forms.add_Form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import *
from PyQt5.QtCore import *
import json


Form, Window = uic.loadUiType("UI/forms/add_form.ui")

class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)


class UiA(QtWidgets.QDialog, Form):
    closed = pyqtSignal(dict)
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.map = 'map,trf'
        self.scale = 2
        self.kx = 0.00002133
        self.ky = 0.0000135
        self.data = {'bad': [], 'k': dict()}
        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()
        self.tracker = MouseTracker(self.uia.imageMap)
        self.edit_name = False
        self.y = None
        self.x = None
        self.pos_x = None
        self.pos_y = None
        self.center = None
        self.area = None
        self.filename = None
        self.initUI()

    def initUI(self):
        self.tracker.positionChanged.connect(self.on_positionChanged)
        self.uia.addBadRoadButton.clicked.connect(self.add_bad_road)
        self.uia.addRoadButton.clicked.connect(self.add_road)
        self.uia.addGroupButton.clicked.connect(self.add_group)
        self.uia.groupList.itemDoubleClicked.connect(self.edit_group)
        self.uia.delBadButton.clicked.connect(self.del_bad_road)
        self.uia.delRoadButton.clicked.connect(self.del_road)
        self.uia.delGroupButton.clicked.connect(self.del_group)
        self.uia.imageMap.clicked.connect(self.map_click)
        self.uia.badRoadList.itemDoubleClicked.connect(self.show_badRoad)
        self.uia.roadList.itemDoubleClicked.connect(self.show_road)
        self.uia.groupEdit.textChanged.connect(self.change_color)
        self.uia.comboBox.currentIndexChanged.connect(self.change_view_map)
        self.uia.saveButton.clicked.connect(self.save)
        self.uia.imageMap.setCursor(QtCore.Qt.CrossCursor)
        self.uia.imageMap.setFocus()
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)

    def change_view_map(self):
        if self.uia.comboBox.currentIndex() == 0:
            self.map = 'map,trf'
            self.scale = 2
        elif self.uia.comboBox.currentIndex() == 1:
            self.map = 'map'
            self.scale = 1
        elif self.uia.comboBox.currentIndex() == 2:
            self.map = 'trf'
            self.scale = 4
        self.load_map()

    def map_click(self):
        self.x = -(325 - self.pos_x)
        self.y = 225 - self.pos_y

        self.new_longitude = round(float(self.uia.longitudeEdit.text()) + self.x * self.kx, 6)
        self.new_latitude = round(float(self.uia.latitudeEdit.text()) + self.y * self.ky, 6)
        self.center = str(self.new_longitude) + " " + str(self.new_latitude)
        self.load_map()

    def change_color(self):
        self.uia.groupEdit.setStyleSheet('QLineEdit { background-color: #FFFFFF; }')

    def showEvent(self, event):
        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.new_longitude, self.new_latitude = get_city(config['DEFAULT']['city'])
        self.load_map()

    def showEdit(self, data):
        self.uia.groupList.clear()
        self.data = data
        self.uia.badRoadList.addItems(self.data['bad'])
        for group in self.data:
            if group != 'bad' and group != 'k':
                self.uia.groupList.addItem(group)
        self.show()

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        delta = QtCore.QPoint(-15, 320)
        self.uia.coor.move(pos + delta)
        self.uia.coor.adjustSize()

        self.pos_x = pos.x()
        self.pos_y = pos.y()

        self.x = -(325 - pos.x())
        self.y = 225 - pos.y()

        self.uia.coor.setText(f"{round(float(self.uia.longitudeEdit.text()) + self.x * self.kx, 6)}\n"
                              f"{round(float(self.uia.latitudeEdit.text()) + self.y * self.ky, 6)}")

    def show_badRoad(self):
        self.new_longitude, self.new_latitude = list(map(float, self.uia.badRoadList.currentIndex().data().split()))
        self.load_map()

    def show_road(self):
        self.new_longitude, self.new_latitude = list(map(float, self.uia.roadList.currentIndex().data().split()))
        self.load_map()

    def edit_group(self):
        self.uia.roadList.clear()
        self.uia.groupEdit.setText(self.uia.groupList.currentItem().text())
        self.uia.roadList.addItems(self.data[self.uia.groupList.currentItem().text()])
        self.uia.koef.setText(str(self.data['k'][self.uia.groupList.currentItem().text()]))
        self.edit_name = True
        self.uia.groupList.setEnabled(False)

    def load_map(self):
        self.uia.longitudeEdit.setText(f"{self.new_longitude}")
        self.uia.latitudeEdit.setText(f"{self.new_latitude}")
        get_map(self.new_longitude, self.new_latitude, self.map, self.scale)
        self.uia.imageMap.setPixmap(QPixmap("data/result/map.png"))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(f"{self.center}")
        self.data['bad'].append(f"{self.center}")
        self.load_map()

    def add_road(self):
        self.uia.roadList.setStyleSheet('QListWidget { background-color: #FFFFFF; }')
        self.uia.roadList.addItem(f"{self.center}")
        self.load_map()

    def add_group(self):
        if self.uia.roadList.count() == 0:
            self.uia.roadList.setStyleSheet('QListWidget { background-color: #FF7E7E; }')
        elif self.uia.groupEdit.text() == "":
            self.uia.groupEdit.setStyleSheet('QLineEdit { background-color: #FF7E7E; }')
        else:
            if self.edit_name:
                item_to_rename = self.uia.groupList.item(self.uia.groupList.currentRow())
                item_to_rename.setText(self.uia.groupEdit.text())
            else:
                self.uia.groupList.addItem(self.uia.groupEdit.text())
            self.data[self.uia.groupEdit.text()] = [self.uia.roadList.item(i).text()
                                                    for i in range(self.uia.roadList.count())]
            self.data['k'][self.uia.groupEdit.text()] = float(self.uia.koef.text())
            self.uia.koef.setText("0.0")
            self.uia.groupEdit.setText("")
            self.edit_name = False
            self.uia.roadList.clear()
            self.uia.groupList.setEnabled(True)

    def del_bad_road(self):
        if self.uia.badRoadList.currentIndex().data() is not None:
            self.uia.badRoadList.takeItem(self.uia.badRoadList.currentRow())

    def del_road(self):
        if self.uia.roadList.currentIndex().data() is not None:
            self.uia.roadList.takeItem(self.uia.roadList.currentRow())

    def del_group(self):
        if self.uia.groupList.currentIndex().data() is not None:
            del self.data[self.uia.groupList.currentItem().text()]
            self.uia.groupList.takeItem(self.uia.groupList.currentRow())

    def save(self):
        self.closed.emit(self.data)
        self.close()
