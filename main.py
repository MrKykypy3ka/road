import requests
import json
import shutil
from PIL import Image, ImageDraw
from forms.UiM import UiM
from PyQt5 import QtWidgets
import sys
import PIL


def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
