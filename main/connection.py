import time
import os
import sys

class Connection():
  def __init__(self, host, port):
    self.host = host
    self.port = port

  def connect_with_server(self):
    for i in range(1):
      i += 1
      os.system('clear')

      sys.stdout.write('\033[34m[*~*]\033[0m Waiting for connections \033[34m[*~*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*\*]\033[0m Waiting for connections \033[34m[*\*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*|*]\033[0m Waiting for connections \033[34m[*|*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*/*]\033[0m Waiting for connections \033[34m[*/*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*~*]\033[0m Waiting for connections \033[34m[*~*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*\*]\033[0m Waiting for connections \033[34m[*\*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*|*]\033[0m Waiting for connections \033[34m[*|*]\033')
      sys.stdout.flush()
      time.sleep(0.3)
      os.system('clear')

      sys.stdout.write('\033[34m[*/*]\33[0m Waiting for connections \033[34m[*/*]\33')
      sys.stdout.flush()
      time.sleep(0.3)

    os.system('clear')
    print("\033[34m[INFO]\033[0m New connection from: ")
    time.sleep(2)

    host = '192.168.1.100'
    command = input('\033[0m \033[31m' + host + '\033[35m /\033[0m \033[36mhome\033[0m\033[0m > \033[33m')
    sys.stdout.write(command)

conn = Connection('192.168.1.100', 5555)
conn.connect_with_server()
# sys.stdout.write()
# sys.stdout.flush()
# time.sleep(0.3)
