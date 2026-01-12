from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Reserva:

    def __init__( self , data ):

        self.id = data['id']
        self.reserva = data['reserva']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

    @classmethod
    def guardar(cls, datos):
        print(datos)
        query = """
            INSERT INTO reservas (reserva, usuario_id) 
            VALUES(%(reserva)s, %(usuario_id)s);
            """
        return connectToMySQL('esquema_booking').query_db(query, datos)

    @classmethod
    def todas_las_reservas(cls, data):

        query = "SELECT * FROM reservas where usuario_id = %(usuario_id)s;"
        results = connectToMySQL('esquema_booking').query_db(query, data)

        if not results:
            return []   # evita el TypeError
    
        reservas = []
        for fila in results:
            reservas.append(cls(fila))
        return reservas
    
    @classmethod
    def borrar(cls, data):
        query = "DELETE FROM reservas WHERE id = %(id)s"
        connectToMySQL("esquema_booking").query_db(query, data)

    @staticmethod
    def valida_reserva(formulario):
        es_valido = True
        if len(formulario["reserva"]) < 1:
            flash('Unable to create a reservation. Please complete all required fields', 'reserva')
            es_valido = False     
        return es_valido
