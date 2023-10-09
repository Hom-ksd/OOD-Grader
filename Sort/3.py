# หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"
# หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"
# หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"
# หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"
# หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"
# หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

def Metadrome(lst):
    if lst:
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True
    return False

def Plaindrome(lst):
    if lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    return False

def Katadrome(lst):
    if lst:
        for i in range(len(lst) - 1):
            if lst[i] <= lst[i + 1]:
                return False
        return True
    return False

def Nialpdrome(lst):
    if lst:
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True
    return False

def Repdrome(lst):
    if lst:
        for i in range(len(lst) - 1):
            if lst[i] != lst[i + 1]:
                return False
        return True
    return False

datas = input("Enter Input : ")

datas = [int(data) for data in datas]


if Repdrome(datas):
    print("Repdrome")
elif Metadrome(datas):
    print("Metadrome")
elif Plaindrome(datas):
    print("Plaindrome")
elif Katadrome(datas):
    print("Katadrome")
elif Nialpdrome(datas):
    print("Nialpdrome")
else:
    print("Nondrome")