class Pipelines(object):
    def totalPipe(params):
        try:
            pipeline = []
            pipeName = {
                '$match': {
                    'name': {"$regex": "^"+params['city'], "$options": 'i'}
                }
            }
            pipeline.append(pipeName)
            project = {
                '$project': {
                    '_id': 0,
                    'name': 1
                }
            }
            pipeline.append(project)
            total = {
                '$count': 'total'
            }
            pipeline.append(total)
            return pipeline
        except Exception as err:
            print(err)
            return[]

    def searchPipe(params):
        try:
            pipeline = []
            pipeName = {
                '$match': {
                    'name': {"$regex": "^"+params['city'], "$options": 'i'}
                }
            }
            pipeline.append(pipeName)
            sortPipe = {
                '$sort':{
                    params['sort']: 1
                }
            }
            pipeline.append(sortPipe)
            skip = (int(params['page']) - 1) * int(params['rows'])
            skipMatch = {
                '$skip': skip
            }
            pipeline.append(skipMatch)
            limit = {
                '$limit': int(params['rows'])
            }
            pipeline.append(limit)
            addDiffLat = {
                '$addFields':{
                    'diffLat':{
                        '$subtract': ['$latitude', float(params['latitude'])]
                    }
                }
            }
            pipeline.append(addDiffLat)
            addDiffLong = {
                '$addFields':{
                    'diffLong':{
                        '$subtract': ['$longitude', float(params['longitude'])]
                    }
                }
            }
            pipeline.append(addDiffLong)
            sortByDiff ={
                '$addFields':{
                    'validateGeo': {
                        '$add':['$diffLat','$diffLong']
                    }
                }
            }
            pipeline.append(sortByDiff)
            project = {
                '$project': {
                    '_id': 0,
                    'name': 1,
                    'longitude': 1,
                    'latitude': 1,
                    'geoip.location': 1,
                    'country_code': 1,
                    "diffLat":1,
                    "diffLong":1,
                    "validateGeo":1
                }
            }
            pipeline.append(project)
            return pipeline
        except Exception as err:
            print(err)
            return[]
