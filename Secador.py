import socket
import time
import threading

def secagem(resposta):
    time.sleep(5)
    valor = str(float(resposta)*0.95)
    secador.sendto(valor.encode(),("localhost",12000))
    print('')

secador = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
secador.sendto("Secador".encode(),("localhost",12000))
quantOleo = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = secador.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True: 
    respostaBytes , enderecoServidor = secador.recvfrom(2048)
    resposta = respostaBytes.decode()
    threading.Thread(target=secagem(resposta)).start()

    