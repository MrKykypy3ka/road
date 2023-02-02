from PyQt5 import uic, QtWidgets, QtCore, QtGui
from forms.main_form import Ui_Dialog
from PyQt5.QtGui import QPixmap

Form, Window = uic.loadUiType("forms/main_form.ui")


class UiM(QtWidgets.QDialog, Form):
    def __init__(self):
        super(UiM, self).__init__()
        self.uim = Ui_Dialog()
        self.uim.setupUi(self)
        self.initUI()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())


    def buttonPresed(self):
        print("ХУЙ")

    def initUI(self):
        self.uim.pushButton.clicked.connect(self.buttonPresed)
