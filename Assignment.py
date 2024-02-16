def notation(base, n):
    if n < base:
        print(numberChar[n], end='')
    else:
        notation(base, n // base)
        print(numberChar[n % base], end='')


def change(n):
    print("2 : ", end='')
    notation(2, n)

    print("\n8 : ", end='')
    notation(8, n)

    print("\n16 : ", end='')
    notation(16, n)


numberChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('decimal number -->'))
change(number)
