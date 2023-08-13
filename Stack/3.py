class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

operation_priority = {'+' : 1,'-' : 1, '*' : 2,'/' : 2, '^' : 3}

stack = []

temp_stack = Stack()

for i in range(len(inp)):
    # print(inp[i] , stack)
    if inp[i].isalpha():
        temp_stack.push(inp[i])
    elif inp[i] in operation_priority:
        while stack and stack[-1] != '(' and operation_priority[inp[i]] <= operation_priority[stack[-1]]:
            temp_stack.push(stack.pop())
        stack.append(inp[i])
    elif inp[i] == '(':
        stack.append(inp[i])
    elif inp[i] == ')':
        while stack and stack[-1] != '(':
            temp_stack.push(stack.pop())
        stack.pop()
    
while stack:
    temp_stack.push(stack.pop())

while not temp_stack.isEmpty():
    S.push(temp_stack.pop())

while not S.isEmpty():

    print(S.pop(), end='')

print()