def staircase(n):
    if n == 0:
        return "Not Draw!"
    if n < 0:
        size = -n
    else:
        size = n
    print_stair(size,n)
    return ""

def print_stair(size,n):
    if n == 1 or n == -1:
        str = "_"*(size-1) + "#"
        print(str)
        return
    if n > 0:
        str = "_"*(size-n) + "#"*n
        print_stair(size,n-1)
        print(str)
    elif n < 0:
        str = "_"*(size+n) + "#"*-n
        print(str)
        print_stair(size,n+1)

print(staircase(int(input("Enter Input : "))))