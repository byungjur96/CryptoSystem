# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

# Creating a Web App
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    response = {
        "ciphertext": "test"
    }
    return jsonify(response), 200

@app.route('/post', methods=['POST', 'GET'])
def post():
    result = request.get_json(silent=True)
    print("Input: ", result)
    response = {
        "ciphertext": result["plaintext"]
    }
    print("Output: ", response)
    return jsonify(response)


# Running the App
app.run(host='0.0.0.0', port=5000)

