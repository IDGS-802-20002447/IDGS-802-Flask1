from flask import Flask,render_template
from flask import request


app=Flask(__name__)

@app.route("/operasBas",methods=["GET"])
def operasBas():
    return render_template("/operasBas.html")

@app.route("/resultado",methods=["POST"])
def resultado():
 n1 = request.form.get("txtNum1")
 n2 = request.form.get("txtNum2")

 res = int(n1) * int(n2)
 i = 0
 suma = 0
 restSuma = ""
 while i < int(n2):
    suma = suma + int(n1)
    if restSuma == "":
       restSuma = restSuma + n1
    else:
       restSuma = restSuma +" + "+ n1
       i += 1
    return render_template("/resultadoAct.html", res = res,restSuma = restSuma, suma = suma)
 

if __name__=="__main__":
    app.run(debug=True,port=5000)

