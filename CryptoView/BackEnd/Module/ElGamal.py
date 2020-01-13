from Tools.Calculator import squareAndMultiply, extendedEuclidean

def decrypt(param):
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

