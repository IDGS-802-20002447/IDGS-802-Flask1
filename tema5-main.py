from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")

def index():
    titulo="Home! Nad"
    lista=["Pedro","Laura","Luis"]
    return render_template("index.html",titulo=titulo,lista=lista)

#http://127.0.0.1:3000/Aumnos
@app.route("/Alumnos")
def alumnos():
    return render_template("alumnos.html")

#http://127.0.0.1:3000/Usuarios
@app.route("/Usuarios")
def usuarios():
    return render_template("usuarios.html")



if __name__=="__main__":
    app.run(debug=True,port=3000)

