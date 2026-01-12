from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.reserva import Reserva

@app.route('/crear/reserva', methods=['POST'])
def crear_reservas():
    if not Reserva.valida_reserva(request.form):
        return redirect('/dashboard')
    
    Reserva.guardar(request.form) #Recibir el identificador del nuevo usuario

    return redirect('/dashboard')

@app.route("/borrar/reserva/<int:id>")
def borrar(id):
    data = {"id": id}
    Reserva.borrar(data)

    return redirect("/dashboard")