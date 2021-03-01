#!bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

actividades = [
    {
        'id':1,
        'titulo': u'Mi actividad primera',
    },
    {
        'id':2,
        'titulo': u'Mi actividad segunda',
    }
]

@app.route('/actividades', methods = ['GET'])
def get_actividades():
    return jsonify({'actividades':actividades})

@app.route('/actividades/<int:id>', methods = ['GET'])
def get_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if len(actividad) == 0:
        abort(404)
    return jsonify({'actividad': actividad[0]})

@app.route('/actividades', methods = ['POST'])
def create_actividad():
    if not request.json or not 'titulo' in request.json:
        abort(400)
    actividad = {
        'id': actividades[-1]['id']+1,
        'titulo': request.json ['titulo'],
    }
    actividades.append(actividad)
    return jsonify({'actividad': actividad}), 201

@app.route('/actividades/<int:id>', methods=['DELETE'])
def delete_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if len(actividad) == 0:
        abort(404)
    actividades.remove(actividad[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

