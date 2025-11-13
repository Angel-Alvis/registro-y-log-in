from flask_app import app
from flask import render_template, redirect, flash, request, session, url_for
from flask_app.models import usuario, mision

@app.route('/crear_mision')
def pagCrearMision():
    return render_template ('crear_mision.html')

@app.route('/formMision', methods=['POST', 'GET'])
def formMision():
    if request.method=='GET':
        return redirect('/')
    datos={
        'nombre':request.form['nombre'],
        'fecha':request.form['fecha'],
        'numero_voluntarios':request.form['numero_voluntarios'],
        'descripcion':request.form['descripcion'],
        'usuario_id':session['usuario_id']
    }
    if mision.Mision.validacion(datos):
            mision.Mision.insert(datos)
            return redirect ('/user')
    return redirect('/crear_mision')

@app.route ('/ver_mision/<int:id>')
def verMision(id):
    if 'usuario_id' not in session:
        return redirect ('/')
    datos={'id':id}
    resultados=mision.Mision.get_by_id(datos)
    return render_template('ver_mision.html', mision=resultados)

@app.route('/editar/<int:id>')
def pagEditar(id):
    if 'usuario_id' not in session:
        return redirect ('/')
    datos={'id':id}
    resultados=mision.Mision.get_by_id(datos)
    if resultados.usuario_id != session['usuario_id']:
        return redirect ('/user')
    return render_template('editar.html', mision=resultados)

@app.route('/editar/<int:id>/cambio', methods=['POST', 'GET'])
def formEditar(id):
    if request.method =='POST':
        datos={
            'id':id,
            'nombre':request.form['nombre'],
            'fecha':request.form['fecha'],
            'numero_voluntarios':request.form['numero_voluntarios'],
            'descripcion':request.form['descripcion'],
            }
        if mision.Mision.validacion(datos):
            mision.Mision.edit(datos)
            return redirect ('/user')
        return redirect(f'/editar/{id}')

@app.route('/eliminar/<int:id>')
def eliminar_mision(id):
    if 'usuario_id' not in session:
        return redirect('/')
    datos={'id':id}
    resultados=mision.Mision.get_by_id(datos)
    if resultados.usuario_id != session['usuario_id']:
        return redirect ('/user')
    mision.Mision.delete(datos)
    return redirect ('/user')