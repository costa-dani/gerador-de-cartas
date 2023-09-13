from flask import Flask, render_template, request
import libmodelo

app = Flask (__name__)
app.secret_key = "euvoficamaluca"

@app.route("/")
def hello():
    return render_template("login.html")

'''
@app.route("/login", methods = ["POST", "GET"])
def login():

    if request.method == "POST":

        nome = request.form.get("nome")
        senha = request.form.get("senha")

        if libmodelo.check(nome,senha):

            return render_template("carta.html")
        
        else: 
            return "<h1>Login invalido</h1>"
    
    return render_template("login.html")
'''

@app.route("/login", methods = ["POST"])
def entrar():
    if request.method == "POST":

        escolha = request.form.get("botao")

        if escolha == "login":

            nome = request.form.get("nome")
            senha = request.form.get("senha")

            if libmodelo.check(nome,senha):

                return render_template("carta.html")
        
            else: 
                return "<h1>Login invalido</h1>"
        
        elif escolha == "signup":

            nome = request.form.get("nome")
            senha = request.form.get("senha")

            libmodelo.signup(nome, senha)

            escolha2 = request.form.get("botao")

            if escolha2 == "signup":
                return render_template("cadastro.html")
            
            elif escolha2 == "login":
                return render_template("login.html")

            return render_template("cadastro.html")
        
    return render_template("login.html")

@app.route("/carta", methods = ["POST"])
def carta():
    if request.method == "POST":

        data = request.form.get("data")
        dest = request.form.get("dest")
        msg = request.form.get("msg")
        rem = request.form.get("rem")

        libmodelo.cartinha(data, dest, msg, rem)

        return render_template("carta.html")

app.run()