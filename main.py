from flask import Flask, render_template,request #manipula los datos


app=Flask(__name__)


@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan","Pedro","Mario"]
    return render_template("index.html", grupo=grupo,lista=lista)

@app.route('/OperasBas',methods=["GET","POST"])
def operas():
    if request.method == "POST":
        # Colocar el request con los puntos y las palabras indica que va a tomar un valor que se le indique. En este caso es n1 y n2
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        res="La suma de {} y {} es {}".format(num1,num2,int(num1)+int(num2))
        return render_template("OperasBas.html", res=res)
    return render_template("OperasBas.html")
    
@app.route('/resultado',methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        # Colocar el request con los puntos y las palabras indica que va a tomar un valor que se le indique. En este caso es n1 y n2
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "La suma de {} y {} es {}".format(num1,num2,int(num1)+int(num2))


@app.route('/cinepolis',methods=["GET","POST"])
def cinepolis():
    res=""
    resultado=0
    if request.method == "POST":
        com=int(request.form.get("compradores"))
        bol=int(request.form.get("boletos"))
        cineco=request.form.get("radio")
        num=7
        precio=12
        total=bol*precio
        if bol>(com*num):
            res="El número de boletos es mayor al permitido por persona"
            return render_template("cinepolis.html", res=res, resultado=0)
        if bol>5:
            total*=0.85
        if bol>2 and bol<=5:
            total*=0.90
        if  cineco=="si":
            total*=0.90
        resultado=total
    return render_template("cinepolis.html", res=res, resultado=resultado)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/hola')
def hola():
    return "Hola!!!"

@app.route('/user/<string:user>')
def user(user):
    return f"Hola {user}!!!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<string:user>/<int:id>')
def username(user,id):
    return f"Nombre: {user} ID: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2)

""" @app.route("/default")
@app.route("/default/<string:nom")
def func(nom='pedro'):
    return "El nombre es Nom es "+nom """

@app.route("/form1")
def form1():
    return '''
            <form>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True, port=3000)