from UI.UiM import UiM
from PyQt5 import QtWidgets
import sys

"""Функция инициализации объекта приложения,
 создания объекта главного окна, его отображения
 и ожидание выхода из программы"""
def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


#  Точка входа в программу
if __name__ == "__main__":
    main()
