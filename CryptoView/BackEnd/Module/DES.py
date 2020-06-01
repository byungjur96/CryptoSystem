ip_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 45, 33, 25, 17, 9, 1,
    59, 51, 47, 35, 27, 19, 11, 3,
    61, 53, 49, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

reverse_ip_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

expanded_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17, 
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

pc1 = [
    57, 49, 41, 33, 25, 17,  9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
	]

pc2 = [
		14, 17, 11, 24, 1, 5,
		3, 28, 15, 6, 21, 10,
		23, 19, 12, 4, 26, 8,
		16, 7, 27, 20, 13, 2,
		41, 52, 31, 37, 47, 55,
		30, 40, 51, 45, 33, 48,
		44, 49, 39, 56, 34, 53,
		46, 42, 50, 36, 29, 32
	]

S_BOX = [     
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


def initial_permutation(string):
    result = ""
    for i in range(64):
        result += (string[ip_table[i]-1])
    return result

def xor(a, b):
    result = ""
    try:
        if len(a) != len(b):
            raise Exception("Input의 길이가 동일하지 않습니다.")
    except Exception as e:
        print(e)
    
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def f_func(r, key):
    expanded = ""
    result = ""
    for i in range(48):
        expanded += r[expanded_table[i] - 1]
    val = xor(expanded, key)
    for i in range(8):
        temp = val[i*6:(i+1)*6]
        column = int("0b"+temp[0]+temp[5], 2)
        row = int("0b"+temp[1:5], 2)
        result += bin(S_BOX[i][column-1][row-1])[2:].zfill(4)
    return result

# key: 7자리의 string
def make_key(key):
    key_set = []  # 만들어진 키를 저장하는 list
    whole_key = ""  # parity bit가 추가된 64 bit의 키
    ascii_key = ""  # 56 bit의 키
    # 7자리의 string으로된 key를 56 bit의 이진수로 바꾼다
    for k in key:
        ascii_key += bin(ord(k))[2:].zfill(8)
    # 56 bit의 key에 parity bit를 추가하여 64 bit로 만든다
    for i in range(8):
        val = ascii_key[i*7:(i+1)*7]
        if val.count("1") % 2 == 0:
            val+="0"
        else:
            val+="1"
        whole_key += val
    # PC-1 전치를 진행한다
    permuted_1 = ""
    for i in range(56):
        permuted_1 += whole_key[pc1[i] - 1]
    left = permuted_1[:28]
    right = permuted_1[28:]
    for i in range(16):
        # 1, 2, 9, 16 번째이면 left shift를 1번 실행한다
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = left[1:] + left[0]
            right = right[1:] + right[0]
        # 그 이외의 경우에는 left shift를 2번 실행한다
        else:
            left = left[2:] + left[:2]
            right = right[2:] + right[:2]
        
        merged = left + right
        subkey = ""
        for i in range(48):
            subkey += merged[pc2[i] - 1]
        key_set.append(subkey)
        left = merged[:24]
        right = merged[24:]
    return key_set


def mesg_bit(string):
    result = []
    while len(string) > 8:
        target = string[:8]
        string = string[8:]
        block = ""
        for t in target:
            block+=(bin(ord(t))[2:].zfill(8))
        result.append(block)
    string.zfill(8)
    last = ""
    for s in string:
        last+=(bin(ord(s))[2:].zfill(8))
    result.append(last.zfill(64))
    return result

def reverse_ip(string):
    result = ""
    for i in range(64):
        result += string[reverse_ip_table[i]-1]
    return string

def encrypt_block(left, right, key):
    after_f = f_func(right, key)
    return right, after_f

def encrypt(param):
    mesg = param["plaintext"]
    key = param["key"]
    cipher = ""
    key_list = make_key(key)
    mesg_block = mesg_bit(mesg)
    for block in mesg_block:
        swapped_mesg = initial_permutation(block)
        l, r = swapped_mesg[:32], swapped_mesg[32:]
        for i in range(16):
            l, r = encrypt_block(l, r, key_list[i])
        bin_cipher = reverse_ip(l+r)
        for i in range(len(bin_cipher)//8):
            input_bin = int(bin_cipher[i*8:(i+1)*8],2)
            cipher += chr(input_bin)
    return cipher
    
def decrypt():
    return
