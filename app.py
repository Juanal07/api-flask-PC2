from flask import Flask, jsonify, abort, request, make_response
from flask_cors import CORS
from src.webscraping import ws_15mpedia
from src.webscraping import ws_opiniones
from src.webscraping import ws_supermercados
from src.webscraping import ws_noticias

def main():
    app = Flask(__name__)
    CORS(app)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error':'Not found'}),404)

    @app.route('/sentiment', methods = ['POST'])
    def sentiment():
        return jsonify({'result': 0.7})

    app.run(debug=True)

if __name__ == '__main__':
    # TODO probar el tema de textblob
    # TODO paginacion
    # main()
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
            ws_supermercados.scraping()
        elif selector == '3':
            ws_noticias.scraping()
        elif selector == '4':
            ws_15mpedia.scraping()
        elif selector == 's':
            print('¡Hasta pronto!')
            exit(0)
        else:
            print('\nError, introduzca una opción válida\n')
