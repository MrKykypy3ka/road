from dotenv import load_dotenv, find_dotenv
import socket
import os

load_dotenv(find_dotenv())
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Открываем файл
    with open('data/result/data.json', 'rb') as f:
        # Читаем содержимое файла
        file_data = f.read()
        # Отправляем файл на сервер
        s.sendall(file_data)