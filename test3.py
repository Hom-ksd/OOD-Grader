def postfix_evaluation(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isalpha():
            stack.append(char)
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = '(' + str(operand1) + char + str(operand2) + ')'
            stack.append(result)

    return stack

infix_expression = 'a+b*c-(d/e+f)*g'
postfix_expression = 'abc*de/f+g*-'

result = postfix_evaluation(postfix_expression)
print(result)
