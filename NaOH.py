import socket
import time

NaOH = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
NaOH.sendto("NaOH".encode(),("localhost",12000))
quantNaOH = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = NaOH.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
while True:
    time.sleep(1)
    NaOH.sendto("NaOH:0.5".encode(),("localhost",12000))