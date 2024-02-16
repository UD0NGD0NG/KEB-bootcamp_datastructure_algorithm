def is_empty():
    global front, tail
    if front == tail:
        return True
    return False


def is_full():
    global size, tail
    if tail == size - 1:
        return True
    return False


def deQueue():
    global Queue, size, front, tail
    if is_empty():
        print("EMPTY")
    else:
        front += 1
        data = Queue[0]
        for i in range(size - 1):
            Queue[i] = Queue[i + 1]
        Queue[size - 1] = None
        return data


Queue = ['JK', 'V', 'JM', 'J', "SG"]
size = len(Queue)
front = -1
tail = 4

while not is_empty():
    print(f"Waiting line: {Queue}")
    data = deQueue()
    print(f"{data} is entrance")

print(f"Waiting line: {Queue}")
print("Restaurant closed!")
