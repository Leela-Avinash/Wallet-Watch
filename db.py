from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["expense_tracker_db"]