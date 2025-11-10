from flask_app import app
from flask import render_template, redirect, flash, request, session, url_for
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return redirect('/')
    user = usuario.Usuario.get_by_email(request.form)
    if not user:
        flash('E-mail no registrado', 'email_login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Constraseña incorrecta', 'pw_login')
        return redirect('/')
    session['user_id']=user.id
    return redirect(url_for('pagUser'))

@app.route('/user')
def pagUser():
    if 'user_id' not in session:
        return redirect ('/')
    datos={'id':session['user_id']}
    user=usuario.Usuario.get_by_id(datos)
    if not user:
        session.clear()
        return redirect ('/')
    return render_template('user.html', user=user)

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Sesión terminada', 'logout')
    return redirect ('/')