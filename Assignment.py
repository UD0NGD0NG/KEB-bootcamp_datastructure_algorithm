def is_full():
    global top, size
    if top >= size - 1:
        return True
    return False


def is_empty():
    global size
    if top == -1:
        return True
    return False


def push(data):
    global Stack, top, size

    if is_full():
        print("FULL")
    else:
        top += 1
        Stack[top] = data


def pop():
    global Stack, top, size
    if is_empty():
        print("EMPTY")
    else:
        print(Stack[top], end='')
        Stack[top] = None
        top -= 1


Stack = [None, None, None, None, None, None]
top = -1
size = 6


print("Go to snack house: ", end='')
while not is_full():
    stone = input()
    push(stone)
    print("-->", end='')
print("snack house")

print("Go to my home: ", end='')
while not is_empty():
    pop()
    print("-->", end='')
print("my home")
