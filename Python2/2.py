pi = 3.141592653589793238462643383279

class Spherical:

    def __init__(self,r):
        ### Enter Your Code Here ###
        self.radius = r
        

    def changeR(self,Radius):
        ### Enter Your Code Here ###
        self.radius = Radius

    def findVolume(self):
        ### Enter Your Code Here ###
        return (4 / 3) * pi * self.radius**3

    def findArea(self):
        ### Enter Your Code Here ###
        return 4 * pi * self.radius**2

    def __str__(self):
        ### Enter Your Code Here ###
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)