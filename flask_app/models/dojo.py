from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data): # data as a dictionary
        # need dojo first before I can create a ninja?
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db( query )
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        return connectToMySQL('dojos_and_ninjas').query_db( query , data )

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name"  : row_from_db["last_name"],
                "dojos_id"   : row_from_db["dojos_id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo