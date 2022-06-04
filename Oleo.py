import socket
import time
import random
import threading

def escutando():
    global quantOleo
    while True: 
        x = random.uniform(0,10)
        time.sleep(x)
        quantOleo += random.uniform(1,2)



oleo = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
oleo.sendto("Oleo".encode(),("localhost",12000))
quantOleo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = oleo.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")

threading.Thread(target=escutando).start()
while True:     
    if quantOleo > 0.75:
        quantOleo -= 0.75
        oleo.sendto("oleo:0.75".encode(),("localhost",12000))
        print("Enviado: 0.75 e ainda tem: "+str(quantOleo))
        time.sleep(1)
    if quantOleo > 0 and quantOleo < 0.75:
        resposta = "oleo:"+str(quantOleo)
        oleo.sendto(resposta.encode(),("localhost",12000))
        print("Foi enviado tudo: "+str(quantOleo))
        time.sleep(1)
        quantOleo = 0






