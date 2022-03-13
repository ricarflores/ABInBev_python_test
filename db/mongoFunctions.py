from db.mongodb import mongoDB
from config.config import config
import math
class mongoAcctions(object):
    def aggregate(pipeline):
        try:
            db = mongoDB.db[config['db']['collection']]
            agg = db.aggregate(pipeline)
            return list(agg)
        except Exception as err:
            print(err)
            return []
    def getPagination(totalItems, params):
        try:
            currentPage = int(params['page'])
            itemsPerPage =  int(params['rows'])
            result = {'start':1, 'end': itemsPerPage}
            if (itemsPerPage * currentPage) > totalItems:
                result['start'] = (currentPage * itemsPerPage) - (itemsPerPage + 1)
                result['end'] = totalItems
            elif currentPage > 1:
                result['start'] = (currentPage * itemsPerPage) - (itemsPerPage -1)
                result['end'] = (currentPage * itemsPerPage)
            result['hasNextPage'] = (itemsPerPage * currentPage) < totalItems
            result['hasPreviousPage'] = currentPage > 1
            result['nextPage'] = currentPage + 1
            result['previousPage'] = currentPage -1
            result['lastPage'] = math.ceil(totalItems / itemsPerPage)
            result['itemsPerPage'] = itemsPerPage
            result['totalDocuments'] = totalItems
            result['currentPage'] = currentPage
            if result['start'] == 1:
                result['start'] = 0
            if result['start'] == -1:
                result['start'] = 0
            return result
        except ValueError as err:
            print(err)
            return 0 