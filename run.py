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
    cadena = "<h4>Continentes</h4><ol><li>America</li><li>Europa</li><li>Africa</li><li>Oceania</li><li>Antartida</li>"
    return cadena


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
