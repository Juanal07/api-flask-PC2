#!bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from textblob import TextBlob

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

@app.route('/sentimiento', methods = ['POST'])
def sentimiento():
    if request.method == 'POST':
        sentencia = request.form['sentencia']
        analysis = TextBlob(sentencia)
        traduccion= analysis.translate(to='en')
        print(traduccion)
        analysisPol = traduccion.sentiment.polarity
        analysisSub = traduccion.sentiment.subjectivity
        print(f'Tiene una polaridad de {analysisPol} y una subjectibidad de {analysisSub}')
        if analysisPol >= 0.7:
            return 'muy feliz'
            print ('muy feliz')
        elif analysisPol >= 0.3 and analysisPol < 0.7:
            return 'feliz, o mas o menos feliz'
            print ('feliz, o mas o menos feliz')
        elif analysisPol > -0.3 and analysisPol < 0.3:
            return 'Sentimiento neutral'
            print ('Sentimiento neutral')
        elif analysisPol > -0.7 and analysisPol <= -0.3:
            return 'triste, o mas o menos triste'
            print ('triste, o mas o menos triste') 
        else:
            return 'muy triste'
            print('muy triste')
        return 'recibido'


if __name__ == '__main__':
    app.run(debug=True)

