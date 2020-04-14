# 범위 내의 소수를 모두 구하는 함수
def find_prime(maximum):
    result = list()
    for n in range(2, maximum):
        state = True
        for i in range(2, n):
            if n % i == 0:
                state = False
                break
        if state:
            result.append(n)
    return result

# 최대공약수를 구하는 함수
def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)

# 서로소를 구하는 함수
def coprime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False

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