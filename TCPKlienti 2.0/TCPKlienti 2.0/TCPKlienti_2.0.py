from socket import *
import sys
import time


print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Klienti")
print("-----------------------\n")



puna = True

print("Zgjedh nje opcion :  \n IP \n PORT \n HOST \n KOHA  \n KENO  \n KONVERTO \n KALKULO \n KONSTANTA \n FAKTORIEL \n ZANORE \n PRINTO\n EXCHANGE\n TRANSFERIMI\n KUADRATIK(ax^2+bx+c=0) \n MESATARJAKENO(0-1000) \n PRIMAR (rangu i eperm) \n BRISHTE (viti) \n NXITIMI \n REVERSE \n")
print("-----------------------\n")


#funksioni i cili dergon te dhenat ne server dhe merr nga ai pergjigjien

while puna:
    serverName = "127.0.0.1"
    serverPort = 9000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    inputi=input()
    if (inputi == "exit"):
        puna = False
        break
    clientSocket.send(inputi.encode("ASCII"))
    print (clientSocket.recv(1024).decode("ASCII"))
else:
    print("Programi u mbyll")
    clientSocket.close()
