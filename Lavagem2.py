import socket
import time
import random

lavagem2 = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lavagem2.sendto("Lavagem2".encode(),("localhost",12000))
quantlavagem2 = 0
lixo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = lavagem2.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True: 
    respostaBytes , enderecoServidor = lavagem2.recvfrom(2048)
    resposta = respostaBytes.decode()
    if resposta == "Acabou":
        lavagem2.sendto(("FIM:"+str(lixo)).encode(),("localhost",12000))
        break

    quantlavagem2 += float(resposta)*0.975
    lixo += float(resposta)*0.025

    while quantlavagem2 > 1.5:  
        time.sleep(1)    
        lavagem2.sendto(str(1.5).encode(),("localhost",12000))
        quantlavagem2 -= 1.5
        print("Enviado: 1.5 e ainda tem: "+str(quantlavagem2))
        

    if(quantlavagem2 > 0):
        time.sleep(1)
        lavagem2.sendto(str(quantlavagem2).encode(),("localhost",12000))
        print("Foi enviado tudo: "+str(quantlavagem2))        
        quantlavagem2 = 0



