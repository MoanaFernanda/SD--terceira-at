import socket
import threading

HOST = 'localhost'
PORT = 5000
MAX_CLIENTS = 10


clients = []

def broadcast_message(message, sender_conn):
    """Envia a mensagem para todos os clientes conectados, exceto para o remetente"""

    for client in clients:
        if client != sender_conn:
            try:
                client.sendall(message.encode())
            except:
                clients.remove(client)
                print(f'Cliente {client.getpeername()} removido')
    
def handle_client(conn, addr):
    print(f'Novo cliente conectado: {addr}')
    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Mensagem recebida de {addr}: {data.decode()}')
            broadcast_message(data.decode(), conn)

        except:
            clients.remove(conn)
            print(f'Cliente {addr} desconectado')
            break
    
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f'Servidor iniciado em {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

start_server()
