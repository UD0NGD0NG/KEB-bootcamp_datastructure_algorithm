class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print(' ', end="  ")
    for v in range(g.SIZE):
        print(chr(ord('A') + v), end="  ")
    print()
    for row in range(g.SIZE):
        print(chr(ord('A') + row), end="  ")
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()


G = None
stack = []
visited_ary = []

G = Graph(4)
G.graph[0][2] = 1; G.graph[0][3] = 1
G.graph[1][2] = 1
G.graph[2][0] = 1; G.graph[2][1] = 1; G.graph[2][3] = 1
G.graph[3][0] = 1; G.graph[3][2] = 1

print("## Undirected Graph ##")
printGraph(G)

current = 0
stack.append(current)
visited_ary.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(4):
        if G.graph[current][vertex] == 1:
            if vertex in visited_ary:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        stack.append(current)
        visited_ary.append(current)
    else:
        current = stack.pop()

print('방문 순서 -->', end=' ')
for i in visited_ary:
    print(chr(ord('A') + i), end=" ")
