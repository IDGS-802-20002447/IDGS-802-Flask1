from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])

def operasBas():
    
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        op=request.form.get("op")

        if op=="suma":
            return "<h2> La suma es: {}</h2>".format(str(int(num1)+int(num2)))
        if op=="resta":
            return "<h2> La resta es: {}</h2>".format(str(int(num1)-int(num2)))
        if op=="multi":
            return "<h2> La multiplicacio es: {}</h2>".format(str(int(num1)*int(num2)))

        if op=="divi":
            return "<h2> La division es: {}</h2>".format(str(int(num1)/int(num2)))    


        return "<h2>Selceciiona Datos</h2>".format(str(int(num1)+int(num2)))

    else:
       return '''
        <form action="/operasBas" method="POST">
        <label> N1: </label>
        <input type="text" name="num1"/></br></br>
        <label> N2: </label>
        <input type="text" name="num2"/></br></br>
        
        
        <input type="radio" id="suma" name="op" value="suma">
        <label for="suma">SUMA</label>

        <input type="radio" id="resta" name="op" value="resta">
        <label for="resta">Resta</label><br>
        
        <input type="radio" id="multi" name="op" value="multi">
        <label for="multi">Multiplicacion</label><br>
       
        <input type="radio" id="div" name="op" value="divi" >
        <label for="div">Division</label><br>
        
        <input type="submit" value="calcular"/><br></br></br>

        </form>
        '''


if __name__=="__main__":
    app.run(debug=True,port=5000)

