from flask import render_template, redirect, session, request, flash
from flask_app import app

#importamos la clase Message
from flask_app.models.messages import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    #verificamos que el usuario haya iniciado sesión:
    if 'user_id' not in session:
        return redirect('/')

    #guardamos el mensaje:
    Message.save(request.form)
    return redirect('/dashboard')

@app.route('/eliminar/mensaje/<int:id>') #en mi url voy a obtener el id del mensaje a borrar
def eliminar_mensaje(id):
    formulario = {"id": id}
    Message.eliminate(formulario)
    return redirect('/dashboard')