def BiS(start,end,arr,target):
    print(start,end)
    if end < start:
        return -1
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    
    if target > arr[mid] :
        return BiS(mid + 1,end,arr,target)
    else:
        return BiS(start,mid - 1,arr,target)


lst = [1,2,3,4,5,6,7,8,9,10]

print(BiS(0,len(lst) - 1,lst,7))