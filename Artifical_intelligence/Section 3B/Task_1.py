def get_precedence(op):
    """Return the precedence of the operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '×', '/'):
        return 2
    return 0

def perform_operation(a, b, op):
    """Perform the arithmetic operation."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op in ('*', '×'):
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Error: Division by zero")
        return a / b

def convert_to_postfix(expression):
    """Convert infix expression to postfix notation."""
    output = []
    operators = []
    number = ''
    
    for char in expression:
        if char.isdigit() or char == '.':
            number += char  
        else:
            if number: 
                output.append(float(number))
                number = ''  
            
            if char in "+-*/×":
                while (operators and operators[-1] != '(' and 
                       get_precedence(operators[-1]) >= get_precedence(char)):
                    output.append(operators.pop()) 
                operators.append(char) 
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()

    if number: 
        output.append(float(number))

    while operators:  
        output.append(operators.pop())
    
    return output

def evaluate_expression(postfix):
    """Evaluate the postfix expression."""
    stack = []
    for token in postfix:
        if isinstance(token, float):
            stack.append(token) 
        else:
            b = stack.pop()
            a = stack.pop()
            result = perform_operation(a, b, token)
            stack.append(result)  
    
    return stack[0] 

def calculate(expression):
    """Calculate the result of the expression."""
    expression = expression.replace(' ', '') 
    postfix = convert_to_postfix(expression)  
    return evaluate_expression(postfix)  

while True:
    user_input = input("Enter an expression (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        result = calculate(user_input)  
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
