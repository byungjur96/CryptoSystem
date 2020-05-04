from Module import RSA
from Module.Tools import Calculator
import random

def key_separator(algorithm):
    if algorithm == "RSA":
        return rsa_key()
    elif algorithm == "ElGamal":
        return elgamal_key()

def rsa_key():
    # p, q 생성과정 분리하기
    p = Calculator.make_prime(10**4)
    q = Calculator.make_prime(10**4)
    # p == q 인 경우 다시 q를 뽑는다.
    while p == q:
        q = Calculator.make_prime(10**4)

    n = p * q
    pi = (p - 1) * (q - 1)
    
    e = RSA.find_e(pi)
    d = RSA.find_d(e, pi)

    key = {
        "Public Key (e, n)": [e, n],
        "Private Key (d, n)": [d, n]
    }
    print(key)
    return key

def elgamal_key():
    p = Calculator.make_prime(10**4)
    g = None
    primitive_root = []
    no_duplicate = True
    while no_duplicate:
        print('g')
        g = random.randrange(2, p-1)
        no_duplicate = Calculator.isPrimitiveRoot(g, p)
    e = random.randrange(2, p-2)
    y = Calculator.squareAndMultiply(g, e, p)

    key = {
        "Public Key": [y],
        "Private Key": [e]
    }