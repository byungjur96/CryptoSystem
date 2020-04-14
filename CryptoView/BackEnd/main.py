# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from Module import AES, DES, ElGamal, RSA
import keygen

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
            "RSA": ['e', 'n'],
            "DES": ['key'],
            "AES": ['key'],
            "ElGamal": ['ya', 'p', 'a']
        },
        "dec": {
            "RSA": ['d', 'n'],
            "DES": ['key'],
            "AES": ['key'],
            "ElGamal": ['xa', 'p', 'a']
        }
    }
    return jsonify(response), 200


# 조건에 맞는 임의의 키 생성
@app.route('/keygen/<alg>', methods=['GET'])
def generate_key(alg):
    print(alg)
    result = keygen.key_separator(alg)
    print(result)
    return jsonify(result), 200


@app.route('/RSA/dec', methods=['POST', 'GET'])
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


@app.route('/RSA/enc', methods=['POST', 'GET'])
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


@app.route('/ElGamal/enc', methods=['POST', 'GET'])
def encrypt_elgamal():
    result = request.get_json(silent=True)
    param = {
        'ya': int(result['y']),
        'p': int(result['p']),
        'a': int(result['a']),
        'plaintext': int(result['plaintext'])
    }
    response = {
        "result": str(ElGamal.encrypt(param))
    }
    return jsonify(response), 200


@app.route('/ElGamal/dec', methods=['POST', 'GET'])
def decrypt_elgamal():
    result = request.get_json(silent=True)
    param = {
        'a': result['a'],
        'p': result['p'],
        'xa': result['xa'],
        'ciphertext': result['ciphertext']
    }
    response = {
        "result" : str(ElGamal.decrypt(param))
    }
    return jsonify(response), 200


# Running the App
app.run(host='0.0.0.0', port=5000)


