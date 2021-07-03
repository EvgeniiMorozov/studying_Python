import socket


server_socket = socket.socket()
server_socket.bind(("localhost", 5000))  # 127.0.0.1
server_socket.listen()

while True:
    print("Перед подключением")
    client_socket, addr = server_socket.accept()
    print("Подключился: {addr}")
    while True:
        try:
            print("Ждём сообщение от {addr}")
            request = client_socket.recv(1024)
            if request is None or request == "" or request == " ":
                client_socket.close()
                break
        except socket.error:
            client_socket.close()
            break
        else:
            print(f"{addr} => {request.decode()}")
            client_socket.send(request)
