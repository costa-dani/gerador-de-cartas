import datetime

arqlog = open("login.txt", "r")
#arqcart = open("cartas.txt", "a")
arqsignup = open("login.txt", "a")

def check(n, s):

    lista = arqlog.readlines()

    for linha in lista:

        nome, senha = linha.strip().split("-")
            
        if nome == n and senha == s:
                return 1
                
    return 0

def cartinha(data, dest, msg, rem):
    
    horario = datetime.datetime.now()
    arqcart = open(str(horario)+".txt", "w+")
    arqcart.write(data+"\n"+dest+"\n"+msg+"\n"+rem)
    arqcart.close()

def signup(nome, senha):
     
    arqsignup.write(nome+"-"+senha)