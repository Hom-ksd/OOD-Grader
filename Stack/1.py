inp = input("Enter Input : ")

stack = []

is_printed = False
ans = False

for i in inp:
    if i == '[' or i == '(':
        stack.append(i)
    elif i == ']' :
        if (not stack or stack.pop() != '['):
            ans = True
    elif i == ')' :
        if (not stack or stack.pop() != '('):
            ans = True

if stack or ans :
    print('Parentheses : Unmatched ! ! !')

else:
    print('Parentheses : Matched ! ! !')

# [[[(([]))]]]