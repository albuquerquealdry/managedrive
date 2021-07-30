import pymongo
from pymongo import MongoClient
from pymongo import collection
from random import randint
import random

def insert_email():
    id=random.randint(1,52)
    client= MongoClient("localhost",27017)
    db = client.mongoDB
    email = input("insert email to email-list:")
    db.listemail.insert_one({
    "id": id,
    "email": email
    })
