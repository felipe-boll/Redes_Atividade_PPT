# Cliente
import socket

HOST = "127.0.0.1"
PORT = "2807"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor e recebe mensagem
    s.connect(HOST, PORT)

    # Recebe mensagem do servidor
    msg = s.recv(1024).decode()
    print(msg)