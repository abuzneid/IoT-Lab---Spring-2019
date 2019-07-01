import socket
import numpy as np
import encodings
from cryptography.fernet import Fernet

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def random_data():

    x1 = np.random.randint(0, 55, None)         # Dummy temperature
    y1 = np.random.randint(0, 45, None)         # Dummy humidigy
    my_sensor = "{},{}".format(x1,y1)
    return my_sensor                            # return data seperated by comma


def encryption_data():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    print("KEY : ", key)
    x = random_data()

    cipher_text = cipher_suite.encrypt(b"{}")
    print("CIPHER :  ",cipher_text)

    return cipher_text,cipher_suite




def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    cipher_text, cipher_suite = encryption_data()

                    cipher_suite = cipher_suite.encrypt('utf-8')

                    conn.sendall(cipher_text)

                    conn.sendall(cipher_suite)


                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break


                if not data:
                    break
                else:
                    pass


if __name__ == '__main__':
    while 1:
        my_server()