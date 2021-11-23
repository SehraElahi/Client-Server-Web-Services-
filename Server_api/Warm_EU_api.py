from flask import Flask, jsonify, json
from flask_restful import Api, Resource
from DataHotEUCountries import HotEUCountries

app = Flask(__name__)
api = Api(app)

#create the Restful web service 
class Countries(Resource):
    def get (self):
        json_data = jsonify({'HotEUCountries': HotEUCountries})
        return json_data

#my api-->publishing web service
#name http://127.0.0.1:5000/countries
api.add_resource(Countries, "/", methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, port =5050)
