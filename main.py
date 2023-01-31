import requests
import json
import shutil
from PIL import *


def twoGis():
    link = 'https://routing.api.2gis.com/carrouting/6.0.0/global?key=1967db2b-de7d-46b3-b63a-ab040702a18a'
    headers = json.load(open("headers.json", "r"))
    data = open("data.json", "r").read()

    question = requests.post(url=link, headers=headers, data=data).text
    result = json.loads(question)
    print(result)
def yandex():
    link = f'https://static-maps.yandex.ru/1.x/?ll={127.53559},{50.26585}&size={650},{450}&spn={0.007},{0.007}&l=map,trf' #50.26585 с.ш. 127.53559 в.д.
    question = requests.get(url=link, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(question.raw, out_file)


if __name__ == "__main__":
        yandex()