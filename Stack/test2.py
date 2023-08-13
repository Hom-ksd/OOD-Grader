class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop(-1)

    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if self.stack :
            return False
        else:
            return True
    
    def __str__(self) -> str:
        return "[" + ", ".join(x for x in self.stack) + "]"
        
inp = input('Enter Infix : ')

operation_priority = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3,'(' : 0}

output = ""

stack = Stack()

for char in inp:
    print(char)
    print(stack)
    if char.isalpha():
        output += char
    elif char == "(":
        stack.push(char)
    elif char == ')':
        while not stack.isEmpty() and stack.top() != '(':
            output += stack.pop()
        stack.pop()
    else:
        while not stack.isEmpty() and stack != '(' and operation_priority[char] <= operation_priority[stack.top()]:
            output += stack.pop()
        stack.push(char)

while(not stack.isEmpty()):
    output += stack.pop()

print(output)