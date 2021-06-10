import socket

host = '192.168.1.100'
port = 9999

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen(5)

print('[*] Servidor conectado | Esperando conexiones [*]')

#  Recibiendo datos de usuario
while True:
    conn, addr = socket_server.accept()
    print('Nueva conexion desde:', addr)
        
    datos = conn.recv(2048).decode()

    if datos == 'comando':
        print('Comando recibido:', datos)
        conn.send('Retorno de comando'.encode())

    elif datos == 'close':
        print('Comando recibido:', datos)
        conn.send('close_conn'.encode())
        # conn.send('Cerrando conexion'.encode())
        break
    elif datos == 'help':
        print('Comando recibido:', datos)
        helper = ' \nComandos que puedes usar: \n - [close] Cierra la conexion con el servidor \n - [connect] Carga la conexion con el servidor'
        conn.send(helper.encode())
    elif datos == 'connect':
        print('Comando recibido:', datos)
    else:
        print('No se recibio el comando esperado',)
        conn.send('El comando recibido no existe'.encode())
        
# command = input('Type command: ')
# if command == 'close':
#     socket_server.close()
# else:
#     print('Comando erroneo')

