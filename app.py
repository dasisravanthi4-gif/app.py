from flask import Flask, request

app = Flask(__name__)
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return users

@app.route('/users', methods=['POST'])
def post_user():
    data = request.json
    users[data['id']] = data
    return {"message": "User added"}

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    users[id] = data
    return {"message": "User updated"}

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    users.pop(id, None)
    return {"message": "User deleted"}

if __name__ == '__main__':
    app.run(debug=True)