class Stack:
    def __init__(self,max_size) -> None:
        self.stack = []
        self.max_size = max_size

    def push(self,data):
        if self.get_size() < self.max_size:
            self.stack.append(data)
            return True
        else:
            return False
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return 0
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def get_size(self):
        return len(self.stack)
    
    def isFull(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            return False
        
    def top(self):
        if self.stack :
            return self.stack[-1]
        else:
            return 0

    def is_Instack(self,data):
        temp_stack = self.stack.copy()
        while(len(temp_stack) > 0):
            if data == temp_stack.pop():
                return True
        return False

    def __str__(self) -> str:
        return '[' + ', '.join(str(car) for car in self.stack) + ']'

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
# m : max_car_in_stack 
# s : car in stack
# o : action for stack
# n : car's number

m,n = int(m),int(n)

### Enter Your Code Here ###

# print(m,s,o,n)
stack1 = Stack(m)
stack2 = Stack(m)

car_list = s.split(',')

for car in car_list:
    if car == '0':
        continue
    else:
        stack1.push(int(car))


if o == 'arrive':
    if not stack1.is_Instack(n) and not stack1.isFull():
        stack1.push(n)
        print(f"car {n} arrive! : Add Car {n}")
    elif stack1.is_Instack(n):
        print(f"car {n} already in soi")
    else:
        print(f"car {n} cannot arrive : Soi Full")
elif o == 'depart':
    if stack1.isEmpty():
        print(f"car {n} cannot depart : Soi Empty")
    else:
        if not stack1.is_Instack(n):
            print(f"car {n} cannot depart : Dont Have Car {n}")
        else:
            while(stack1.top() != n):
                stack2.push(stack1.pop())
            stack1.pop()
            while(not stack2.isEmpty()):
                stack1.push(stack2.pop())
            print(f"car {n} depart ! : Car {n} was remove")

print(stack1)