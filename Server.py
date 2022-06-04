import socket
import time
import matplotlib.pyplot as plt

def verificaResposta(resposta):
    if resposta.split(":")[0] == "FIM":
        return True
    return False


server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('',12000))
todosOn = 0
print("Esperando...")

while True:
    mensageBytes , enderecoCliente = server.recvfrom(2048)
    resposta = mensageBytes.decode()

    if resposta == "EtOH":
       print("EtOH entrou!")
       enderecoClienteEtOH = enderecoCliente
       todosOn +=1
       print("Faltam :",10-todosOn)

    if resposta == "NaOH":
        print("NaOH entrou!")
        enderecoClienteNaOH = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Oleo":
        print("Oleo entrou!")
        enderecoClienteOleo = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Decantador":
        print("Decantador entrou!")
        enderecoClienteDecantador = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Reator":
        print("Reator entrou!")
        enderecoClienteReator = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Lavagem1":
        print("Lavagem1 entrou!")
        enderecoClienteLavagem1 = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Lavagem2":
        print("Lavagem2 entrou!")
        enderecoClienteLavagem2 = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Lavagem3":
        print("Lavagem3 entrou!")
        enderecoClienteLavagem3 = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "Secador":
        print("Secador entrou!")
        enderecoClienteSecador = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)

    if resposta == "SecadorEtOH":
        print("SecadorEtOH entrou!")
        enderecoClienteSecadorEtHO = enderecoCliente
        todosOn +=1
        print("Faltam :",10-todosOn)


    if todosOn == 10:
        print("Todos entraram!")
        server.sendto("start".encode(),enderecoClienteEtOH)
        server.sendto("start".encode(),enderecoClienteNaOH)
        server.sendto("start".encode(),enderecoClienteOleo)       
        server.sendto("start".encode(),enderecoClienteReator)
        server.sendto("start".encode(),enderecoClienteDecantador)
        server.sendto("start".encode(),enderecoClienteSecadorEtHO)
        server.sendto("start".encode(),enderecoClienteLavagem1)
        server.sendto("start".encode(),enderecoClienteLavagem2)
        server.sendto("start".encode(),enderecoClienteLavagem3)
        server.sendto("start".encode(),enderecoClienteSecador)
        break
   
