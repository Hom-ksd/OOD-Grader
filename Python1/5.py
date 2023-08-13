n = int(input("Enter Input : "))
yini,yinj = n + 3, 1
yangi,yangj = 1 , n + 3
back = n * 2 + 3
for i in range(n * 2 + 4):
    for j in range(n * 2 + 4):
        if (i >= yini and i <= yini + n - 1) and (j >= yinj and j <= yinj + n - 1):
            print("+",end="")
        elif (i >= yangi and i <= yangi + n - 1) and (j >= yangj and j <= yangj + n - 1):
            print("#",end="")
        elif (j <= n - i) and (i <= n):
            print(".",end="")
        elif (j >= back) and (i >= n + 3):
            print(".",end="")
        elif(j >= n - i and j <= n + 1):
            print("#",end="")
        elif(j > n + 1):
            print("+",end="")
        else: print(j,end=" ")
    print()
    if i >= n + 3:
        back -= 1

# 4 1

# 5 1 
# 6 2