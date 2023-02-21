import requests
import shutil
from PIL import Image, ImageDraw
#1967db2b-de7d-46b3-b63a-ab040702a18a
#ruhpjd9444
#trf

def get_map(longitude, latitude):
    name = 'data\map.png'
    link = f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&size={649},{449}&spn={0.005},{0.005}&l=map'
    question = requests.get(url=link, stream=True)
    with open(name, 'wb') as out_file:
        shutil.copyfileobj(question.raw, out_file)
    draw_dot(name)


def draw_dot(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    draw.line((325, 225, 325, 225), fill='red', width=1)
    image.save(name, quality=100)
