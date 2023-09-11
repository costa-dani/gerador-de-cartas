import datetime
from fpdf import FPDF

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
    
    global horario
    horario = datetime.datetime.now()
    arqcart = open(str(horario)+".txt", "w+")
    arqcart.write(data+"\n"+dest+"\n"+msg+"\n"+rem)
    arqcart.close()
    pdf(str(horario)+".txt")

def pdf(nome):
    arq = open(nome, "r")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    for l in arq:
        pdf.cell(200, 10, txt = l, ln = 1, align = 'C')
    pdf.output(str(horario)+".pdf")

def signup(nome, senha):
     
    arqsignup.write(nome+"-"+senha)