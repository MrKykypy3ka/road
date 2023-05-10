from PyQt5 import uic, QtWidgets, QtCore
from UI.forms.add_Form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map
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
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.map = 'map,trf'
        self.scale = 2
        self.kx = 0.00002133
        self.ky = 0.0000135

        self.y = None
        self.x = None
        self.pos_x = None
        self.pos_y = None

        self.data = {}

        self.center = None
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.uia.addBadRoadButton.clicked.connect(self.add_bad_road)
        self.uia.addRoadButton.clicked.connect(self.add_road)
        self.uia.addCrossroadButton.clicked.connect(self.add_crossroad)

        self.uia.delBadButton.clicked.connect(self.del_bad_road)
        self.uia.delRoadButton.clicked.connect(self.del_road)
        self.uia.delCrossroadButton.clicked.connect(self.del_crossroad)

        self.uia.imageMap.clicked.connect(self.map_click)

        self.uia.saveButton.clicked.connect(self.save)
        tracker = MouseTracker(self.uia.imageMap)
        tracker.positionChanged.connect(self.on_positionChanged)

        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()

        self.uia.comboBox.currentIndexChanged.connect(self.view)

        self.uia.imageMap.setCursor(QtCore.Qt.CrossCursor)
        self.uia.imageMap.setFocus()

        self.uia.badRoadList.itemDoubleClicked.connect(self.show_badRoad)
        self.uia.roadList.itemDoubleClicked.connect(self.show_road)
        self.uia.crossroadList.itemDoubleClicked.connect(self.show_crossroad)


    def keyPressEvent(self, e):
        self.uia.imageMap.setFocus()
        if e.key() == 87:  # W
            self.new_latitude = str(round(float(self.uia.latitudeEdit.text()) + 0.00005, 6))
        elif e.key() == 65:  # A
            self.new_longitude = str(round(float(self.uia.longitudeEdit.text()) - 0.00005, 6))
        elif e.key() == 83:  # S
            self.new_latitude = str(round(float(self.uia.latitudeEdit.text()) - 0.00005, 6))
        elif e.key() == 68:  # D
            self.new_longitude = str(round(float(self.uia.longitudeEdit.text()) + 0.00005, 6))
        elif e.key() == 16777235:  # ^
            self.new_latitude = str(round(float(self.uia.latitudeEdit.text()) + 0.005, 6))
        elif e.key() == 16777236:  # ->
            self.new_longitude = str(round(float(self.uia.longitudeEdit.text()) + 0.005, 6))
        elif e.key() == 16777237:  # v
            self.new_latitude = str(round(float(self.uia.latitudeEdit.text()) - 0.005, 6))
        elif e.key() == 16777234:  # <-
            self.new_longitude = str(round(float(self.uia.longitudeEdit.text()) - 0.005, 6))
        self.load_map()

    def view(self):
        if self.uia.comboBox.currentIndex() == 0:
            self.map = 'map,trf'
            self.scale = 2
        elif self.uia.comboBox.currentIndex() == 1:
            self.map = 'map'
            self.scale = 1
        elif self.uia.comboBox.currentIndex() == 2:
            self.map = 'trf'
            self.scale = 4
        # self.kx = 0.00002133 / self.scale
        # self.ky = 0.0000135 / self.scale
        self.load_map()

    def map_click(self):
        self.x = -(325 - self.pos_x)
        self.y = 225 - self.pos_y

        self.new_longitude = round(float(self.uia.longitudeEdit.text()) + self.x * self.kx, 6)
        self.new_latitude = round(float(self.uia.latitudeEdit.text()) + self.y * self.ky, 6)

        self.center = self.uia.longitudeEdit.text() + " " + self.uia.latitudeEdit.text()
        self.load_map()

    def showEvent(self, event):
        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()
        with open('data/result/data.json', 'r') as file:
            self.data = json.load(file)
        self.load_map()

    def showEdit(self, area=None):
        self.show()
        with open("data/result/data.json") as file:
            temp = json.load(file)
            self.data = temp[area]
        self.uia.badRoadList.addItems(self.data['bad'])
        self.uia.roadList.addItems(self.data['road'])
        self.uia.crossroadList.addItems(self.data['crossroad'])

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

    def show_crossroad(self):
        self.new_longitude, self.new_latitude = list(map(float, self.uia.crossroadList.currentIndex().data().split()))
        self.load_map()

    def load_map(self):
        self.uia.longitudeEdit.setText(f"{self.new_longitude}")
        self.uia.latitudeEdit.setText(f"{self.new_latitude}")

        get_map(self.new_longitude, self.new_latitude, self.map, self.scale)
        self.uia.imageMap.setPixmap(QPixmap("data/result/map.png"))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(f"{self.center}")
        self.data[f"area {len(self.data)}"]["bad"].append(self.center)
        self.load_map()

    def add_road(self):
        self.uia.roadList.addItem(f"{self.center}")
        self.data[f"area {len(self.data)}"]["road"].append(self.center)
        self.load_map()

    def add_crossroad(self):
        self.uia.crossroadList.addItem(f"{self.center}")
        self.data[f"area {len(self.data)}"]["crossroad"].append(self.center)
        self.load_map()

    def del_bad_road(self):
        if self.uia.badRoadList.currentIndex().data() is not None:
            temp = list()
            for i in range(self.uia.badRoadList.count()):
                temp.append(self.uia.badRoadList.item(i).text())
            temp.remove(self.uia.badRoadList.currentIndex().data())
            self.uia.badRoadList.clear()
            self.uia.badRoadList.addItems(temp)

    def del_road(self):
        if self.uia.roadList.currentIndex().data() is not None:
            temp = list()
            for i in range(self.uia.roadList.count()):
                temp.append(self.uia.roadList.item(i).text())
            temp.remove(self.uia.roadList.currentIndex().data())
            self.uia.roadList.clear()
            self.uia.roadList.addItems(temp)

    def del_crossroad(self):
        if self.uia.crossroadList.currentIndex().data() is not None:
            temp = list()
            for i in range(self.uia.crossroadList.count()):
                temp.append(self.uia.crossroadList.item(i).text())
            temp.remove(self.uia.crossroadList.currentIndex().data())
            self.uia.crossroadList.clear()
            self.uia.crossroadList.addItems(temp)

    def save(self):
        with open('data/result/data.json', 'w', encoding='utf-8') as out_file:
            json.dump(self.data, out_file, separators=(', ', ': '), indent=4, ensure_ascii=False)
        self.close()
