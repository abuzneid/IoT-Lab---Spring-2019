import socket
import threading
import time
from cryptography.fernet import Fernet

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):
    x1, y1 = x.split(",")
    return x1,y1


def decrypt_data(cipher_text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    print(plain_text.decode('utf-8'))



def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        my = input("Enter command ")

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(4096).decode('utf-8')
        print(data)
        print(type(data))

        s.close()

if __name__ == "__main__":
    while 1:
        my_client()

