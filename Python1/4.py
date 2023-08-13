def add_bomb(lst,i,j):
    if i - 1 >= 0 and j - 1 >= 0:
        if lst[i - 1][j - 1] != '#':
            lst[i - 1][j - 1] += 1
    
    if i - 1 >= 0:
        if lst[i - 1][j] != '#':
            lst[i - 1][j] += 1
            
    if i - 1 >= 0 and j + 1 < len(lst[i]):
        if lst[i - 1][j + 1] != '#':
            lst[i - 1][j + 1] += 1
    
    
    if i >= 0 and j - 1 >= 0:
        if lst[i][j - 1] != '#':
            lst[i][j - 1] += 1

    if i >= 0 and j + 1 < len(lst[i]):
        if lst[i][j + 1] != '#':
            lst[i][j + 1] += 1

    if i + 1 < len(lst) and j - 1 >= 0:
        if lst[i + 1][j - 1] != '#':
            lst[i + 1][j - 1] += 1

    if i + 1 < len(lst):
        if lst[i + 1][j] != '#':
            lst[i + 1][j] += 1
            
    if i + 1 < len(lst) and j + 1 < len(lst[i]):
        if lst[i + 1][j + 1] != '#': 
            lst[i + 1][j + 1] += 1

    return lst

def num_grid(lst):

    for i in range(len(lst)):
    #    print(lst[i])
       for j in range(len(lst[i])):
            if lst[i][j] == '-':
                lst[i][j] = 0

    for i in range(len(lst)):
    #    print(lst[i])
       for j in range(len(lst[i])):
            if lst[i][j] == '#':
                add_bomb(lst,i,j)

    for i in range(len(lst)):
    #    print(lst[i])
       for j in range(len(lst[i])):
            if type(lst[i][j]) != "#":
                lst[i][j] = str(lst[i][j]) 

    return lst


'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

print("*** Minesweeper ***")


lst_input = []

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")

