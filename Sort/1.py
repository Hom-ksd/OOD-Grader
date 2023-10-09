inp = input("Enter Input : ").split()

datas = list(map(int,inp))

for i in range(len(datas),1,-1):
    isMove = False
    m = -1
    for j in range(i - 1):
        if datas[j] > datas[j + 1]:
            if m < datas[j]:
                m = datas[j]
            datas[j],datas[j + 1] = datas[j + 1],datas[j]
            isMove = True
    string = ", ".join(str(data) for data in datas)
    if i == 2 and isMove:
        print(f"last step : [{string}] move[{m}]")
        break
    elif isMove :
        print(f"{len(datas) - i + 1} step : [{string}] move[{m}]")
    else:
        print(f"last step : [{string}] move[None]")
        break
# print(datas)