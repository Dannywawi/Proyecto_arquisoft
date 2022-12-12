from pymongo import MongoClient

def connectDb():

    cluster=MongoClient("mongodb+srv://user_arqui:1234@cluster0.nsjvyri.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["proyecto"]
    return db