from PyQt5 import uic, QtWidgets, QtCore
from forms.add_Form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map
import sqlite3

Form, Window = uic.loadUiType("forms/add_form.ui")


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
        self.kx = 0.00002133
        self.ky = 0.0000135

        self.y = None
        self.x = None

        self.center = None
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.uia.addBadRoadButton.clicked.connect(self.add_bad_road)
        self.uia.addRoadButton.clicked.connect(self.add_road)
        self.uia.addCrossroadButton.clicked.connect(self.add_crossroad)
        self.uia.addTimeButton.clicked.connect(self.add_time)
        self.uia.imageMap.clicked.connect(self.map_click)
        self.uia.viewButton.clicked.connect(self.load_map)
        self.uia.saveButton.clicked.connect(self.save)
        tracker = MouseTracker(self.uia.imageMap)
        tracker.positionChanged.connect(self.on_positionChanged)

        self.new_longitude = self.uia.longitudeEdit.text()
        self.new_latitude = self.uia.latitudeEdit.text()

        self.db = sqlite3.connect('load.sqlite')
        self.sql = self.db.cursor()


    def save(self):
        print(1)
        self.save_bad_sections()
        self.save_road()
        self.save_crossroad()
        self.save_time()
        self.save_date()

    def save_bad_sections(self):
        s_id = 1
        print([self.uia.badRoadList.item(i) for i in range(self.uia.badRoadList.count())])
        for elem in self.uia.badRoadList.items():
            # sqlite_insert_query = "INSERT INTO badSections (badSection_id, street, longitude, latitude, count_lane, max_speed) VALUES (?, ?, ?, ?, ?, ?);"
            temp = elem.replace(',', '').replace('(', '').replace(')', '')
            longitude = elem
            print(longitude)
            # latitude =
            # data = (s_id, "", )
            # sql.execute(sqlite_insert_query, data)
            # db.commit()
            # s_id += 1

    def save_road(self):
        pass

    def save_crossroad(self):
        pass

    def save_time(self):
        pass

    def save_date(self):
        pass

    def map_click(self):
        self.x = -(325 - self.pos_x)
        self.y = 225 - self.pos_y

        self.new_longitude = round(float(self.uia.longitudeEdit.text()) + self.x * self.kx, 6)
        self.new_latitude = round(float(self.uia.latitudeEdit.text()) + self.y * self.ky, 6)

        self.uia.longitudeEdit.setText(f"{self.new_longitude}")
        self.uia.latitudeEdit.setText(f"{self.new_latitude}")

        self.center = f"({self.uia.longitudeEdit.text()}, {self.uia.latitudeEdit.text()})"


    def showEvent(self, event):
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        delta = QtCore.QPoint(30, 320)
        self.uia.coor.move(pos + delta)
        self.uia.coor.adjustSize()

        self.pos_x = pos.x()
        self.pos_y = pos.y()

        self.x = -(325 - pos.x())
        self.y = 225 - pos.y()

        self.uia.coor.setText(f"{round(float(self.uia.longitudeEdit.text()) + self.x * self.kx, 6)}\n"
                              f"{round(float(self.uia.latitudeEdit.text()) + self.y * self.ky, 6)}")


    def load_map(self):
        get_map(self.new_longitude, self.new_latitude)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(self.center)
        self.load_map()


    def add_road(self):
        self.uia.roadList.addItem(self.center)
        self.load_map()

    def add_crossroad(self):
        self.uia.crossroadList.addItem(self.center)
        self.load_map()

    def add_time(self):
        self.uia.timeList.addItem(self.uia.timeEdit.time().toString('hh:mm'))
