check = []

def permute(nums,current = []):
    if len(nums) == 0:
        if current not in check:
            print(current)
            check.append(current)
    else:
        for i in range(len(nums)-1,-1,-1):
            new_nums = nums[:i] + nums[i+1:]
            permute(new_nums,current + [nums[i]])

def permu(inp):
    if len(inp) == 1:
        return [inp]
    all = permu(inp[1:])
    res = []
    for sub_list in all:
        for i in range(len(inp) ):
            res.append(sub_list[:i] + [inp[0]] + sub_list[i:])
    return res

nums = [1,2,3]
nums.reverse()

print(permu(nums))


# nums = [1,2,3]
# permute(nums)

# 1 2 3
# 2 3
# 3
# in 2 3 all = [ 3 ] 
# for i in all{ [ 3 ] }
# for j in 2 { 2 , 3 }
#  res.append( [ 2 , 3 ] )
#  res.append( [ 3 , 2 ] )
# res = [ [2,3] , [3,2] ]
# in 1 2 3 all = [ [2,3] , [3,2] ]
# for i in all [ [2,3] , [3,2] ]
# for j in 3
#  i = [2 , 3]
#  res.append( [ 1 , 2 , 3 ] )
#  res.append( [ 2 , 1 , 3 ] )
#  res.append( [ 2 , 3 , 1 ] )
#  i = [3 , 2]
#  res.append( [ 1 , 3 , 2 ] )
#  res.append( [ 3 , 1 , 2 ] )
#  res.append( [ 3 , 2 , 1 ] )