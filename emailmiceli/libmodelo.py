import datetime
from fpdf import FPDF

def check(n, s):

    arqlog = open("login.txt", "r")
    lista = arqlog.readlines()

    for linha in lista:

        nome, senha = linha.strip().split("-")
            
        if nome == n and senha == s:
                return 1
                
    return 0

def cartinha(data, dest, msg, rem):
    
    global horario
    horario = (datetime.datetime.now())
    horario = (str(horario)).replace(" ", "")
    arqcart = open(horario+".txt", "w+")
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
    pdf.output(horario+".pdf")

def signup(nome, senha):

    arqsignup = open("login.txt", "a")
    arqsignup.write(nome+"-"+senha)
    arqsignup.close()