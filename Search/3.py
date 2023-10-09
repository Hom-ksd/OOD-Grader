def findSqrt(num,precision = 1e-5):
    if num < 0:
        return
    
    if num == 0 or num == 1:
        return num
    
    left,right = 0,num

    while right - left > precision:
        mid = (left + right) / 2
        result = mid * mid
        if result == num:
            return mid
        elif result < num:
            left = mid
        else:
            right = mid
    
    return (left + right) // 2
        

num = int(input("simple sqrt: "))

print(f"{findSqrt(num):.0f}")