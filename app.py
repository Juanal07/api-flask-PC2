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

@app.route('/sentiment', methods = ['POST'])
def sentiment():
    sentiment = request.json['text']
    analysis = TextBlob(sentiment)
    language = analysis.detect_language()
    if language != 'en':
        analysis= analysis.translate(to='en')
    print(analysis)
    analysisPol = analysis.sentiment.polarity
    analysisSub = analysis.sentiment.subjectivity
    print(f'Tiene una polaridad de {analysisPol} y una subjectibidad de {analysisSub}')
    if analysisPol >= 0.7:
        # muy feliz
        return jsonify({'result': 1})
    elif analysisPol >= 0.3 and analysisPol < 0.7:
        # feliz, o mas o menos feliz
        return jsonify({'result': 2})
    elif analysisPol > -0.3 and analysisPol < 0.3:
        # Sentimiento neutral
        return jsonify({'result': 3})
    elif analysisPol > -0.7 and analysisPol <= -0.3:
        # triste, o mas o menos triste
        return jsonify({'result': 4})
    else:
        # muy triste
        return jsonify({'result': 5})

if __name__ == '__main__':
    app.run(debug=True)

