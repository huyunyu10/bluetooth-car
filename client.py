import bluetooth #bluetooth library
bd_addr = "B8:27:EB:8D:78:2B" # here need to modify. use hciconfig to get address
port = 1 #set port number
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) #launch a Socket
sock.connect((bd_addr, port)) #connect bluetooth with address and port number
sock.send("hello!!") #sent hello string to socket
sock.close() #close socket

