import random


class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current.link is None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node
    node.link = head


def classify(data):
    global head, current

    odd_cnt = 0
    even_cnt = 0

    for num in data:
        if num % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

    print(f"홀수: {odd_cnt}, 짝수: {even_cnt}")

    current = head
    if even_cnt > odd_cnt:
        if current.data % 2 == 0:  # There is no "do-while" in Python.
            current.data *= -1
        current = current.link
        while current != head:
            if current.data % 2 == 0:
                current.data *= -1
            current = current.link
    else:
        if current.data % 2 == 1:
            current.data *= -1
        current = current.link
        while current != head:
            if current.data % 2 == 1:
                current.data *= -1
            current = current.link


head, current, pre = None, None, None
data_array = [random.randint(1, 100) for n in range(7)]

if __name__ == "__main__":

    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_nodes(head)
    classify(data_array)
    print_nodes(head)
