import socket
import time
import random

lavagem1 = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lavagem1.sendto("Lavagem1".encode(),("localhost",12000))
quantlavagem1 = 0
lixo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = lavagem1.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True: 
    respostaBytes , enderecoServidor = lavagem1.recvfrom(2048)
    resposta = respostaBytes.decode()
    if resposta == "Acabou":
        lavagem1.sendto(("FIM:"+str(lixo)).encode(),("localhost",12000))
        break

    quantlavagem1 += float(resposta)*0.975
    lixo += float(resposta)*0.025

    while quantlavagem1 > 1.5: 
        time.sleep(1)     
        lavagem1.sendto(str(1.5).encode(),("localhost",12000))
        quantlavagem1 -= 1.5
        print("Enviado: 1.5 e ainda tem: "+str(quantlavagem1))
        

    if(quantlavagem1 > 0):
        time.sleep(1)
        lavagem1.sendto(str(quantlavagem1).encode(),("localhost",12000))
        print("Foi enviado tudo: "+str(quantlavagem1))        
        quantlavagem1 = 0



