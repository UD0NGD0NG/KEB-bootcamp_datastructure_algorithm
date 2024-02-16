def print_graph():
    global Graph, conveni

    print("     ", end="    ")
    for data in conveni:
        print(f"{data[0]}", end="   ")
    print()

    for row in range(len(conveni)):
        print(f"{conveni[row][0]:<8}", end='')
        for col in range(len(Graph[row])):
            print(f"{Graph[row][col]:>6}", end=' ')
        print()


Graph = [[0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1],
         [0, 0, 0, 1, 0]]
conveni = [["GS25", 30], ["CU", 60], ["Seven11", 10], ["MiniStop", 90], ["Emart24", 40]]

max = conveni[0]
for data in conveni:
    if max[1] < data[1]:
        max = data

print_graph()
print(f"max conveni: {max[0]}, max count: {max[1]}")
