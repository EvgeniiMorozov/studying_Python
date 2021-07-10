import socket
from select import select

tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket()
    server_socket.bind(("localhost", 5000))  # 127.0.0.1:5000
    server_socket.listen()

    while True:
        yield "read", server_socket
        client_socket, addr = server_socket.accept()  # read, потому что ждём подключения
        print(f"Подключился: {addr}")
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield "read", client_socket
        try:
            print(f"Ждём сообщение от {client_socket.getpeername()}")
            request = client_socket.recv(1024)  # read, потому что ждём сообщения
            # if request is None or request == "" or request == " ":
            #     tasks.remove(client_socket)
            #     client_socket.close()
        except socket.error:
            # tasks.remove(client_socket)
            # client_socket.close()
            break
        else:
            yield "write", client_socket
            print(f"{client_socket.getpeername()} => {request.decode()}")
            client_socket.send(request)  # write, потому что отправляем сообщение


# def send_message(client_socket):
#     try:
#         print(f"Ждём сообщение от {client_socket.getpeername()}")
#         request = client_socket.recv(1024)
#         if request is None or request == "" or request == " ":
#             to_monitor.remove(client_socket)
#             client_socket.close()
#     except socket.error:
#         to_monitor.remove(client_socket)
#         client_socket.close()
#     else:
#         print(f"{client_socket.getpeername()} => {request.decode()}")
#         client_socket.send(request)


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            action, sock = next(tasks)

            if action == "read":
                to_read[sock] = task
            elif action == "write":
                to_write[sock] = task
        except StopIteration:
            print("Всё готово!")


tasks.append(server())
event_loop()
