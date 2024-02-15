def printPoly(t_x, p_x):
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        degree = t_x[i]  # 항 차수
        coefficient = p_x[i]  # 계수

        if coefficient >= 0:
            polyStr += "+"
        polyStr += str(coefficient) + "x^" + str(degree) + " "

    return polyStr


def calcPoly(x_val, _x):
    retValue = 0

    for i in range(len(_x[0])):
        degree = _x[0][i]
        coefficient = _x[1][i]
        retValue += coefficient * x_val ** degree

    return retValue


x = [[300, 20, 0],
     [7, -4, 5]]

if __name__ == "__main__":
    pStr = printPoly(x[0], x[1])
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, x)
    print(pxValue)
