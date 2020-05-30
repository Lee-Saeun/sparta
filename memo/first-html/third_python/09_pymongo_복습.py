from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta2

all_users = list(db.users.find())

same_ages = list(db.users.find({'age':24}))


for user in all_users :
    print(user['name'])