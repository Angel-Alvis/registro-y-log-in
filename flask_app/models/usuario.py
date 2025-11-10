from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query='''select * from usuarios'''
        resultados=connectToMySQL('db_login').query_db(query)
        usuarios=[]
        for fila in resultados:
            usuarios.append(cls(fila))
        return usuarios

    @classmethod
    def insert(cls, datos):
        query='''insert into usuarios(nombre, apellido, email, password)
        values(%(nombre)s, %(apellido)s, %(email)s, %(password)s)'''
        return connectToMySQL('db_login').query_db(query, datos)
    
    @staticmethod
    def validar_registro(usuario):
        esValido=True
        if len(usuario['nombre']) <=2:
            esValido=False
            flash('Nombre inválido','nombre')
        if len(usuario['apellido'])<=2:
            esValido=False
            flash('Apellido inválido','apellido')
        if not EMAIL_REGEX.match(usuario['email']):
            esValido=False
            flash('E-mail inválido', 'email')
        if len(usuario['password'])<8:
            esValido=False
            flash('La contraseña debe contener al menos 8 caracteres', 'pw')
        if Usuario.get_by_email(usuario):
            esValido=False
            flash('E-mail ya registrado', 'email')
        if usuario['password']!=usuario['confirm_pw']:
            esValido=False
            flash('Contraseñas no coinciden', 'pw')
        if esValido:
            flash('Registro correcto', 'registro')
        else:
            flash('Registro incorrecto', 'registro')
        return esValido

    @classmethod
    def get_by_email(cls, datos):
        query='''select * from usuarios where email=%(email)s'''
        resultados=connectToMySQL('db_login').query_db(query, datos)
        if len(resultados)==1:
            usuario=cls(resultados[0])
            return usuario
        return False
    
    @classmethod
    def get_by_id(cls, datos):
        query='''select * from usuarios where id=%(id)s'''
        resultados=connectToMySQL('db_login').query_db(query, datos)
        if len(resultados)==1:
            usuario=cls(resultados[0])
            return usuario
        return False
