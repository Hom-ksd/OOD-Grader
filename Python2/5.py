class funString():

    def __init__(self,string = ""):
        ### Enter Your Code Here ###
        self.string  = string

    def __str__(self):
        ### Enter Your Code Here ###
        pass

    def size(self) :
        ### Enter Your Code Here ###
        return len(self.string)

    def changeSize(self):
        ### Enter Your Code Here ###
        return_string = ""
        for char in self.string:
            if char >= 'A' and char <= 'Z':
                return_string += chr(ord(char) + 32)
            elif char >= 'a' and char <= 'z':
                return_string += chr(ord(char) - 32)
        return return_string
    
    def reverse(self):
        ### Enter Your Code Here ###
        return self.string[::-1]

    def deleteSame(self):
        ### Enter Your Code Here ###
        return_string = ""
        for char in self.string:
            if char not in return_string:
                return_string += char
        return return_string


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())