import time
import random

a_list = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

# 범위의 값이 소수인지 빠르게 확인한다.
def make_prime(maximum):
    lst = []
    for i in range(2, maximum + 1):
        if miller_rabin_test(i, maximum):
            lst.append(i)
    ans = random.choice(lst)
    while not prime_check(ans):
        ans = random.choice(lst)
    return ans

# 값이 소수인지 판별하는 함수
def prime_check(val):
    result = list()
    state = True
    for i in range(2, val):
        if val % i == 0:
            state = False
            break
    return state

# 밀러 라빈 소수 판정법을 통해 빠르게 pseudo-prime 여부를 확인한다.
def miller_rabin_test(n, maximum_range):
    # n이 2인 경우 참을 반환한다.
    if n == 2:
        return True
    # n이 2가 아닌 짝수인 경우 거짓을 반환한다.
    elif n % 2 == 0:
        return False
    # n이 홀수인 경우 테스트를 진행한다.
    else:
        d = n - 1
        s = 0
    while d % 2 == 1:
        s += 1
        d // 2

    for a in a_list:
        if squareAndMultiply(a, d, n) != 1:
            return False
    for i in range(15):
        a = random.randrange(1,maximum_range)
        if squareAndMultiply(a, d, n) != 1:
            return False
    for r in range(s-1):
        for a in a_list:
            if squareAndMultiply(a, d*(2**r), n) != -1:
                return False
        for i in range(15):
            a = random.randrange(1,maximum_range)
            if squareAndMultiply(a, d, n) != 1:
                return False
    return True

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