from textblob import TextBlob

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