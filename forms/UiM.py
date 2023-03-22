from PyQt5 import uic, QtWidgets, QtCore
from UI.main_form import Ui_mainForm
from forms.UiL import UiL

Form, Window = uic.loadUiType("UI/main_form.ui")


class UiM(QtWidgets.QDialog, Form):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.initUI()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.listForm = None

    def button_pressed2(self):
        self.listForm = UiL(self)
        self.listForm.show()

    def initUI(self):
        self.uim.pushButton_2.clicked.connect(self.button_pressed2)
