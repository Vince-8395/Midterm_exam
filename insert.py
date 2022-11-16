from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager


class HeartRateAPI(Resource):

    def get(self):
        HeartRate = HeartRate.objects().to_json()
        return Response(HeartRate, mimetype="application/json", status=400)

    @jwt_required()
    def post(self):
        body = request.get_json()
        HeartRate = HeartRate(**body).save()
        id = HeartRate.id
        return {'id': str(id)},200
            


        

