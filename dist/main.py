from PyQt5 import QtWidgets
from UI.UiM import UiM
import sys
import image_rc

def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
