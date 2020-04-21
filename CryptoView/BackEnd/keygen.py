from Module import RSA
from Module.Tools import Calculator

def key_separator(algorithm):
    if algorithm == "RSA":
        return rsa_key()

def rsa_key():
    # p, q 생성과정 분리하기
    p = Calculator.make_prime(10**4)
    q = Calculator.make_prime(10**4)
    # p == q 인 경우 다시 q를 뽑는다.
    while p == q:
        q = Calculator.make_prime(10**4)
    e = RSA.find_e(pi)
    d = RSA.find_d(e, pi)

    key = {
        "Public Key (e, n)": [e, n],
        "Private Key (d, n)": [d, n]
    }
    print(key)
    return key