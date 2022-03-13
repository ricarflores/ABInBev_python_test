from unittest import result
from flask import request, jsonify, Response
import flask
from controllers.searchCity import City
app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.errorhandler(404)
def not_found(e):
    return Response("Not found", status=404, mimetype='application/json')
@app.route('/search', methods=['GET'])
def getSearch():
    try:
        city = request.args.get('q')
        page = request.args.get('page', default=1, type=int)
        rows = request.args.get('rows', default=10, type=int)
        sort = request.args.get('sort', default="name", type=str)
        latitude = request.args.get('latitude', default="0", type=str)
        longitude = request.args.get('longitude', default="0", type=str)
        params = {'city': city, 'page': page, 'rows': rows,
                  'sort': sort, 'latitude': latitude, 'longitude': longitude}
        res = City.searchCity(params)
        return res
    except Exception as err:
        print(err)
        return jsonify({
            'error': True,
            'sucess': False,
            'search': []
        })


if __name__ == "__main__":
    app.run(port='5050')
