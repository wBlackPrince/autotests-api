import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12345)
client_socket.connect(server_address)

def send_mymessage(message, client_socket):
    client_socket.send(message.encode())

def receive_response(client_socket):
    response = client_socket.recv(1024).decode()
    print(response)



send_mymessage("Привет", client_socket)
# Для второго клиента
# send_mymessage("Как дела ?", client_socket)
receive_response(client_socket)

client_socket.close()

