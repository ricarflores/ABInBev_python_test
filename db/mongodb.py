from pymongo import MongoClient
from config.config import config

class mongoDB(object):
    _client = MongoClient(config['db']['urlMongo'])
    db = _client[config['db']['db']]
