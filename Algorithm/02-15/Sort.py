import random


def findInsertIdx(ary, data):
    find_idx = -1
    for i in range(0, len(ary)):
        if ary[i] > data:
            find_idx = i
            break
    if find_idx == -1:
        return len(ary)
    else:
        return find_idx


before = [random.randint(1, 200) for _ in range(10)]
after = []

print('정렬 전 -->', before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 -->', after)
