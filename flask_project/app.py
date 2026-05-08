from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Niraj:NIRAj123@cluster0.ks8jauz.mongodb.net/")
db = client["testdb"]
collection = db["users"]

@app.route('/')
def home():
    return jsonify({"message": "MongoDB Connected!"})

@app.route('/add')
def add():
    collection.insert_one({"name": "Niraj", "role": "DevOps Learner"})
    return jsonify({"message": "Data inserted"})

@app.route('/get')
def get():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)