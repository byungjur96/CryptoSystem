# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from Module import AES, DES, ElGamal, RSA
from flask_cors import CORS

# Creating a Web App
app = Flask(__name__)
CORS(app)

@app.route('/alg/list', methods=['GET'])
def returnAlgList():
    algorithms = ['RSA', 'DES', 'AES', 'ElGamal']
    return jsonify(algorithms), 200


# 암호화/복호화 과정에서 필요한 parmeter의 종류와 개수를 return한다.
@app.route('/params', methods=["GET"])
def returnParams():
    response = {
        "enc" : {
            "rsa": ['e', 'n'],
            "DES": ['key'],
            "AES": ['key'],
            "ElGamal": []
        },
        "dec": {
            "rsa": ['d', 'n'],
            "DES": ['key'],
            "AES": ['key'],
            "ElGamal": []
        }
    }
    return jsonify(response), 200


@app.route('/test', methods=['GET'])
def test():
    response = {
        "ciphertext": "test"
    }
    return jsonify(response), 200


@app.route('/rsa/dec', methods=['POST', 'GET'])
def decrypt_rsa():
    result = request.get_json(silent=True)
    param = {
        'd': int(result['d']),
        'n': int(result['n']),
        'ciphertext': int(result['Ciphertext'])
    }
    
    response = {
        "result": str(RSA.decrypt(param))
    }
    return jsonify(response), 200

@app.route('/rsa/enc', methods=['POST'])
def encrypt_rsa():
    result = request.get_json(silent=True)
    param =  {
        'e': int(result['e']),
        'n': int(result['n']),
        'plaintext': int(result['Plaintext'])
    }

    response = {
        "result": str(RSA.encrypt(param))
    } 
    return jsonify(response), 200


# Running the App
app.run(host='0.0.0.0', port=5000)


