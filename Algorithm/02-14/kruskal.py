class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print("   ", end=' ')
    for v in range(g.SIZE):
        print(name_ary[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(name_ary[row], end="  ")
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end="  ")
        print()
    print()


def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
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

    return findVtx in visitedAry


G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
CC, SL, SC, DJ, KJ, PS = 0, 1, 2, 3, 4, 5

gSize = 6
G1 = Graph(gSize)
G1.graph[CC][SL] = 10; G1.graph[CC][SC] = 15
G1.graph[SL][CC] = 10; G1.graph[SL][SC] = 40; G1.graph[SL][DJ] = 11; G1.graph[SL][KJ] = 50
G1.graph[SC][CC] = 15; G1.graph[SC][SL] = 40; G1.graph[SC][DJ] = 12
G1.graph[DJ][SL] = 11; G1.graph[DJ][SC] = 12; G1.graph[DJ][KJ] = 20; G1.graph[DJ][PS] = 30
G1.graph[KJ][SL] = 50; G1.graph[KJ][DJ] = 20; G1.graph[KJ][PS] = 25
G1.graph[PS][DJ] = 30; G1.graph[PS][KJ] = 25

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(G1)

edge_ary = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edge_ary.append([G1.graph[i][k], i, k])

edge_ary.sort(key=lambda data: data[0], reverse=True)

new_ary = []
for i in range(0, len(edge_ary), 2):
    new_ary.append(edge_ary[i])

index = 0
while len(new_ary) > gSize - 1:
    start = new_ary[index][1]
    end = new_ary[index][2]
    save_cost = new_ary[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN:
        del (new_ary[index])
    else:
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1

print('## 최소 비용의 자전거 도로 연결도 ##')
printGraph(G1)

cost = 0
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        cost += G1.graph[row][col]

print("최소 비용: ", end='')
print(cost // 2)
