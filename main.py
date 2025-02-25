from flask import Flask, render_template,request #manipula los datos
from flask import g
from flask_wtf.csrf import CSRFProtect # Ayuda ante ataques CSRF
from flask import flash
import forms

app=Flask(__name__)
app.secret_key="Esta es la clave secreta"
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# imprime una solictud antes de cualquier otra.
@app.before_request
def before_request():
    g.nombre="Mario"
    print(' Before request 1')

 #imprime una solictud despues de cualquier otra.
@app.after_request
def after_request(response):
    print(' After request 3')
    return response


@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan","Pedro","Mario"]
    print("Index 2")
    print("Hola {}".format(g.nombre))
    return render_template("index.html", grupo=grupo,lista=lista)

@app.route('/Alumnos', methods=["GET","POST"])
def alumnos():
    mat=''
    nom=''
    edad=''
    correo=''
    ape=''
    alumno_clase=forms.UserForm(request.form) #instancia de la clase de forms.py
    if request.method=='POST' and alumno_clase.validate():
        mat=alumno_clase.matricula.data
        nom=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.email.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clase,mat=mat,nom=nom,ape=ape,edad=edad,correo=correo)

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
    csrf.init_app(app) # Esto principalmente sirve para que pase los parametros que definimos en la clave secrete
    app.run(debug=True, port=3000)