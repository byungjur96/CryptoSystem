import random
from time import sleep
import sys
import math


# Extended Euclidean Algorithm
def extendedEuclidean(a, b):
    i = 1
    history = [
        [None, a, 1, 0],
        [None, b, 0, 1]
    ]
    while history[i][1] != 0:
        q = history[i-1][1] // history[i][1]
        r = history[i-1][1] % history[i][1]
        s = history[i-1][2] - history[i][2] * q
        t = history[i-1][3] - history[i][3] * q
        history.append([q, r, s, t])
        i += 1
    return history[i-1]


# Square-and-Multiply Algorithm
def squareAndMultiply(a, e, n):
    bin_e = bin(e)[2:]
    b = 1
    for i in range(0, len(bin_e)):
        b = (b*b) % n
        if bin_e[i] == '1':
            b = (b*a) % n
    return b


def main():
    q = 2934201397
    a = 37
    ya = 2174919958
    ciphertext = (2909170161, 2565161545)
    xa = 0
    cal_ya = 1
    while cal_ya != ya:
        xa += 1
        cal_ya = (cal_ya * a) % q
    print('xa is {}.'.format(xa))

    k = squareAndMultiply(ciphertext[0], xa ,q)
    print('k is {}.'.format(k))
    k_inverse = extendedEuclidean(k, q)[2]
    print('k_inverse is {}.'.format(k_inverse))
    print()

    m = (ciphertext[1]*k_inverse) % q
    print('Plaintext for {} is {}'.format(ciphertext, m))


if __name__ == '__main__':
    main()
