from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models import usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def pagInicio():
    return render_template('inicio.html')

@app.route('/registro', methods=['POST', 'GET'])
def formRegistro():
    if request.method=='GET':
        return redirect ('/')
    datos={
        'nombre':request.form['nombre'],
        'apellido':request.form['apellido'],
        'email':request.form['email'],
        'password':request.form['password'],
        'confirm_pw':request.form['confirm_pw']
        }
    if usuario.Usuario.validar_registro(datos):
        pw_hash=bcrypt.generate_password_hash(request.form['password'])
        datos['password']=pw_hash
        del datos['confirm_pw']
        print(datos)
        usuario.Usuario.insert(datos)
        return redirect('/')
    else:
        return redirect('/')