print("Começamos!!!")
cont = 0
quantDecantador = 0
quantGlicerina = 0
quantBiodisel = 0
xquantBiodisel = []
ytempo = []
start = time.time()
while True:
    mensageBytes , enderecoCliente = server.recvfrom(2048)
    resposta = mensageBytes.decode()
    end = time.time()

    if enderecoCliente == enderecoClienteOleo:
        server.sendto(resposta.encode(),enderecoClienteReator)
        print("Oleo enviado para o Reator: "+resposta)
    
    if enderecoCliente == enderecoClienteNaOH:
        server.sendto(resposta.encode(),enderecoClienteReator)
        print("NaOH enviado para o Reator: "+resposta)

    if enderecoCliente == enderecoClienteEtOH:
        server.sendto(resposta.encode(),enderecoClienteReator)
        print("EtOH enviado para o Reator: "+resposta)

    if enderecoCliente == enderecoClienteReator:
        if(quantDecantador < 10):
            quantDecantador +=  int(resposta)
            server.sendto(resposta.encode(),enderecoClienteDecantador)            
            print("Enviando para o Decantador: "+resposta)
        else:
            print("Decantador ja esta cheio: ",quantDecantador)
            server.sendto("cheio".encode(),enderecoClienteReator)
    
    if enderecoCliente == enderecoClienteDecantador:
        quantDecantador = 0       
        server.sendto("vazio".encode(),enderecoClienteReator)
        print("Decantador esta livre!  ",quantDecantador)        
        server.sendto(resposta.split(":")[0].encode(),enderecoClienteLavagem1)
        server.sendto(resposta.split(":")[1].encode(),enderecoClienteSecadorEtHO)
        quantGlicerina += float(resposta.split(":")[2])
    if enderecoCliente == enderecoClienteSecadorEtHO:
        print("")
        server.sendto(resposta.encode(),enderecoClienteEtOH)


    if enderecoCliente == enderecoClienteLavagem1:
        print("Lavagem1 feita, enviando: "+resposta+" para a lavagem2")
        server.sendto(resposta.encode(),enderecoClienteLavagem2)

    if enderecoCliente == enderecoClienteLavagem2:
        print("Lavagem2 feita, enviando: "+resposta+" para a lavagem3")
        server.sendto(resposta.encode(),enderecoClienteLavagem3)

    if enderecoCliente == enderecoClienteLavagem3:
        print("Lavagem3 feita, enviando: "+resposta+" para o secador")
        server.sendto(resposta.encode(),enderecoClienteSecador)
    
    if enderecoCliente == enderecoClienteSecador:
        print("Recebendo biodisel: "+resposta)
        quantBiodisel += float(resposta)

    if (end-start)/30 > cont:
        cont += 1
        xquantBiodisel.append(quantBiodisel)
        ytempo.append(end-start)


    if (end-start) > 3600:
        proximo = True
        server.sendto("Acabou".encode(),enderecoClienteReator)
        while proximo:            
            mensageBytes1 , enderecoCliente = server.recvfrom(2048)
            resposta1 = mensageBytes1.decode()
            if verificaResposta(resposta1):
                proximo = False
            
        proximo = True
        server.sendto("Acabou".encode(),enderecoClienteDecantador)
        while proximo: 
            mensageBytes2 , enderecoCliente = server.recvfrom(2048)
            resposta2 = mensageBytes2.decode()
            if verificaResposta(resposta2):
                proximo = False
            

        proximo = True
        server.sendto("Acabou".encode(),enderecoClienteLavagem1)
        while proximo:
            lixo1 , enderecoCliente = server.recvfrom(2048)
            respLixo1 = lixo1.decode()
            if verificaResposta(respLixo1):
                proximo = False
            

        proximo = True
        server.sendto("Acabou".encode(),enderecoClienteLavagem2)
        while proximo:  
            lixo2 , enderecoCliente = server.recvfrom(2048)
            respLixo2 = lixo2.decode()
            if verificaResposta(respLixo2):
                proximo = False
            

        proximo = True
        server.sendto("Acabou".encode(),enderecoClienteLavagem3)
        while proximo:  
            lixo3 , enderecoCliente = server.recvfrom(2048)
            respLixo3 = lixo3.decode()
            if verificaResposta(respLixo3):
                proximo = False
            

        print("============================================")
        print("Funcionou por "+str(end-start)+" e resultou em :")
        print("Quantidade de Glicerina: ",quantGlicerina)
        print("Quantidade de Biodisel: ",quantBiodisel)
        print("============================================")         
        print("Sobrou "+resposta1.split(":")[1]+" L de Oleo")
        print("Sobrou "+resposta1.split(":")[2]+" L de NaOH")  
        print("Sobrou "+resposta1.split(":")[3]+" L de EtOH")   
        print("============================================")
        print("O Reator realizou "+resposta1.split(":")[4]+" ciclos")
        print("O Decantador realizou "+resposta2.split(":")[1]+" ciclos")
        print("============================================")
        print("Foram desperdiçados :")     
        print("O primeiro tanque de lavagem jogou fora: "+respLixo1.split(":")[1]+" de Emulsão")
        print("O segundo tanque de lavagem jogou fora: "+respLixo2.split(":")[1]+" de Emulsão")
        print("O terceiro tanque de lavagem jogou fora: "+respLixo3.split(":")[1]+" de Emulsão")
        print("============================================")
        plt.plot(xquantBiodisel,ytempo)
        plt.xlabel("Quantidade Biodisel em Litros")
        plt.ylabel("Tempo em segundos")
        plt.show()
        break


    


    