class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_arr(Head):
    print(Head.data, end='')
    while Head.link is not None:
        Head = Head.link
        print(Head.data, end='')
    print()


current = None

name = input("Name--> ")
while name != '':
    mail = input("Mail--> ")

    new_node = Node()
    new_node.data = [name, mail]

    if current is not None:
        new_node.link = current
    current = new_node
    print_arr(current)

    name = input("Name--> ")
