import socket

serverIP='172.17.29.11'
serverPORT =6000

serveraddress=(serverIP,serverPORT)
bufferSize = 1024
Socket= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message='Hi my name is Arpita Tomar and my ID is 2022B4PS0596P'

bytestosend= str.encode(message)

Socket.sendto(bytestosend,serveraddress)
