input_string = input("Enter expresion : ")

stack = []

open_brackets = ('(' , '[' , '{')
close_brackets = (')' , ']' , '}')

is_answered = False

for char in input_string:
    if char in open_brackets:
        stack.append(char)
    else:
        if char not in close_brackets:
            continue
        else:
            if stack:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    if not is_answered :
                        print(f"{input_string} Unmatch open-close")
                        is_answered = True
            else:
                if not is_answered :
                    print(f"{input_string} close paren excess")
                    is_answered = True

if stack and not is_answered:
    print(f"{input_string} open paren excess   ",end="")
    print(f"{len(stack)} : " + "".join(str(i) for i in stack))
else:
    if not is_answered:
        print(f"{input_string} MATCH")
