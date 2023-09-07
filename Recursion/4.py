def check_left(lst,target,data):
    if target < 0 or target >= len(lst):
        return 0
    
    if lst[target] != data:
        return 0
    
    return 1 + check_left(lst,target-1,data)

def check_right(lst,target,data):
    if target < 0 or target >= len(lst):
        return 0
    
    if lst[target] != data:
        return 0
    
    return  1 + check_right(lst,target+1,data)

data,target = input("input number : ").split(",")
# 111112211002111,2
# 5
target = int(target) - 1
if data == "":
    print("Output : List is entry")
elif target >= len(data):
    print("Output : Pin number out of range")
elif target < 1:
    print("Output : Pin number less than 1")    
else:
    print("Character :",data[target])
    print("Count :",check_left(data,target,data[target]) + check_right(data,target + 1,data[target]))