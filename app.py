from flask import Flask, jsonify, abort, request, make_response
from flask_cors import CORS
from src.webscraping import ws_15mpedia
from src.webscraping import ws_opiniones
from src.webscraping import ws_supermercados
from src.webscraping import ws_noticias
from src.webscraping import ws_estaciones
from src.webscraping import ws_sanidad
from src.sentiment import sentiment

def main():
    app = Flask(__name__)
    CORS(app)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.route('/api/sentiment', methods=['POST'])
    def sentimiento():
        return sentiment.getSentiment(request.json['text'])

    app.run(debug=True)


def webscraping():
    # TODO paginacion
    while True:
        print('Opciones: \
            \n 1-Opiniones de restaurantes \
            \n 2-Supermercados \
            \n 3-Noticias \
            \n 4-Lista de todos los municipios (Tiempo de ejecucion elevado) \
            \n s-Para salir')

        selector = input('Introduzca la opción deseada: ')

        if selector == '1':
            ws_opiniones.scraping()
        elif selector == '2':
            provincia = input("Introduce el nombre de la provincia (con minúsculas y tilde): ")
            municipio = input("Introduce el nombre del municipio (con tilde): ")
            ws_supermercados.scraping(provincia, municipio)
        elif selector == '3':
            ws_noticias.scraping()
        elif selector == '4':
            ws_15mpedia.scraping()
        elif selector == 's':
            print('¡Hasta pronto!')
            exit(0)
        else:
            print('\nError, introduzca una opción válida\n')


if __name__ == '__main__':
    # main() #Para ejecutar la API de flask y realizar el análisis del sentimiento
    # webscraping() #Para elegir entre los distintos ws a ejecutar (Segunda entrega PCII)
    # ws_15mpedia.scraping() #Para insertar los municipios en la BBDD, ejecutar una sola vez (YA HECHO)
    # ws_estaciones.scrap() #Para insertar las estaciones en la BBDD, ejecutar una sola vez (YA HECHO)
    # ws_sanidad.scrap() #Para insertar los centros sanitarios en la BBDD, ejecutar una sola vez (YA HECHO)
    ws_noticias.scraping()