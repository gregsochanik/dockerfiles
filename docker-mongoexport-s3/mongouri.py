import pymongo
import os

uri = os.environ['MONGO_URI']
data = pymongo.uri_parser.parse_uri(uri)
auth = '' if data['username'] is None else '-u %s -p %s' % (data['username'], data['password'])
host = '-h %s:%s' % (data['nodelist'][0][0], data['nodelist'][0][1])
dbname = '-d %s' % data['database']
collection = '' if os.environ.get('MONGO_COLLECTION') is None else '-c %s' % os.environ.get('MONGO_COLLECTION')
authDatabase = '' if os.environ.get('MONGO_AUTH_DATABASE') is None else '--authenticationDatabase %s' % os.environ.get('MONGO_AUTH_DATABASE')
options = '%s %s %s %s %s' % (auth, host, dbname, collection, authDatabase)

print options
