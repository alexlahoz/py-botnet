import socket

host = '192.168.1.100'
port = 9999

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((host, port))

while True:
    mensaje = input(' > ')
    socket_client.send(mensaje.encode())
    datos = socket_client.recv(2048).decode()

    if datos == 'close_conn':
        socket_client.close()
        break

    print('Informacion del servidor:', datos)

socket_client.close()