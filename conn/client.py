import socket

host = '192.168.1.100'
port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
  message = input(' > ')
  client_socket.send(message.encode())
  data = client_socket.recv(2048).decode()

  if data == 'close_conn':
    client_socket.close()
    break

  print('Server info:', data)

client_socket.close()
