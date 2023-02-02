import requests
import json
import shutil
from PIL import *
from forms.UiM import UiM
from PyQt5 import QtWidgets
import sys
#1967db2b-de7d-46b3-b63a-ab040702a18a
#ruhpjd9444

def twoGis():
    link = 'https://routing.api.2gis.com/carrouting/6.0.0/global?key=1967db2b-de7d-46b3-b63a-ab040702a18a'
    headers = json.load(open("data/headers.json", "r"))
    data = open("data/data.json", "r").read()
    question = requests.post(url=link, headers=headers, data=data).text
    result = json.loads(question)
    with open('data/result.json', 'w', encoding='utf-8') as out_file:
        json.dump(result, out_file, separators=(', ', ': '), indent=4, ensure_ascii=False)

def yandex():
    link = f'https://static-maps.yandex.ru/1.x/?ll={127.53559},{50.265}&size={650},{450}&spn={0.024},{0.024}&l=trf' #50.26585 с.ш. 127.53559 в.д.
    question = requests.get(url=link, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(question.raw, out_file)

def get_city():
    link = f'https://catalog.api.2gis.com/3.0/items/geocode?lon={127.53522}&lat={50.26463}&fields=items.adm_div,items.address&type=street&key=ruhpjd9444'
    question = requests.get(url=link).text
    result = json.loads(question)
    with open('data/result.json', 'w', encoding='utf-8') as out_file:
        json.dump(result, out_file, separators=(', ', ': '), indent=4, ensure_ascii=False)


def coor():
    link = f'https://catalog.api.2gis.com/2.0/region/search?q=Благовещенск&fields=items.bounds&key=ruhpjd9444'
    question = requests.get(url=link).text
    result = json.loads(question)
    with open('data/result.json', 'w', encoding='utf-8') as out_file:
        json.dump(result, out_file, separators=(', ', ': '), indent=4, ensure_ascii=False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiM()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()