from flask import Flask

app = Flask(__name__)

#Variaveis 
@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def olamundo(usuario, idade, altura):
    return {
        "Usuario": usuario,
        "idade": idade,
        "altura": altura
    }



@app.route("/bemvindo")
def hello_world():
    return {
        'message':'Hello world'
    }