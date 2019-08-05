# Echo server program
import socket
import os
import sys
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

echo_socket = socket.socket()
echo_socket.bind((HOST,PORT))
echo_socket.listen(1)


for i in range(3):
    pid = os.fork()
    if pid == 0:
        childpid = os.getpid()
        print("Child {} listening on localhost:4242".format(childpid))

        try:
            connection,address = echo_socket.accept()
            if connection:
                print('Connected by', address)
                while True:
                    data = connection.recv(1024)
                    if not data: 
                        break
                    connection.sendall(data)

        except KeyboardInterrupt:
            echo_socket.close()
            sys.exit()

try:
    os.waitpid(-1, 0)
except ChildProcessError:
    print("no more children")
    echo_socket.close()
    sys.exit()
except KeyboardInterrupt:
    print("\nbailing")
    echo_socket.close()
    sys.exit()
    
echo_socket.close()
sys.exit()