from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager

class HeartRateApi(Resource):

@jwt_required()
    def read(self):
        HeartRate.objects.get(id=id).update(**body)
        return 'Heart Rate was successfully read', 200