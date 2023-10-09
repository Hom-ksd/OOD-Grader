def findMaxInRow(Map,Row):
    mx = -1
    index = -1
    for i in range(len(Map[Row])):
        if mx < Map[Row][i]:
            mx = Map[Row][i]
            index = i
    return index

def findMaxInColumn(Map,Column):
    mx = -1
    for i in range(len(Map)):
        # print(Map[i][Column])
        if mx < Map[i][Column]:
            mx = Map[i][Column]
    return mx


mn = 1e9
min_index = [-1,-1]

size,Data = input("input : ").split(",")

size = size.split()
Data = Data.split()

size = list(map(int,size))
Data = list(map(int,Data))

Map = []

for i in range(size[0]):
    Map.append([])
    for j in range(size[1]):
        Map[i].append(Data[size[0] * i + j])
        if mn > Map[i][j]:
            mn = Map[i][j]
            min_index[0] = i
            min_index[1] = j

print(findMaxInColumn(Map,findMaxInRow(Map,min_index[0])))
