# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from Module import AES, DES, ElGamal, RSA
from flask_cors import CORS

# Creating a Web App
app = Flask(__name__)
CORS(app)

# 암호화 과정에서 필요한 parameter의 종류와 개수를 return한다.
@app.route('/enc/list', methods=['GET'])
def returnEncParam():
    response = {
        "rsa": ['e', 'n'],
        "DES": [],
        "AES": [],
        "ElGamal": []
    }
    return jsonify(response), 200

# 복호화 과정에서 필요한 parameter의 종류와 개수를 return한다.
@app.route('/dec/list', methods=['GET'])
def returnDecParam():
    response = {
        "rsa": ['d', 'n'],
        "DES": [],
        "AES": [],
        "ElGamal": []
    }
    return jsonify(response), 200

@app.route('/test', methods=['GET'])
def test():
    response = {
        "ciphertext": "test"
    }
    return jsonify(response), 200

@app.route('/dec/rsa', methods=['POST', 'GET'])
def post():
    result = request.get_json(silent=True)
    param = {
        'd': int(result['d']),
        'n': int(result['n']),
        'ciphertext': int(result['ciphertext'])
    }
    
    response = {
        "plaintext": str(RSA.decrypt(param))
    }
    return jsonify(response), 200


# Running the App
app.run(host='0.0.0.0', port=5000)


