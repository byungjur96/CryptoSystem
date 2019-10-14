class DES:
    def initial_permutation(inputblock):
        table = [
            [58, 50, 42, 34, 26, 18, 10, 2],
            [60, 52, 44, 36, 28, 20, 12, 4],
            [62, 54, 46, 38, 30, 22, 14, 6],
            [64, 56, 48, 40, 32, 24, 16, 8],
            [57, 49, 45, 33, 25, 17, 9, 1],
            [59, 51, 47, 35, 27, 19, 11, 3],
            [61, 53, 49, 37, 29, 21, 13, 5],
            [63, 55, 47, 39, 31, 23, 15, 7]
        ]
        result = ''
        for i in range(64):
            print(table[int(i//8)][i % 8])
            #result+=inputblock[int(i//8)][i%8]

    def make_sub_key(self):
        return


def encrypt():
    DES.initial_permutation('test')
    for i in range(16):
        return


def decrypt():
    return

def main():
    option = -1
    while option != '0':
        print("<Option>")
        print("1. Encrypt")
        print("2. Decrypt")
        print("Enter '0' to exit")
        option = input('Enter Option: ')
        if option == '1':
            encrypt()
        elif option == '2':
            decrypt()
        elif option == '0':
            print('End this Program')
        else:
            print('Wrong Option! Try again')

if __name__ == '__main__':
    main()
