# Echo client program
import socket

HOST = 'localhost'        # The remote host
PORT = 50007              # The same port as used by the server

echo_socket = socket.socket()
echo_socket.connect((HOST,PORT))
message = input('please input message: ')
echo_socket.sendall(bytes(message, 'utf-8'))
data = echo_socket.recv(1024)

print('Received', str(repr(data))[1:])
echo_socket.close()