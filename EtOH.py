import socket
import time
import threading


def escutando():
    global quantEtOH
    while True:
        respostaBytes , enderecoServidor = EtOH.recvfrom(2048)
        resposta = respostaBytes.decode()       
        quantEtOH += float(resposta)
        print("Chego EtOH: ",quantEtOH)


EtOH = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
EtOH.sendto("EtOH".encode(),("localhost",12000))
quantEtOH = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = EtOH.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
threading.Thread(target=escutando).start()
while True:
    quantEtOH += 0.25
    if quantEtOH > 1:
        quantEtOH -= 1
        EtOH.sendto("EtOH:1".encode(),("localhost",12000))
        print("Enviado: 1 e ainda tem: "+str(quantEtOH))
        time.sleep(1)
    if quantEtOH < 1:
        resposta = "EtOH:"+str(quantEtOH)
        EtOH.sendto(resposta.encode(),("localhost",12000))
        print("Foi enviado tudo: "+str(quantEtOH))
        time.sleep(1)
        quantEtOH = 0