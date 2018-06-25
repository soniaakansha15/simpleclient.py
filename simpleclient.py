# client.py file
#!/usr/bin/python

# import socket module
import socket

#create socket object
s=socket.socket()

# get local machine name
host=socket.gethostname()

# reserve a port for ur service
port=1234

s.connect((host,port))
print s.recv(10242)
s.close
