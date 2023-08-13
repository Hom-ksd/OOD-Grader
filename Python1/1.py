print("*** Converting hh.mm.ss to seconds ***")
hh,mm,ss = input("Enter hh mm ss : ").split()
hh = int(hh)
mm = int(mm)
ss = int(ss)
# print(hh,mm,ss)
if hh < 0:
    print(f"hh({hh}) is invalid!")
elif mm < 0 or mm >= 60:
    print(f"mm({mm}) is invalid!")
elif ss < 0:
    print(f"ss({ss}) is invalid!")
else:
    ans = 0
    ans += hh * 3600 + mm * 60 + ss
    print(f"{hh:02d}:{mm:02d}:{ss:02d} = {ans:,} seconds")

