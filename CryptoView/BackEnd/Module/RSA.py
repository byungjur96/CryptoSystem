import random
from Module.Tools.Calculator import *

# n과 pi를 계산하는 함수
def make_key(p, q):
    n = p * q
    pi = (p - 1) * (q - 1)
    return [n, pi]

# pi와 서로소이면서 pi보다 작은 수들을 모두 구해서 그 중 임의의 값을 e로 지정하는 함수
def find_e(pi):
    list_e = set({})
    for i in range(2, pi):
        if coprime(i, pi):
            list_e.add(i)
    list_e = list(list_e)
    e = list_e[random.randrange(0, len(list_e))]
    return e

# (e*d) mod pi = 1 인 d를 구하는 함수
def find_d(e, pi):
    d = []
    i = 1
    while len(d) == 0:
        if (i * e) % pi == 1:
            d.append(i)
        else:
            i += 1

    return d[0]


# 암호화를 진행하는 함수
def encrypt(param):
    rsa = RSA()
    mesg = param["plaintext"]
    e = param["e"]
    n = param["n"]

    """
    text로 들어온 경우에 대해 -> 추후 변경
    code = [ord(char) for char in mesg]
    crypto = []
    for m in code:
        c = squareAndMultiply(m, e, n)
        crypto.append(c)
    """
    return squareAndMultiply(mesg, e, n)
    
    

# 복호화를 진행하는 함수
def decrypt(param):
    d = param["d"]
    n = param["n"]
    cipher = param["ciphertext"]
    return squareAndMultiply(cipher, d, n)
