def sort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_half = sort(left_half)
    right_half = sort(right_half)

    return merge(left_half,right_half)



def merge(left,right):
    result = []
    left_idx,right_idx = 0,0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] >= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

inp = input("Enter your List : ").split(",")
inp = [int(x) for x in inp]
print("List after Sorted :",sort(inp))