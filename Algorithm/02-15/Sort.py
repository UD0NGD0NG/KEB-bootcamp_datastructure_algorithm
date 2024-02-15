import random


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = arr[n // 2]
    left, right = [], []

    for num in arr:
        if num < mid:
            left.append(num)
        elif num > mid:
            right.append(num)

    return quick_sort(left) + [mid] + quick_sort(right)


data_ary = [random.randint(0, 200) for _ in range(20)]

print('정렬 전 -->', data_ary)
data_ary = quick_sort(data_ary)
print('정렬 후 -->', data_ary)
