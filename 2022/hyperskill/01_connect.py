import sys
import socket

if __name__ == "__main__":
    if len(sys.argv) == 4:
        my_sock = socket.socket()
        hostname = sys.argv[1]
        port = int(sys.argv[2])
        my_sock.connect((hostname, port))
        password = sys.argv[3]
        my_sock.send(password.encode())
        print(my_sock.recv(1024).decode())
    else:
        print('Wrong arguments!')
