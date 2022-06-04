import socket
import time
import threading

def secagem(resposta):
    time.sleep(5)
    valor = str(float(resposta)*0.95)
    secadorEtHO.sendto(valor.encode(),("localhost",12000))
    print("Enviando: "+resposta)

secadorEtHO = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
secadorEtHO.sendto("SecadorEtOH".encode(),("localhost",12000))
quantOleo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = secadorEtHO.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True: 
    respostaBytes , enderecoServidor = secadorEtHO.recvfrom(2048)
    resposta = respostaBytes.decode()
    if resposta != "":
        threading.Thread(target=secagem(resposta)).start()
    resposta = ""
    