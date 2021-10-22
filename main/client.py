import socket, time, sys

class Client():
  def __init__(self):
    self.host = '192.168.1.100'
    self.port = 5555

  def connect_with_server(self):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((self.host, self.port))

    sock.setblocking(True) is equivalent to sock.settimeout(None)
    sock.setblocking(False) is equivalent to sock.settimeout(0.0)
    client_socket.setblocking(False)

    while True:
      bot_name = (f'{self.host}').encode('utf-8')
      command = input(f'{bot_name} > ')
      print(command)
      client_socket.send(command)
      data = client_socket.recv(2048).decode()

      if data:
        print(data)
        client_socket.close()

  def send_message(self, client_socket, bot_name):
    while True:
      message = input(f'{bot_name} > ')

      if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{10}}".encode('utf-8')
        client_socket.send(message_header + message)

        while True:
          username_header = client_socket.recv(10)
          if not len(username_header):
            print('Connection closed by the server')
            sys.exit()

          username_length = int(username_header.decode('utf-8').strip())
          username = client_socket.recv(username_length).decode('utf-8')
          message_header = client_socket.recv(10)
          message_length = int(message_header.decode('utf-8').strip())
          message = client_socket.recv(message_length).decode('utf-8')

          print(f'{username} > {message}')

client = Client()
client.connect_with_server()
