S = []

Data = input("Data : ").split()

Data = list(map(int,Data))

result = []

max_size = 0


for i in range(len(Data)):
    if not result:
        result.append(Data[i])
    else:
        while(result and Data[i] <= result[-1]):
            result.pop(-1)
        result.append(Data[i])
    print(i + 1 ,":",result)
    max_size = max(max_size,len(result))
print(f"longest increasing subsequence : {max_size}")