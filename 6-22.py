for i in range(1, 31):
    div3 = i % 3 == 0
    div5 = i % 5 == 0

    if div3 and div5:
        print("BINGO")
    elif div3:
        print("THREE")
    elif div5:
        print("FIVE")
    else:
        print(i)