from decorator import Decorator
import socket, time, os, sys

class Server():
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.connections = []
    self.decorate = Decorator().decorate

  def start_server(self):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((self.host, self.port))
    server_socket.listen(5)
    os.system('clear')
    print(
      self.decorate('cyan', '[INFO]'), 'Server started on',
      self.decorate('blue', 'Host:'), self.decorate('purple', self.host),
      self.decorate('blue', 'Port:'), self.decorate('purple', self.port)
      # "\033[35m /\033[0m \033[36mhome\033[0m\033[0m > \033[33m"
    )
    time.sleep(2)
    self.connections_handler(server_socket)

  def connections_handler(self, server_socket):
    self.connection_receiver()

    while True:
      break
      conn, addr = server_socket.accept()
      print('New connection from:', addr)

      data = conn.recv(2048).decode()
      print('Received command:', data)
      conn.send('Command feedback: '.encode())

  def connection_receiver(self):
    for i in range(5):
      i += 1
      os.system('clear')

      sys.stdout.write('\033[34m[*~*]\033[0m Waiting for connections \033[34m[*~*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*\*]\033[0m Waiting for connections \033[34m[*\*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*|*]\033[0m Waiting for connections \033[34m[*|*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*/*]\033[0m Waiting for connections \033[34m[*/*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*~*]\033[0m Waiting for connections \033[34m[*~*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*\*]\033[0m Waiting for connections \033[34m[*\*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*|*]\033[0m Waiting for connections \033[34m[*|*]\033')
      sys.stdout.flush()
      time.sleep(0.2)
      os.system('clear')

      sys.stdout.write('\033[34m[*/*]\33[0m Waiting for connections \033[34m[*/*]\33')
      sys.stdout.flush()
      time.sleep(0.2)

    # os.system('clear')
    # print("\033[34m[INFO]\033[0m New connection from: ")
    # time.sleep(2)

    # host = '192.168.1.100'
    # command = input('\033[0m \033[31m' + host + '\033[35m /\033[0m \033[36mhome\033[0m\033[0m > \033[33m')
    # sys.stdout.write(command)

  def command_handler(self):
    pass
    # command = conn.recv(2048).decode()

    # if data == 'comando':
      #   print('Comando recibido:', data)
      #   conn.send('Retorno de comando'.encode())

      # elif data == 'close':
      #   print('Comando recibido:', data)
      #   conn.send('close_conn'.encode())
      #   # conn.send('Cerrando conexion'.encode())
      #   break

      # elif data == 'help':
      #   print('Comando recibido:', data)
      #   helper = ' \nComandos que puedes usar: \n - [close] Cierra la conexion con el servidor \n - [connect] Carga la conexion con el servidor'
      #   conn.send(helper.encode())

      # elif data == 'connect':
      #   print('Comando recibido:', data)

      # else:
      #   print('No se recibio el comando esperado',)
      #   conn.send('El comando recibido no existe'.encode())

server = Server('192.168.1.100', 5555)
server.start_server()
