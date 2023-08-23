from flask import Flask, render_template, request, flash, redirect
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY']= "PALAVRA-SECRETA"
@app.route("/")
def home():
    return render_template("html/login.html")

@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    usuarios_path = os.path.join(current_directory, 'usuarios.json')

    try:
        with open(usuarios_path) as usuarios_file:
            lista = json.load(usuarios_file)
            cont = 0
            for c in lista:
                cont+=1
                if usuario == c['nome'] and senha == c['senha']:
                    return render_template("html/acesso.html", nomeUsuario=c['nome'])
                if cont >= len(lista):
                    flash('Usuário inválido')
                    return redirect("/")
    except FileNotFoundError:
        return "Arquivo de usuários não encontrado."

 
if __name__ in '__main__':
    app.run(debug=True)