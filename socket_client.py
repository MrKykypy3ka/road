import socket

HOST = '192.168.50.69'  # Локальный IP-адрес
PORT = 7000             # Порт

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Открываем файл
    with open('data/result/data.json', 'rb') as f:
        # Читаем содержимое файла
        file_data = f.read()
        # Отправляем файл на сервер
        s.sendall(file_data)