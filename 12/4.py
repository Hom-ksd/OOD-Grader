print("*** String Rotation ***")
str1,str2 = input("Enter 2 strings : ").split()

r_str1 = str1
r_str2 = str2

cnt = 1

Finish = False
is_printed = False

while(True):
    r_str1 = r_str1[-1] + r_str1[:-1]
    r_str2 = r_str2[1:] + r_str2[0]
    if r_str1 == str1 and r_str2 == str2:
        Finish = True
    # print part
    if cnt <= 5 or Finish:
        print(cnt, r_str1, r_str2)
    elif not is_printed:
        print(" . . . . . ")
        is_printed = True

    if Finish :
        print(f"Total of  {cnt} rounds.")
        break
    cnt += 1
