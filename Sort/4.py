l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "merge sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    datas = []
    print_data = []
    for data in l:
        datas.append(data)
        print_data.append(data)
        back = len(datas) - 1
        for i in range(len(datas) - 1):
            min_index = i
            for j in range(i + 1,len(datas)):
                if datas[j] < datas[min_index]:
                    min_index = j
            if min_index != i:
                datas[min_index],datas[i] = datas[i],datas[min_index]
        if len(datas) % 2 == 0:
            mean = datas[len(datas)//2 - 1] + datas[len(datas)//2]
            mean /= 2
        else:
            mean = datas[len(datas)//2]
        string = ", ".join(str(x) for x in print_data)
        print(f"list = [{string}] : median = {mean:.1f}")
            
            