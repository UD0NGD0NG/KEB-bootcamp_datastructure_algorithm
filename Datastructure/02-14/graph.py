class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print(' ', end="  ")
    for v in range(g.SIZE):
        print(v, end="  ")
    print()
    for row in range(g.SIZE):
        print(row, end="  ")
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()


G1, G2 = None, None

G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("## Undirected Graph ##")
printGraph(G1)

G2 = Graph(4)
G2.graph[0][1] = 1; G2.graph[0][2] = 1
G2.graph[3][0] = 1; G2.graph[3][2] = 1

print("## Directed Graph ##")
printGraph(G2)
