# by loop
# def factorial(number) -> int:
#     """
#     factorial by repetition
#     :param number: number (int)
#     :return: factorial result (int)
#     """
#     result = 1
#     for i in range(1, number+1):
#         result = result * i
#     return result


# by recursion
def factorial(number) -> int:
    """
    factorial by recursion
    :param number: number (int)
    :return: factorial result (int)
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":
    # n = int(input("Input n : "))
    # r = int(input("Input r : "))
    # print(f"{n}C{r} = {nCr(n, r)}")
    f = int(input())
    print(factorial(f))
