class Dictionary:
    def __init__(self) -> None:
        self.keys = []
        self.datas = []

    def append(self,key,data):
        self.keys.append(key)
        self.datas.append(data)

    def checkKey(self,key):
        return key in self.keys
    
    def checkData(self,data):
        return data in self.datas

    def getKeyIndex(self,key):
        if key not in self.keys:
            return -1
        else:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    return i
                
    def getDataIndex(self,data):
        if data not in self.datas:
            return -1
        else:
            for i in range(len(self.datas)):
                if self.datas[i] == data:
                    return i
    
    def getData(self,index):
        if index < len(self.datas):
            return self.datas[index]
        
    def getKey(self,index):
        if index < len(self.keys):
            return self.keys[index]

def isIsomorphic(string1,string2):
    index = 0
    check = Dictionary()
    for char in string1:
        #if char not in check and string2[index] not in check.values():
        # print(char,string2[index])
        if not check.checkKey(key=char) and not check.checkData(data=string2[index]):   
            check.append(char,string2[index])
        else:
            #if char not in check or check[char] != string2[index] :
            if check.getData(check.getKeyIndex(char)) != string2[index] or check.getKey(check.getDataIndex(string2[index])) != char:
                return False
        index += 1
    # print(check)
    return True

strings = input("Enter str1,str2: ").split(",")


if isIsomorphic(strings[0],strings[1]):
    print(f"{strings[0]} and {strings[1]} are Isomorphic")
else:
    print(f"{strings[0]} and {strings[1]} are not Isomorphic")
