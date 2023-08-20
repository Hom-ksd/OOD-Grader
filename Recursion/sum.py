answer = []
def ssum(target,number,path):
    # print(target,number,path)
    if target == 0:
        print(path)
        temp = path.copy()
        answer.append(temp)
        return 
    elif target < 0:
        return 

    if number <= 0:
        return 
    
    path.append(number)
    r1 = ssum(target - number,number,path)
    path.pop(-1)
    r2 = ssum(target,number - 1,path)


n = int(input())

print(ssum(n,n,[]))
print(answer)