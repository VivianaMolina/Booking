from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.usuario import Usuario 
from flask_app.models.reserva import Reserva 

#Importación de BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/registrar', methods=['POST'])
def register():

    if not Usuario.valida_usuario(request.form):
        return redirect('/')
    
    #Guardar registro, encripta la password y la guarda en la variable pwd
    pwd = bcrypt.generate_password_hash(request.form['contrasena'])

    formulario = {
        "nombre": request.form['nombre'].strip().capitalize(),
        "apellido": request.form['apellido'].strip().capitalize(),
        "email": request.form['email'],
        "contrasena": pwd
    }

    id = Usuario.guardar(formulario) #Recibir el identificador del nuevo usuario

    session['usuario_id'] = id
    session['usuario_nombre'] = request.form['nombre'].strip().capitalize()
    session['usuario_apellido'] = request.form['apellido'].strip().capitalize()
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    if 'usuario_id' not in session:
        return redirect("/")

    data = {"usuario_id": session['usuario_id']}
    reservas = Reserva.todas_las_reservas(data)
    return render_template("dashboard.html", reservas=reservas)

@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.get_by_email(request.form)
    if not usuario:
        flash("No account found with this email address", "inicio_sesion")
        return redirect("/")

    if not bcrypt.check_password_hash(usuario.contrasena, request.form['contrasena']):
        flash('Invalid password', 'inicio_sesion')
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    session['usuario_apellido'] = usuario.apellido
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')