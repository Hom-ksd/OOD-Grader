n = int(input("Enter Input : "))
maxsize = n

tower = {0 : 'A',
         1 : 'B',
         2 : 'C'}

def create_list(n):
    if n == 1:
        return [1]
    else:
        return [n] + create_list(n-1)

def print_list(lst,size):
    if size == 1:
        if lst[0] :
            print(lst[0][0],end="  ")
        else:
            print("|  ",end="")
        if lst[1]:
            print(lst[1][0],end="  ")
        else:
            print("|  ",end="")
        if lst[2]:
            print(lst[2][0])
        else:
            print("|")
    else:
        if len(lst[0]) < size:
            print('|  ',end="")
        else:
            print(lst[0][size - 1],end="  ")

        if len(lst[1]) < size:
            print('|  ',end="")
        else:
            print(lst[1][size - 1],end="  ")

        if len(lst[2]) < size:
            print('|')
        else:
            print(lst[2][size - 1])
        
        print_list(lst,size-1)

def move(n, start, target, base, lst):
    if n == 1:
        print("move",n,"from ",tower[start], "to" ,tower[target])
        lst[target].append(lst[start].pop(-1))
        print_list(lst,maxsize + 1)
    else:
        move(n - 1, start, base, target, lst)
        print("move",n,"from ",tower[start], "to" ,tower[target])
        lst[target].append(lst[start].pop(-1))
        print_list(lst,maxsize + 1)
        move(n - 1, base, target, start, lst)

if n > 0 :
    lst = create_list(n)
    hanoi = [lst,[],[]]
    print_list(hanoi,maxsize + 1)
    move(n,0,2,1,hanoi)
