
# Runs on Pc, directly from Thonny
# The client

import socket
s = socket.socket()
host = '192.168.10.33'# ip of raspberry pi, running the server
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()
