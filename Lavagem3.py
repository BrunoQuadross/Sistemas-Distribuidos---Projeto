import socket
import time
import random

lavagem3 = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lavagem3.sendto("Lavagem3".encode(),("localhost",12000))
quantlavagem3 = 0
lixo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = lavagem3.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True: 
    respostaBytes , enderecoServidor = lavagem3.recvfrom(2048)
    resposta = respostaBytes.decode()
    if resposta == "Acabou":
        lavagem3.sendto(("FIM:"+str(lixo)).encode(),("localhost",12000))
        break

    quantlavagem3 += float(resposta)*0.975
    lixo += float(resposta)*0.025

    while quantlavagem3 > 1.5: 
        time.sleep(1)     
        lavagem3.sendto(str(1.5).encode(),("localhost",12000))
        quantlavagem3 -= 1.5
        print("Enviado: 1.5 e ainda tem: "+str(quantlavagem3))
        

    if(quantlavagem3 > 0):
        time.sleep(1)
        lavagem3.sendto(str(quantlavagem3).encode(),("localhost",12000))
        print("Foi enviado tudo: "+str(quantlavagem3))        
        quantlavagem3 = 0



