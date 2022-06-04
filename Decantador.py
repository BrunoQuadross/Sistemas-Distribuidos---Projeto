import socket
import time


Decantador = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Decantador.sendto("Decantador".encode(),("localhost",12000))
quantDecantador = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = Decantador.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

ciclos = 0
print("Começando!")
while True: 
    respostaBytes , enderecoServidor = Decantador.recvfrom(2048)
    resposta = respostaBytes.decode()  
    if  resposta == "Acabou":
        Decantador.sendto(("FIM:"+str(ciclos)).encode(),("localhost",12000))
        break

    quantDecantador += float(resposta)
    print("Tem no momento :",quantDecantador)
    if(quantDecantador == 10):
        print("Decantando!")
        time.sleep(5)
        resposta = str(quantDecantador*0.96)+":"+str(quantDecantador*0.03)+":"+str(quantDecantador*0.01)
        Decantador.sendto(resposta.encode(),("localhost",12000))
        quantDecantador = 0
        ciclos += 1





