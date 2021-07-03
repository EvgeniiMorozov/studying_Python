import socket

client_socket = socket.socket()
client_socket.connect(("localhost", 5000))

while True:
    data = input("Введите сообщение: ").encode()
    client_socket.send(data)
    data = client_socket.recv(1024)

    if data == b"q":
        break

    print(f"{client_socket.getpeername()} => {data.decode()}")

client_socket.close()
