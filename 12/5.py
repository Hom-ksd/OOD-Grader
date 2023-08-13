class MyInt:
    def __init__(self,value):
        self.value = value

    def __sub__(self,other):
        return f"{self.value} - {other.value} = {self.value - int(other.value/2)}"
    
    def isPrime(self):
        if self.value <= 1:
            return f"{self.value} isPrime : False"
        for i in range(2,int(self.value / 2)):
            if self.value % i == 0:
                return f"{self.value} isPrime : False"
        return f"{self.value} isPrime : True"
    
    def isprime(self,data):
        for i in range(2,int(data / 2) + 1):
            if data % i == 0:
                return False
        return True

    def showPrime(self):
        if self.value <= 1:
            return f"Prime number between 2 and {self.value} : " + "!!!A prime number is a natural number greater than 1"
        return_str = ""
        for i in range(2,self.value + 1):
            if self.isprime(i):
                return_str += str(i) + " "
        return f"Prime number between 2 and {self.value} : " + return_str

print(" *** class MyInt ***")
num1,num2 = input("Enter 2 number : ").split()
a = MyInt(int(num1))
b = MyInt(int(num2))

print(a.isPrime())
print(b.isPrime())
print(a.showPrime())
print(b.showPrime())
print(a-b)