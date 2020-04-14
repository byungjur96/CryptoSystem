from Module import RSA

def key_separator(algorithm):
    if algorithm == "RSA":
        return rsa_key()

def rsa_key():
    # p, q 생성과정 분리하기
    p = RSA.make_p(10**2)
    q = RSA.make_q(10**2)
    # p == q 인 경우 다시 q를 뽑는다.
    while p == q:
        q = RSA.make_q(10**2)
    [n, pi] = RSA.make_key(p, q)
    e = RSA.find_e(pi)
    d = RSA.find_d(e, pi)

    key = {
        "Public Key (e, n)": [e, n],
        "Private Key (d, n)": [d, n]
    }
    print(key)
    return key