from forms.UiM import UiM
from PyQt5 import QtWidgets
import sys
#1967db2b-de7d-46b3-b63a-ab040702a18a
#ruhpjd9444

def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()