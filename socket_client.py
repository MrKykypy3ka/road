from dotenv import load_dotenv, find_dotenv
import socket
import pickle
import os
import io

load_dotenv(find_dotenv())
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

def send_file(filepath):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            request = "S_F"
            s.sendall(request.encode())
            response = s.recv(1024).decode()
            if response != "OK":
                return "Ошибка при отправке запроса на сервер."
            s.sendall(os.path.basename(filepath).encode())
            with open(filepath, 'rb') as file:
                data = file.read(1024)
                while data:
                    s.sendall(data)
                    data = file.read(1024)
            return "Файл успешно отправлен."
        except socket.error as e:
            return "Ошибка при отправке файла: " + str(e)

def get_list_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            request = "G_L"
            s.sendall(request.encode())
            data = s.recv(io.DEFAULT_BUFFER_SIZE)
            file_list = pickle.loads(data)
            return file_list
        except socket.error as error:
            return f"Ошибка при получении списка файлов: {error}"

def get_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            request = f"R_F {filename}"
            s.sendall(request.encode())
            with open(f"data/archive/{filename}", 'wb') as f:
                while True:
                    data = s.recv(1024)
                    if not data:
                        break
                    f.write(data)
            return f"Файл успешно получен"
        except socket.error as error:
            return f"Ошибка при получении файла: {error}"
