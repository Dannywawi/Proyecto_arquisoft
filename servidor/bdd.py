from pymongo import MongoClient

def connectDb():

    cluster=MongoClient('mongodb://localhost:27017/')
    db=cluster["proyecto"]
    return db