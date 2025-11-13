from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import usuario

class Mision:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.fecha=data['fecha']
        self.numero_voluntarios=data['numero_voluntarios']
        self.descripcion=data['descripcion']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.usuario_id=data['usuario_id']
        self.usuario_nombre=data['usuario_nombre']

    @classmethod
    def get_all_misiones(cls):
        query='''select *, usuarios.nombre as usuario_nombre, usuarios.id as usuario_id
                from misiones
                join usuarios on usuario_id=usuarios.id'''
        resultados=connectToMySQL('db_login').query_db(query)
        misiones=[]
        for resultado in resultados:
            datos={
                'id':resultado['id'],
                'nombre':resultado['nombre'],
                'fecha':resultado['fecha'],
                'numero_voluntarios':resultado['numero_voluntarios'],
                'usuario_id':resultado['usuario_id'],
                'usuario_nombre':resultado['usuario_nombre'],
                'descripcion':resultado['descripcion']
            }
            misiones.append(datos)
        return misiones
    
    @classmethod
    def insert(cls, datos):
        query='''insert into misiones(nombre, fecha, descripcion, numero_voluntarios, usuario_id)
                values (%(nombre)s, %(fecha)s, %(descripcion)s, %(numero_voluntarios)s, %(usuario_id)s)'''
        return connectToMySQL('db_login').query_db(query, datos)
    
    @staticmethod
    def validacion(datos):
        esCorrecto=True
        if len(datos['nombre'].strip()) == 0:
            flash('Nombre inválido', 'nombre')
            esCorrecto = False
        if len(datos['fecha']) == 0:
            flash('Fecha inválida', 'fecha')
            esCorrecto = False
        if datos['numero_voluntarios'].strip() == '' or int(datos['numero_voluntarios']) < 2 or int(datos['numero_voluntarios']) > 20:
            flash('Debe haber al menos un voluntario','numero_voluntarios')
            esCorrecto = False
        if len(datos['descripcion'].strip()) == 0:
            flash('Descripción inválida','descripcion')
            esCorrecto = False
        return esCorrecto
    
    @classmethod
    def get_by_id(cls, datos):
        query='''select *, usuarios.nombre as usuario_nombre, usuarios.id as usuario_id
                from misiones
                join usuarios on usuario_id=usuarios.id where misiones.id=%(id)s'''
        resultados=connectToMySQL('db_login').query_db(query, datos)
        if len(resultados)==1:
            mision=cls(resultados[0])
            return mision
        return False

    @classmethod
    def edit(cls, datos):
        query='''update misiones 
        set nombre=%(nombre)s, fecha=%(fecha)s, numero_voluntarios=%(numero_voluntarios)s, descripcion=%(descripcion)s
        where misiones.id=%(id)s
        '''
        print ("exito edit")
        return connectToMySQL('db_login').query_db(query,datos)

    @classmethod
    def delete(cls,datos):
        query='''delete from misiones
        where id=%(id)s'''
        return connectToMySQL('db_login').query_db(query,datos)