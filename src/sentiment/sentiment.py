from flask import jsonify
from textblob import TextBlob

def getSentiment(textInput):
    analysis = TextBlob(textInput)
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

