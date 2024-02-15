def insert(position, friend, frequency):
    global kakao
    kakao.append(None)
    _len = len(kakao)

    for i in range(_len - 1, position, -1):
        kakao[i] = kakao[i - 1]

    kakao[position] = (friend, frequency)


kakao = [('DH', 200), ('JY', 150), ("ZW", 90), ('SN', 30), ('JH', 15)]
is_add = False

while (True):
    new_friend = input("friend to add--> ")

    if new_friend == 'Stop':
        break

    new_frequency = int(input("how many--> "))

    is_add = False
    for n in range(len(kakao)):
        if new_frequency >= kakao[n][1]:
            insert(n, new_friend, new_frequency)
            is_add = True
            break

    if not is_add:
        kakao.append((new_friend, new_frequency))

    print(kakao)
