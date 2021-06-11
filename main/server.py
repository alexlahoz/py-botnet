import socket

class Server():
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.connections = []

  def start_server(self):
    print('Host:', self.host, 'Port:', self.port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((self.host, self.port))
    server_socket.listen(5)
    self.connection_handler(server_socket)

  def connection_handler(self, server_socket):
    while True:
      conn, addr = server_socket.accept()
      print('New connection from:', addr)

      data = conn.recv(2048).decode()
      counter = 0
      while counter == 1:
        if data == 'comando':
          print('Comando recibido:', data)
          conn.send('Retorno de comando'.encode())
          counter += 1

        elif data == 'close':
          print('Comando recibido:', data)
          conn.send('close_conn'.encode())
          # conn.send('Cerrando conexion'.encode())
          break

        elif data == 'help':
          print('Comando recibido:', data)
          helper = ' \nComandos que puedes usar: \n - [close] Cierra la conexion con el servidor \n - [connect] Carga la conexion con el servidor'
          conn.send(helper.encode())
          counter += 1

        elif data == 'connect':
          print('Comando recibido:', data)
          counter += 1

        else:
          print('No se recibio el comando esperado',)
          conn.send('El comando recibido no existe'.encode())
          counter += 1
      break

  def test(self):
    conn = Connection(self.host, self.port)
    conn.connect_with_server()

  def connections(self):
    pass

  def commands(self):
    # command = conn.recv(2048).decode()
    pass

server = Server('192.168.1.100', 5555)
server.start_server()

