def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)


def fibo_iterative(number: int) -> int:
    a = 0
    b = 1
    for i in range(number):
        a, b = b, a + b
    return a


memo = [None for _ in range(100)]
def fibo_memoization(number: int, memo) -> int:
    """
    fibonacci function by recursion with memoization
    :param number: integer number
    :return: integer number
    """
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number - 1, memo) + fibo_memoization(number - 2, memo)
        memo[number] = result
    return result


print('피보나치 수 --> ', end='')
for i in range(0, 40):
    print(fibo_recursion(i), end=' ')

print('\n피보나치 수 --> ', end='')
for i in range(0, 40):
    print(fibo_iterative(i), end=' ')

print('\n피보나치 수 --> ', end='')
for i in range(0, 40):
    print(fibo_memoization(i, memo), end=' ')
