from flask import Flask, render_template,request,abort
import json
import os
import sys
app = Flask(__name__)
def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
            return datos
    except:
        print("ERROR AL LEER EL FICHERO")
        sys.exit(0)
libros=leer_json("books.json")

@app.route('/')
def inicio():
	return render_template("base.html",libreria=libros)
@app.route('/libros/<isbn>')
def saca_isbn(isbn):
    for libro in libros:
        if libro.get("isbn")==isbn:
            return render_template("libros.html",almacen=libro)
        abort(404)
#port=os.environ["PORT"]
app.run("0.0.0.0",port=5555,debug=True)
