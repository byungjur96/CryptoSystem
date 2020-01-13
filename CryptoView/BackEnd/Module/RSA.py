import random
from Module.Tools.Calculator import *


class RSA:
    # 지정한 범위 내 임의의 소수를 출력하는 함수
    def make_p(self):
        list_p = find_prime('p')
        while len(list_p) == 0:
            print('Chosen range has no prime number!')
            list_p = find_prime('p')
        list_p = list(list_p)
        p = list_p[random.randrange(0, len(list_p))]
        return p

    # 지정한 범위 내 임의의 소수를 출력하는 함수
    def make_q(self):
        list_q = find_prime('q')
        while len(list_q) == 0:
            print('Chosen range has no prime number!')
            list_q = find_prime('q')
        list_q = list(list_q)
        q = list_q[random.randrange(0, len(list_q))]
        return q

    # n과 pi를 계산하는 함수
    def make_key(self, p, q):
        n = p * q
        pi = (p - 1) * (q - 1)
        return [n, pi]

    # pi와 서로소이면서 pi보다 작은 수들을 모두 구해서 그 중 임의의 값을 e로 지정하는 함수
    def find_e(self, pi):
        list_e = set({})
        for i in range(2, pi):
            if coprime(i, pi):
                list_e.add(i)
        list_e = list(list_e)
        e = list_e[random.randrange(0, len(list_e))]
        return e

    # (e*d) mod pi = 1 인 d를 구하는 함수
    def find_d(self, e, pi):
        d = []
        i = 1
        while len(d) == 0:
            if (i * e) % pi == 1:
                d.append(i)
            else:
                i += 1

        return d[0]


# 암호화를 진행하는 함수
def encrypt():
    rsa = RSA()
    p = rsa.make_p()
    q = rsa.make_q()
    [n, pi] = rsa.make_key(p, q)
    e = rsa.find_e(pi)
    d = rsa.find_d(e, pi)
    mesg = input('Write a message to Encrypt: ')
    log = "Encryping '" + mesg + "'"

    code = [ord(char) for char in mesg]
    crypto = []
    for m in code:
        c = squareAndMultiply(m, e, n)
        crypto.append(c)
    print('Public key: ' + str([e, n]))
    print('Private key: ' + str([d, n]))
    print('Encrypted message is', crypto)
    print()


# 복호화를 진행하는 함수
def decrypt(param):
    d = param["d"]
    n = param["n"]
    cipher = param["ciphertext"]
    return squareAndMultiply(cipher, d, n)
