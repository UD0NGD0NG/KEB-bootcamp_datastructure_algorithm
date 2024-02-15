import random


def bubble_sort(arr):
    n = len(arr)
    for end in range(n - 1, 0, -1):
        is_changed = False
        for cur in range(end):
            if arr[cur] > arr[cur + 1]:
                arr[cur], arr[cur + 1] = arr[cur + 1], arr[cur]
                is_changed = True
        if not is_changed:
            break
    return arr


data_arr = [random.randint(0, 200) for _ in range(20)]


print(f"before sorting: {data_arr}")
bubble_sort(data_arr)
print(f"after sorting: {data_arr}")
