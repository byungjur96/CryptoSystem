from Tools.BaseChange import *

Sbox = [
            ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
            ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
            ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
            ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
            ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
            ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
            ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
            ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
            ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
            ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
            ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
            ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
            ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
            ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
            ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
            ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
        ]

mix = [
		[2, 3, 1, 1],
		[1, 2, 3, 1],
		[1, 1, 2, 3],
		[3, 1, 1, 2]
	]

P = "000102030405060708090A0B0C0D0E0F"
K = "01010101010101010101010101010101"

def printhex(a):
	for i in range(len(a)):
		if i % 4 == 3:
			print(a[i], end=" ")
		else:
			print(a[i], end="")

def dimension(a):
	return [a[0:4], a[4:8], a[8:12], a[12:16]]

def hextotable(a):
	text_len = len(a) // 2
	result = []
	for i in range(text_len):
		val = ""
		for j in range(2):
			val += a[2 * i + j]
		result.append(val)
	return result	

def addRoundKey(a, b):
	key_len = len(a)
	result = ""
	for i in range(key_len):
		if a[i] == b[i]:
			result += "0"
		else:
			result += "1"
	return bitohex(result)

def subBytes(a):
	result = ""
	text_len = len(a) // 2
	for i in range(text_len):
		temp = []
		for j in range(2):
			if ord('A') <= ord(a[2 * i + j]) <= ord('F'):
				temp.append(ord(a[2 * i + j]) - ord('A') + 10)
			else:
				temp.append(int(a[2 * i + j]))
		result += Sbox[temp[0]][temp[1]]
	return result

def xor(a, b):
	result = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			result += '0'
		else:
			result += "1"
	return result

def rotate(a):
	return [
		[a[0], a[4], a[8], a[12]], 
		[a[1], a[5], a[9], a[13]], 
		[a[2], a[6], a[10], a[14]], 
		[a[3], a[7], a[11], a[15]]
	]

def shiftRows(a):
	res = rotate(a)
	return [
		res[0],
		res[1][1:] + res[1][:1],
		res[2][2:] + res[2][:2],
		res[3][3:] + res[3][:3]
		]

def mixCal(a, b):
	if b == 1:
		return a
	elif b == 2:
		return (a+'0')[-8:]
	else:
		return xor(a, (a+'0')[-8:])

def mixColumns(a):
	result = [[], [], [], []]
	# input의 column이면서 output의 row
	for i in range(4):
		# mix의 row이면서 output의 column
		for j in range(4):
			temp_val = '00000000'
			for k in range(4):
				temp_bi = mixCal(hextobi(a[k][i]), mix[j][k])
				temp_val = xor(temp_val, temp_bi)

			temp_val = bitohex(xor(temp_val,'00011011'))
			result[j].append(temp_val)
	return result

def main():
	bi_p = hextobi(P)
	bi_k = hextobi(K)

	# AddRoundKey
	text = addRoundKey(bi_p, bi_k)
	
	# SubstituteByte
	text = subBytes(text)
	
	# ShiftRows
	text = hextotable(text)
	text = shiftRows(text)
	
	# MixColumns
	result = mixColumns(text)
	for i in result:
		print(i)
	

if __name__ == '__main__':
	main()
