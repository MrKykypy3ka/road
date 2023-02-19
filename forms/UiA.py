import time

from PyQt5 import uic, QtWidgets, QtCore
from forms.add_Form import Ui_addForm
from PyQt5.QtGui import QPixmap
from API.yandex import get_map

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
        self.uia = Ui_addForm()
        self.uia.setupUi(self)
        self.uia.addBadRoadButton.clicked.connect(self.add_bad_road)
        self.uia.addRoadButton.clicked.connect(self.add_road)
        self.uia.addCrossroadButton.clicked.connect(self.add_crossroad)
        self.uia.addTimeButton.clicked.connect(self.add_time)
        tracker = MouseTracker(self.uia.imageMap)
        tracker.positionChanged.connect(self.on_positionChanged)
        self.center = None
        self.uia.imageMap.clicked.connect(self.map_click)


    def map_click(self):
        self.uia.longitudeBad.setText(f"{round(float(self.uia.longitudeBad.text()) + self.x * self.kx, 6)}")
        self.uia.latitudeBad.setText(f"{round(float(self.uia.latitudeBad.text()) + self.y * self.ky, 6)}")


    def showEvent(self, event):
        #get_map(0, 0)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        delta = QtCore.QPoint(30, 320)
        self.uia.coor.move(pos + delta)
        self.x = -(self.uia.imageMap.width() // 2 - pos.x())
        self.y = self.uia.imageMap.height() // 2 - pos.y()
        self.kx = 0.0000428
        self.ky = 0.000028
        self.uia.coor.adjustSize()
        self.uia.coor.setText(f"{round(float(self.uia.longitudeBad.text()) + self.x * self.kx, 6)}\n"
                              f"{round(float(self.uia.latitudeBad.text()) + self.y * self.ky, 6)}")
        #50.258908, 127.550502

    def load_map(self):
        longitude = float(self.uia.longitudeBad.text())
        latitude = float(self.uia.latitudeBad.text())
        get_map(longitude, latitude)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(f"({self.uia.longitudeBad.text()}, {self.uia.latitudeBad.text()})")
        self.load_map()


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
