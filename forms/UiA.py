import json

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from UI.add_form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map
import sqlite3
import json

Form, Window = uic.loadUiType("UI/add_form.ui")

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
        self.scale = 1.3
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
        self.uia.imageMap.clicked.connect(self.map_click)

        self.uia.saveButton.clicked.connect(self.save)
        tracker = MouseTracker(self.uia.imageMap)
        tracker.positionChanged.connect(self.on_positionChanged)

        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()

        self.db = sqlite3.connect('db/load.db')
        self.sql = self.db.cursor()

        self.uia.comboBox.currentIndexChanged.connect(self.view)

        self.uia.imageMap.setCursor(QtCore.Qt.CrossCursor)
        self.uia.imageMap.setFocus()


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
            self.scale = 1.3
        elif self.uia.comboBox.currentIndex() == 1:
            self.map = 'map'
            self.scale = 1
        elif self.uia.comboBox.currentIndex() == 2:
            self.map = 'trf'
            self.scale = 1.3
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
        with open('data/data.json', 'r') as file:
            self.data = json.load(file)
        self.load_map()

    def showEdit(self, area=None):
        self.show()
        with open("data/data.json") as file:
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

    def load_map(self):
        self.uia.longitudeEdit.setText(f"{self.new_longitude}")
        self.uia.latitudeEdit.setText(f"{self.new_latitude}")

        get_map(self.new_longitude, self.new_latitude, self.map, self.scale)
        self.uia.imageMap.setPixmap(QPixmap("data/map.png"))

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

    def save(self):
        # self.save_bad_sections()
        # self.save_road()
        # self.save_crossroad()
        # self.save_time()
        # self.save_date()
        with open('data/data.json', 'w', encoding='utf-8') as out_file:
            json.dump(self.data, out_file, separators=(', ', ': '), indent=4, ensure_ascii=False)
        self.close()

    def save_bad_sections(self):
        try:
            badSection_id = 1
            for elem in [self.uia.badRoadList.item(i).text() for i in range(self.uia.badRoadList.count())]:
                temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
                longitude = temp[0]
                latitude = temp[1]

                sqlite_insert_query = """INSERT INTO badSections (badSection_id, street,
                 longitude, latitude, count_lane, max_speed) VALUES (?, ?, ?, ?, ?, ?);"""
                data = (badSection_id, "", longitude, latitude, 0, 0)
                self.sql.execute(sqlite_insert_query, data)
                self.db.commit()
                badSection_id += 1
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            print("Данные успешно загружены!")

    def save_road(self):
        try:
            road_id = 1
            for elem in [self.uia.roadList.item(i).text() for i in range(self.uia.roadList.count())]:
                temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
                longitude = temp[0]
                latitude = temp[1]

                sqlite_insert_query = """INSERT INTO roads (road_id, street,
                 longitude, latitude, count_lanes, max_speed) VALUES (?, ?, ?, ?, ?, ?);"""
                data = (road_id, "", longitude, latitude, 0, 0)
                self.sql.execute(sqlite_insert_query, data)
                self.db.commit()
                road_id += 1
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            print("Данные успешно загружены!")

    def save_crossroad(self):
        try:
            crossroad_id = 1
            for elem in [self.uia.crossroadList.item(i).text() for i in range(self.uia.crossroadList.count())]:
                temp = elem.replace(',', '').replace('(', '').replace(')', '').split()
                longitude = temp[0]
                latitude = temp[1]
                sqlite_insert_query = """INSERT INTO crossroads (crossroad_id, street,
                 longitude, latitude, trafficLights) VALUES (?, ?, ?, ?, ?);"""
                data = (crossroad_id, "", longitude, latitude, 0)
                self.sql.execute(sqlite_insert_query, data)
                self.db.commit()
                crossroad_id += 1
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            print("Данные успешно загружены!")
