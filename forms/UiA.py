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

    def showEvent(self, event):
        #get_map(0, 0)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        delta = QtCore.QPoint(30, 320)
        self.uia.coor.move(pos + delta)
        #print("(%d, %d)" % (pos.x(), pos.y()))
        self.uia.coor.adjustSize()
        self.uia.coor.setText(f"{pos.x() * (float(self.uia.longitudeBad.text()) / self.uia.imageMap.width())}\n{pos.y() * (float(self.uia.latitudeBad.text()) / self.uia.imageMap.height())}")

    def load_map(self):
        # (0, 0) (50.262629, 127.537114)
        # (649, 0) (50.262681, 127.550838)
        # (0, 449) (50.256489, 127.536930)
        # (649, 449) (50.256483, 127.550860)
        # (325, 225) (50.25958, 127.54389)
        # longitudu - Долгота
        # latitude - широта
        longitude = float(self.uia.longitudeBad.text())
        latitude = float(self.uia.latitudeBad.text())
        get_map(longitude, latitude)
        self.uia.imageMap.setPixmap(QPixmap('data\map.png'))

    def add_bad_road(self):
        self.uia.badRoadList.addItem(f"({self.uia.longitudeBad.text()}, {self.uia.latitudeBad.text()})")
        self.load_map()
        # self.uia.longitudeBad.setText("")
        # self.uia.latitudeBad.setText("")
        print(f"y - долгота: {self.uia.latitudeBad.text()}")
        print(f"х - широта: {self.uia.longitudeBad.text()}")
        print(f"k1 - долгота(н): {float(self.uia.longitudeBad.text()) / self.uia.imageMap.width()}")
        print(f"k1 - широта(н): {float(self.uia.latitudeBad.text()) / self.uia.imageMap.height()}")

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
