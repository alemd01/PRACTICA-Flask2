from flask import Flask, render_template,request,abort,json
import os
import sys
app = Flask(__name__)
datos = open('books.json')
libros = json.load(datos)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("base.html",libreria=libros)

@app.route('/libros/<isbn>')
def saca_isbn(isbn):
    for libro in libros:
        if libro.get("isbn")==isbn:
            return render_template("libros.html",almacen=libro)
    abort(404)

port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)
