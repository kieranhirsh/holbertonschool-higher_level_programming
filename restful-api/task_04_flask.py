#!/usr/bin/python3
''' module documentation '''
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "not a JSON"}), 400

    for field in ["username", "name", "age", "city"]:
        if field not in data:
            return jsonify({"error": "Missing {}".format(field)}), 400

    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({"message": "User added", "user": users[data["username"]]}), 201

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)