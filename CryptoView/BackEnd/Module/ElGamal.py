from Module.Tools.Calculator import squareAndMultiply, extendedEuclidean
import random


def decrypt(param):
    # ciphertext = (2909170161, 2565161545)
    # a = 37
    # p = 2934201397 -> p
    ciphertext = param["ciphertext"]
    a = param["a"]
    p = param["p"]
    xa = param["xa"]
    
    # find inverse of k
    k = squareAndMultiply(ciphertext[0], xa ,p)
    print(k)
    k_inverse = extendedEuclidean(k, p)[2]

    mesg = (ciphertext[1]*k_inverse) % p
    return mesg


def encrypt(param):
    ya = param["ya"] # 16
    p = param["p"] # 31
    a = param["a"] # 3
    mesg = param["plaintext"]  #15

    r = random.randrange(p)
    k = (ya ** r) % p
    c1 = (a ** r) % p
    c2 = (k*mesg) % p
    return [c1, c2]