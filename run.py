"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"
    return "<h2>David Pillco/h2>" 

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
    cadena += "<h4>Ejemplos de Paises por Contientes</h4><br>"
    cadena2 =  <ul><li type="circle">AMÉRICA</li></ul><br><li type="square">Ecuador</li><br><li type="square">Colombia</li>
    
    return cadena
    return cadena2

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
