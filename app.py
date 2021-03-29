
from flask import Flask, jsonify, abort, request, make_response

from flask_cors import CORS

from src.webscraping import ws_15mpedia,  ws_supermercados

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
    # main()
    #ws_15mpedia.scraping()
    ws_supermercados.scraping()
