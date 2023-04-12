from flask import Flask, jsonify, request
from db import get_db

app = Flask(__name__)
db = get_db()


@app.route('/users', methods=['POST'])
def create_user():
    if db is None:
        return jsonify({"message": "Database connection error"}), 500

    username = request.json['username']
    password = request.json['password']
    user_id = db.users.insert_one({'username': username, 'password': password}).inserted_id
    new_user = db.users.find_one({'_id': user_id})

    result = {'username': new_user['username'], 'password': new_user['password']}
    return jsonify({'result': result}), 201


if __name__ == '__main__':
    app.run(debug=True)
