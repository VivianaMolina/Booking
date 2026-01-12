from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:

    def __init__( self , data ):

        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, contrasena) 
            VALUES(%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s)
            """
        return connectToMySQL('esquema_booking').query_db(query, datos)
    
    @classmethod
    def get_by_email(cls, formulario):

        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL('esquema_booking').query_db(query, formulario)

        if len(resultado) < 1:
            return False
        else:
            usuario = cls(resultado[0])
            return usuario

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True

        if len(formulario['nombre']) < 2:
            flash('The name must contain at least 2 characters', 'registro')
            es_valido = False
        
        if len(formulario['apellido']) < 2:
            flash('The last name must contain at least 2 characters', 'registro')
            es_valido = False
        
        if len(formulario['contrasena']) < 8:
            flash('The password must contain at least 8 characters', 'registro')
            es_valido = False
        
        if formulario['contrasena'] != formulario['confirmar-contrasena']:
            flash('Passwords do not match. Please try again.', 'registro')
            es_valido = False
        
        #Revisamos que email tenga el formato correcto -> Expresiones Regulares
        if not EMAIL_REGEX.match(formulario['email']):
            flash('Invalid email address', 'registro')
            es_valido = False
        
        #Consultamos si existe el correo electrónico
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL('esquema_booking').query_db(query, formulario)
        if results and len(results) >= 1:
            flash('Email address already registered.', 'registro')
            es_valido = False
        
        return es_valido
