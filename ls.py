from socket import *
import time
import pickle

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
#---------------------Local Server Inital Table------------
def initial_LocalServer_Table():
    print ("Initial Local Server Table........")
    list0 = [ 0,'Name         ]', 'Type ', 'Value           ','TTL___', 'Static']
    list1 = [ 1,'www.csusm.edu ', 'A    ', '144.37.5.45     ',"______      ", 1 ]
    list2 = [ 2,'cc.csusm.edu  ', 'A    ', '144.37.5.117    ',"______      ", 1 ]
    list3 = [ 3,'cc1.csusm.edu ', 'CNAME', 'cc.csusm.edu    ',"______      ", 1 ]
    list4 = [ 4,'cc1.csusm.edu ', 'A    ', '144.37.5.118    ',"______      ", 1 ]
    list5 = [ 5,'my.csusm.edu  ', 'A    ', '144.37.5.150    ',"______      ", 1 ]
    list6 = [ 6,'qualcomm.com  ', 'NS   ', 'dns.qualcomm.com',"______      ", 1 ]
    list7 = [ 7,'viasat.com    ', 'NS   ', 'dns.viasat.com  ',"______      ", 1 ]
    print(list0)
    print(list1)
    print(list2)
    print(list3)      
    print(list4)
    print(list5)
    print(list6)
    print(list7)
#----------------End of Inital Table-------------------------
a = [1,"", "", "", "", ""]

num=8

while 1:#------while connection is established
    q1, clientAddress = serverSocket.recvfrom(2048)
    name = q1.decode()
    a[1] = name
        
#    if name == "www.csusm.edu":

#    a[1] = "www.csusm.edu"

    serverSocket.sendto(name.encode(), clientAddress)

    q2, clientAddress = serverSocket.recvfrom(2048)
    type = q2.decode()

    if type == "0":
      a[2] = "A"
    
    if type == "1":
      a[2] = "AAAA"
    
    if type == "2":
      a[2] = "CNAME"
    
    if type == "3":
      a[2] = "NS"
  
    num+=1
    MESSAGE = pickle.dumps(a)
    serverSocket.sendto(MESSAGE.encode(),clientAddress)
#    serverSocket.sendto(type.encode(), clientAddress)
    initial_LocalServer_Table()
    print(a)
    
    


