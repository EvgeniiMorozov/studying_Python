import socket
from select import select

to_monitor = []

server_socket = socket.socket()
server_socket.bind(('localhost', 5000))  # 127.0.0.1:5000
server_socket.listen()


def accept_connection(server_socket):
    print('Перед подключением')
    client_socket, addr = server_socket.accept()
    print(f'Подключился: {addr}')
    to_monitor.append(client_socket)


def send_message(client_socket):
    try:
        print(f'Ждём сообщение от {client_socket.getpeername()}')
        request = client_socket.recv(1024)
        if request is None or request == '' or request == ' ':
            to_monitor.remove(client_socket)
            client_socket.close()
    except socket.error:
        to_monitor.remove(client_socket)
        client_socket.close()
    else:
        print(f'{client_socket.getpeername()} => {request.decode()}')
        client_socket.send(request)


def event_loop():
    to_monitor.append(server_socket)
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


event_loop()
