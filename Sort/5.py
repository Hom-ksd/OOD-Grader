def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(lst_a,lst_b):
    index_a = 0
    index_b = 0
    result = []
    while index_a < len(lst_a) and index_b < len(lst_b):
        if lst_a[index_a] >= lst_b[index_b]:
            result.append(lst_a[index_a])
            index_a += 1
        else:
            result.append(lst_b[index_b])
            index_b += 1
    
    result.extend(lst_a[index_a:])
    result.extend(lst_b[index_b:])
    return result

datas = input("input : ").split()

datas = list(map(int,datas))

datas = [(datas[i],datas[i+1]) for i in range(0,len(datas),2)]

# print(datas)

sorted_Datas = merge_sort(datas)

# print(sorted_Datas)

ans = 0

for i in range(len(sorted_Datas) - 1):
    for j in range(i,len(sorted_Datas)):
            if sorted_Datas[i][1] < sorted_Datas[j][1]:
                ans += sorted_Datas[i][0] + sorted_Datas[j][0]

print(f"ans = {ans}")