# settings of mongoDB client
import pymongo 

username = 'user_auth'
password = 'user_auth_password'

mongo_client = pymongo.MongoClient('mongodb://{user}:{pwd}@localhost:27017/admin'.format(user = username, pwd = password))