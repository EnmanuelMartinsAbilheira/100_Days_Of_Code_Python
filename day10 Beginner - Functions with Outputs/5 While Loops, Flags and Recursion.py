#calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multipply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply, 
  "/": divide,
}

def calculator():

    print(logo)

    num1 = float(input("whats the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("whats the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}");

        if input(f"type 'y' to continue calculating with {answer}, orr type 'n' to start new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()