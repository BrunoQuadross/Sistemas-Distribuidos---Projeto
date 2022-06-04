import socket
import time
import threading

def escutando():
    global quantOleo 
    global quantNaOH 
    global quantEtOH
    global decantador 
    global cont
    while True:
        respostaBytes , enderecoServidor = reator.recvfrom(2048)
        resposta = respostaBytes.decode()

        if resposta.split(":")[0] == "oleo":
            quantOleo += float(resposta.split(":")[1])
            print("Chego Oleo !" )

        if resposta.split(":")[0] == "NaOH":
            quantNaOH += float(resposta.split(":")[1])
            print("Chego NaOH!")
            
        if resposta.split(":")[0] == "EtOH":
            quantEtOH += float(resposta.split(":")[1])
            print("Chego EtOH!")
        if resposta == "cheio":
            print("TO CHEIO")
            decantador = False
        if resposta == "vazio":
            print("ESVAZIOU")
            decantador = True
        if resposta == "Acabou":
            print("Acabou!")
            decantador = False
            fim = "FIM:"+str(quantOleo)+":"+str(quantNaOH)+":"+str(quantEtOH)+":"+str(cont)
            reator.sendto(fim.encode(),("localhost",12000))



reator = server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
reator.sendto("Reator".encode(),("localhost",12000))

decantador = True
quantOleo = 0
quantNaOH = 0
quantEtOH = 0
quantTotal = 0
cont = 0
print("Esperando...")

while True:
    respostaBytes , enderecoServidor = reator.recvfrom(2048)
    if respostaBytes.decode() ==  "start":
        break

print("Começando!")
threading.Thread(target=escutando).start()
while True:
    if(quantOleo >= 2 and quantNaOH >= 1 and  quantEtOH >= 1):
        quantTotal += 5
        print("Estamos processando: ",quantTotal)
        quantOleo -= 2
        quantNaOH -= 1
        quantEtOH -= 1
        time.sleep(1)
        for i in range(5):  
            print("Quantidade: ",quantTotal)
            if(decantador):          
                reator.sendto("1".encode(),("localhost",12000))
                time.sleep(1)
                quantTotal -=1
                if i == 4:
                    cont +=1
            else:
                quantOleo += 0.4
                quantNaOH += 0.20
                quantEtOH += 0.20


