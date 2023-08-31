arqlog = open("login.txt", "r")
arqcart = open("cartas.txt", "a")

def check(n, s):

    lista = arqlog.readlines()

    for linha in lista:

        nome, senha = linha.strip().split("-")
            
        if nome == n and senha == s:
                return 1
                
    return 0

def cartinha(data, dest, msg, rem):
    arqcart.write(data+"\n"+dest+"\n"+msg+"\n"+rem)
