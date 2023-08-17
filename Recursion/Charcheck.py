def clear_data(x):
    if len(x) == 1:
        return [x[0].strip("'")]
    
    return [x[0].strip("'")] + clear_data(x[1:])

def segment(text, language, data, index):
    print(data)
    if data != "" and data[-1] != text[len(data) - 1]:
        return False
    
    if len(data) > len(text):
        return False
    
    if index >= len(language):
        return False

    if data == text:
        return True

    check1 = segment(text,language,data+language[index],0)
    check2 = segment(text,language,data,index+1)

    return check1 or check2




inp = input("list[str]: ").split(", ")
inp = clear_data(inp)
target = inp[0]
data = inp[1:]
print(target,data)
print(segment(target,data,"",0))