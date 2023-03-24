HOST = 'localhost'
PORT = 5000

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f'Mensagem enviada: {data.decode()}')

def send_messages(sock):
    while True:
        message = input('> ')
        sock.sendall(message.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(s,)).start()
    threading.Thread(target=send_messages, args=(s,)).start()

    while True:
        pass
