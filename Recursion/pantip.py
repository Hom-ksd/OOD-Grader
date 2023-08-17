def pantip(k, n, arr, path):
    if k == 0:
        print(*path, " ")
        return 1
    elif n == len(arr) or k < 0:
        return 0
    
    size = pantip(k - arr[n], n + 1,arr, path + [arr[n]])
    size2 = pantip(k,n+1,arr,path) 

    # size = 0
    # for i in range(len(arr)):
        # new_path = path
        # new_path.append(arr[i])
        # new_arr = arr[i+1:]
        # size += pantip(k,n+arr[i],new_arr,new_path) 
        # new_path.pop(-1)

    return size+size2
    

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print(f"{arr} {inp[0]} {pattern}") 