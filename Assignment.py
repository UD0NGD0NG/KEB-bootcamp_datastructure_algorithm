import random


class Node:
    def __init__(self):
        self.data = None
        self.link = None


def insert_node(_head, _data):
    global cnt, head

    if _head.link is None:
        if _head.data == _data:
            pass
        elif _data < _head.data:
            new_node = Node()
            new_node.data = _data
            new_node.link = _head
            head = new_node
            cnt += 1
        else:
            new_node = Node()
            new_node.data = _data
            _head.link = new_node
            cnt += 1

    else:
        while _head.link is not None:
            if _data == _head.data:
                break

            if _data < _head.data:
                new_node = Node()
                new_node.data = _data
                new_node.link = _head
                if head == _head:
                    head = new_node
                cnt += 1
                break
            else:
                if _data < _head.link.data:
                    new_node = Node()
                    new_node.data = _data
                    new_node.link = _head.link
                    _head.link = new_node
                    cnt += 1
                    break
                else:
                    _head = _head.link


def print_list(_head):
    print(_head.data, end=' ')
    while _head.link is not None:
        _head = _head.link
        print(_head.data, end=' ')


new_node = Node()
new_node.data = random.randint(1, 45)
head = new_node
cnt = 1

while cnt != 6:
    new_data = random.randint(1, 45)
    insert_node(head, new_data)

print_list(head)
