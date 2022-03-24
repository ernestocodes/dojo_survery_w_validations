from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());'
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results

    @classmethod
    def get_most_recent(cls):
        query = 'SELECT * FROM dojos ORDER BY id DESC'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        dojo = cls(results[0])
        return dojo

    @staticmethod
    def validate(dojo):
        is_valid = True
        if len(dojo['name'])<3:
            flash("Name must be at least 3 characters.", 'err_name')
            is_valid = False
        if len(dojo['location'])< 1:
            flash("Location must be selected.", 'err_location')
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Language must be selected.", 'err_language')
        if len(dojo['comment'])< 10:
            flash("Comment must be longer than 10 characters.", 'err_comment')
            is_valid =  False
        return is_valid
