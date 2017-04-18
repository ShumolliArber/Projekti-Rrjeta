from socket import *
import sys

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Klienti")
print("-----------------------\n")
puna=True

print("Zgjedh nje opcion :  \n IP \n PORT \n HOST \n KOHA  \n KENO  \n KONVERTO \n KALKULO \n KONSTANTA \n FAKTORIEL \n ZANORE \n PRINTO\n EXCHANGE\n TRANSFERIMI\n KUADRATIK(ax^2+bx+c=0) \n MESATARJAKENO(0-1000) \n PRIMAR (rangu i eperm) \n BRISHTE (viti) \n")
print("-----------------------\n")



serverName = "127.0.0.1"
serverPort = 9000
clientSocket = socket(AF_INET,SOCK_DGRAM)
while puna:

    opcioni=input()
    if opcioni=="exit":
        puna=False
        break

    clientSocket.sendto(opcioni.encode('ASCII'),(serverName,serverPort))
    modifiedOpcioni,serverAddress = clientSocket.recvfrom(2048)
    print("From Server: \n",modifiedOpcioni.decode('ASCII'))
else:
    print("Programi u mbyll!")

 