from PyQt5 import uic, QtWidgets, QtCore
from forms.main_form import Ui_mainForm
from forms.UiA import UiA

Form, Window = uic.loadUiType("forms/main_form.ui")


class UiM(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.initUI()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.addForm = UiA(self)

    def button_pressed2(self):
        self.addForm.show()

    def initUI(self):
        self.uim.pushButton_2.clicked.connect(self.button_pressed2)
