from flask import Flask

app=Flask(__name__)

@app.route("/")

def index():
    return "!Hola Mundo! --NUEVO"

#http://127.0.0.1:3000/user/nadia
@app.route("/user/<string:user>")
def user(user):
    return "Hola: "+user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero:{}".format(n)

#http://127.0.0.1:3000/user/1/Nadia
@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "<h1> ID: {} NOMBRE: {}</h1>".format(id,username)

#http://127.0.0.1:3000/suma/2.9/8.3
@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

#http://127.0.0.1:3000/default/midatos
@app.route("/default")
@app.route("/default/<string:n>")
def default(n="datos"):
    return "Los datos son:" + n


if __name__=="__main__":
    app.run(debug=True,port=3000)

