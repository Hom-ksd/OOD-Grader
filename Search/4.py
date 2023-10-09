def isIsomorphic(string1,string2):
    index = 0
    check = {}
    for char in string1:
        if char not in check and string2[index] not in check.values():
            check[char] = string2[index]
        else:
            if char not in check or check[char] != string2[index] :
                return False
        index += 1
    # print(check)
    return True

strings = input("Enter str1,str2: ").split(",")


if isIsomorphic(strings[0],strings[1]):
    print(f"{strings[0]} and {strings[1]} are Isomorphic")
else:
    print(f"{strings[0]} and {strings[1]} are not Isomorphic")
