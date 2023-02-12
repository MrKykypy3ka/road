from PyQt5 import QtCore, QtGui, QtWidgets


class AnalyserForm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    uia = Ui_Dialog()
    uia.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())