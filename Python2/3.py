print("*** Odd Even ***")

d_type,data,pos = input("Enter Input : ").split(",")
if d_type == 'L':
    lst = data.split()
    ans = []
    if pos == "Odd":
        for i in range(0,len(lst),2):
            ans.append(lst[i])
    elif pos == 'Even':
        for i in range(1,len(lst),2):
            ans.append(lst[i])
    print(ans)
elif d_type == 'S':
    if pos == "Odd":
        ans = data[::2]
    elif pos == "Even":
        ans = data [1::2]
    print(ans)