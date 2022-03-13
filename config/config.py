import json 

config = {
    'db':{
        'user': 'admin',
        'address': 'SG-empty-hound-8155-50128.servers.mongodirector.com',
        'port': '27017',
        'password': 'KgmzQz9z0adgUzqS',
        'info': '',
        'option': '{ useNewUrlParser: true }',
        'db': 'Paises',
        'collection': 'City'
    }
}
if 'urlMongo' not in config['db']:
    if config['db']['user'] is not '':
        config['db']['urlMongo'] = 'mongodb://' + config['db']['user'] + ':' + config['db']['password'] + '@' + config['db']['address'] + ':' + config['db']['port'] + "/admin" 
    else:
        config['db']['urlMongo'] = 'mongodb://' + config['db']['address'] + ':' + config['db']['port'] + '/' + config['db']['info']