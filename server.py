# Servidor
import socket

HOST = "0.0.0.0"
PORT = 2807

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST, PORT)
    s.listen(1)

    # Aguarda jogadores entrarem
    print("[server] aguardando jogador1...")
    conn_1, addr = s.accept
    conn_1.sendall("[server] OK, você é o jogador1".encode)
    conn_1.sendall("")
    print("[server] Aguardando jogador2...")
    conn_2, addr = s.accept

    # Envia uma mensagem aos jogadores
    conn_1.sendall("[server] OK, você é o jogador 1".encode())
    conn_2.sendall("[server] OK, você é o jogador 2".encode())

    conn_1.close()
    conn_2.close()