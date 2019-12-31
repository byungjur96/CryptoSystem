# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from Module import AES, DES, ElGamal, RSA
from flask_cors import CORS

# Creating a Web App
app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    response = {
        "ciphertext": "test"
    }
    return jsonify(response), 200

@app.route('/dec/rsa', methods=['POST', 'GET'])
def post():
    result = request.get_json(silent=True)
    print(result)
    param = [
        int(result['d']),
        int(result['n']),
        int(result['ciphertext'])
    ]
    response = {
        "plaintext": str(RSA.decrypt(param))
    }
    return jsonify(response)


# Running the App
app.run(host='0.0.0.0', port=5000)


