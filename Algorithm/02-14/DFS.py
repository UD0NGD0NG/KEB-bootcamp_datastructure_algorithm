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


G1 = None
stack = []
visitedAry = []

G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("## Undirected Graph ##")
printGraph(G1)

current = 0
stack.append(current)
visitedAry.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문 순서 -->', end=' ')
for i in visitedAry:
    print(chr(ord('A') + i), end=" ")
