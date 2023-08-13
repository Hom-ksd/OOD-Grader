print("*** Reading E-Book ***")
text,hl = input("Text , Highlight : ").split(",")
# print(text,hl)
for char in text:
    if char == hl:
        print(f"[{char}]",end="")
    else:
        print(char,end="")
