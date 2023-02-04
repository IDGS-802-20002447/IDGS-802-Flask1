from flask import Flask, render_template,request

app=Flask(__name__)


@app.route("/cinepolis",methods=["GET"])
def cinepolis():
    return render_template("/cinepolis.html")

@app.route("/Resul",methods=["POST"])
def resultado():
   n1=int(request.form.get("txtNum1"))
   n2=int(request.form.get("txtNum2"))
   op=request.form.get("op")
   nombre=request.form.get("nameUse")

   rest=int(n1)*int(n2)
   resulTar=""
  
   
   if int(n1)>=5:
      resul=(int(rest)*.85)
     

   if int(n1)>=2:
      resul=(rest*.90)    

   else:
        resul=rest 
   

   if op=="si":
        resulTar=(int(resul)*.90)
        resulTar=(str(int(resulTar)))

   if op=="no":
        resulTar=(str(int(resul)))     


   return render_template("/cinepolisResul.html",resulTar=resulTar,user=nombre)



if __name__=="__main__":
    app.run(debug=True,port=4000)
