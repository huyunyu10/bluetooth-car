import bluetooth #bluetooth library
import time
import subprocess

server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM ) #launch a Socket
port = 1 #set port number
server_sock.bind(("",port))
server_sock.listen(1) #start listen
client_sock,address = server_sock.accept() #server socket accept connection request
subprocess.call("python3 test.py", shell=True)

