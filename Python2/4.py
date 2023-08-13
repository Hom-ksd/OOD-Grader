def find_base(nums) :
    n = 3
    while(True):
        # print(n)
        check20 = convert_to_base(20,n)
        check21 = convert_to_base(21,n)
        # print(check20, check21)
        if check20 == nums:
            print(f"saimai is just 20, in base {n}!")
            break
        elif check21 == nums:
            return f"saimai is just 21, in base {n}!"
            break
        n += 1
        
def convert_to_base(nums,base):
    digits = 0
    return_ans = 0
    for num in reversed(str(nums)):
        return_ans += int(num) * (base ** digits)
        digits += 1        
    #print(return_ans)
    return int(return_ans)

year = int(input("Enter year : "))

# print(convert_to_base(21,3))

find_base(year)