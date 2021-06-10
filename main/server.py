import socket
from connection_load import Connection


class Server():
  def __init__(self, host, port):
    self.host = host
    self.port = port

  def start_server(self):
    print('Host:', self.host, 'Port:', self.port)
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((self.host, self.port))
    socket_server.listen(5)

  def test(self):
    conn = Connection(self.host, self.port)
    conn.connect_with_server()

  def connections(self):
    pass

  def commands(self):
    # command = conn.recv(2048).decode()
    pass

server = Server('192.168.1.129', 5555)
# server.start_server()
server.test()
