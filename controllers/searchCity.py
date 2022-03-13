from flask import jsonify
from pipelines.aggregates import Pipelines
from db.mongoFunctions import mongoAcctions
class City:
    def searchCity(params):
        try:
            if not params['city'] or (params['latitude'] == "0" or params['longitude'] == "0"):
                return jsonify({
                    'error': True,
                    'sucess': False,
                    'search': [],
                    'msg': 'malformet search, no city or latitude/longitude'
                })
            pipeline = Pipelines.searchPipe(params)
            data = mongoAcctions.aggregate(pipeline)
            if not data:
                return jsonify({
                    'error': False,
                    'sucess': True,
                    'search': [],
                    'msg': 'not results'
                })
            orderList = sorted(data, key=lambda x: x['validateGeo'], reverse=True)
            interactive = 0
            for doc in reversed(orderList):
                score = 0
                if doc['validateGeo'] == 0:
                    score = 1
                else:
                    toRest = ((interactive+1) /len(orderList))
                    if toRest == 1:
                        score = 0.99
                    else:
                        score = score  + toRest
                interactive = interactive + 1
                doc['score'] = round(score, 2)
                del doc['diffLat']
                del doc['diffLong']
                del doc['validateGeo']
            totalPipe = Pipelines.totalPipe(params)
            totalData = mongoAcctions.aggregate(totalPipe)[0]
            pagination = mongoAcctions.getPagination(totalData['total'], params)
            return jsonify({
                'search': orderList,
                'error': False,
                'sucess': True,
                'pagation': pagination
            })
        except Exception as err:
            print(err)
            return jsonify({
                'error': True,
                'sucess': False,
                'search': [],
            })
