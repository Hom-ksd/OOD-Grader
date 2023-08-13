def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    stack = []
    output = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isalpha():
            output.append(char)
        elif char in operators:
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    postfix_expression = ''.join(output)
    return postfix_expression

infix_expression = 'a+b*c-(d/e+f)*g'

postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)
