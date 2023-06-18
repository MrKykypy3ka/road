import requests
import shutil
from PIL import Image, ImageDraw
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

def get_map(longitude, latitude, map_parameters, scale, longitude_spn=0.005, latitude_spn=0.005, w=649, h=449):
    try:
        name = 'data/result/map.png'
        link = f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}' \
               f'&size={w},{h}&spn={longitude_spn},{latitude_spn}&l={map_parameters}&scale={scale}'
        question = requests.get(url=link, stream=True)
        with open(name, 'wb') as out_file:
            shutil.copyfileobj(question.raw, out_file)
        draw_dot(name)
    except:
        print("Ошибка запроса")


def get_city(city):
    try:
        link = f'https://geocode-maps.yandex.ru/1.x/?apikey={TOKEN}&geocode={city}&format=json'
        response = requests.get(link)
        return response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    except:
        print("Ошибка запроса")


def draw_dot(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    draw.line((325, 217, 325, 233), fill=(0, 0, 0), width=2)
    draw.line((317, 225, 333, 225), fill=(0, 0, 0), width=2)
    image.save(name)