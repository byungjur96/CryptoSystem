"""
    진법을 바꾼다.
        - 2진수: string
        - 10진수: integer
        - 16진수: string
"""
# 2진수를 16진수로 바꾼다.
def bitohex(string):
    result = ""
    string_len = len(string)
    if string_len % 4 != 0:
        string_len += 4
        for k in range(4 - (string_len % 4)):
            string = '0' + string
    print(string)
    print(string_len)
    for i in range(string_len // 4):
        temp = 0
        for k in range(4):
            temp += (int(string[4*i + k])*(2**(3-k)))
        if temp > 9:
            temp = chr(ord('A')+ temp - 10)
        else:
            temp = str(temp)
        result += temp
    return result

# 10진수를 16진수로 바꾼다.
def dectohex(num):
    result = ""
    while num != 0:
        if num % 16 > 9:
            temp = chr(ord('A') + num % 16 - 10)
        else:
            temp = str(num % 16)
        num = num // 16
        print(temp)
        result = temp + result
    return result

# 16진수를 2진수로 바꾼다.
def hextobi(string):
    result = ""
    for i in range(len(string)):
        value = ""
        if ord('A') <= ord(string[i]) <= ord('F'):
            target = ord(string[i]) - ord('A') + 10
        else:
            target = int(string[i])
        for k in range(4):
            if target % 2 == 1:
                value = "1" + value
            else:
                value = "0" + value
            target = target // 2
        result += value
    return result

# 16진수를 10진수로 바꾼다.
def hextodec(string):
    result = 0
    string_len = len(string)
    for j in range(string_len):
        if ord('A') <= ord(string[j]) <= ord('F'):
                result += (ord(string[j]) - ord('A') + 10) * (16 ** (string_len - j - 1))
        else:
            result += (int(string[j])) * (16 ** (string_len - j - 1))
    return result

