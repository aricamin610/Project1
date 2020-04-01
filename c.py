from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

thislist = [1,"string", "string", "string", "string", "string"]

def initial_Client_Table():
    print ("Initial Client Server Table........")

    list0 = [ 0,'Name         ]', 'Type ', 'Value           ','TTL  ', 'Static'] 
    print(list0)

q1 = input('Enter the host name/domain name:')
clientSocket.sendto(q1.encode(),(serverName, serverPort))
name, localserverAddress = clientSocket.recvfrom(2048)
print (name.decode())

q2 = input("Enter the type of DNS query 0. A, 1. AAAA, 2. CNAME, 3. NS):")
clientSocket.sendto(q2.encode(), (serverName, serverPort))

type, localserverAddress = clientSocket.recvfrom(2048)
print (type.decode())

clientSocket.close()
#---------------------Client Inital Table------(HAS TO BE EMPTY AT FIRST)------

#----------------End of Inital Table-------------------------

