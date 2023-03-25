import requests
import shutil
from PIL import Image, ImageDraw

def get_map(longitude, latitude, map_parameters, scale, longitude_spn=0.005, latitude_spn=0.005, w=649, h=449):
    name = 'data/result/map.png'
    link = f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}' \
           f'&size={w},{h}&spn={longitude_spn},{latitude_spn}&l={map_parameters}&scale={scale}'
    question = requests.get(url=link, stream=True)
    with open(name, 'wb') as out_file:
        shutil.copyfileobj(question.raw, out_file)
    draw_dot(name)


def draw_dot(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    draw.line((325, 220, 325, 230), fill=(0, 0, 0), width=1)
    draw.line((320, 225, 330, 225), fill=(0, 0, 0), width=1)
    image.save(name)
