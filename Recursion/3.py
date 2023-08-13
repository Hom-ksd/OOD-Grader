def power(a,b):
    if b == 0:
        return 1
    
    if b == 1:
        return a
    
    return a * power(a,b-1)

inp = input("Enter Input a b : ").split()

print(power(int(inp[0]),int(inp[1])))