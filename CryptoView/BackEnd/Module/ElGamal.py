from Module.Tools.Calculator import squareAndMultiply, extendedEuclidean

def decrypt(param):
    q = 2934201397
    a = 37
    ya = 2174919958
    ciphertext = (2909170161, 2565161545)
    xa = 0
    cal_ya = 1
    # Find xa
    while cal_ya != ya:
        xa += 1
        cal_ya = (cal_ya * a) % q

    # find inverse of k
    k = squareAndMultiply(ciphertext[0], xa ,q)
    k_inverse = extendedEuclidean(k, q)[2]

    m = (ciphertext[1]*k_inverse) % q
