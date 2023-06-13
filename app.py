from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class IndexApi(Resource):
    def get(self):
        return jsonify({
            'status_code': 200,
            'message': 'success'
        })
    
api.add_resource(IndexApi, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')