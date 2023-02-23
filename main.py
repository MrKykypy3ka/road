from forms.UiM import UiM
from PyQt5 import QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()