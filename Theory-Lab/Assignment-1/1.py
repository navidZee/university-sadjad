import math
 
firstRun = True

def bold(string):
    """
    This function returns a bolded string.
    """
    return "\033[1m" + string + "\033[0m"

while True:

    if firstRun:
        print("=== Welcome To The Simple Calculator ===")
    
    firstRun = False
    
    print("list of available operations:")
    print("1. Addition: +")
    print("2. Subtraction: -")
    print("3. Multiplication: *")
    print("4. Division: /")
    print("5. Power: ** or ^")
    print("7. Logarithm: log")
    print("8. Sin: sin")
    print("9. Cos: cos")
    print("10. Tan: tan")
    print("11. Cot: cot")
    print("12. Sqrt: sqrt")
    print("13. Factorial: !")
    print("14. Exit: exit or quit")
    
    print("")
    print("please choose an operator: ")

    operator = input()

    if operator in ["14", "exit", "quit"]:
        break

    twoOperatorsList = ['+', '-', '*', '/', '**', '^']

    print("type your number:")
    inputA = float(input())
    if operator in twoOperatorsList:
        print("type your second number:")
        inputB = float(input())

    if operator == "+":
        result = inputA + inputB

    elif operator == "-":
        result = inputA - inputB

    elif operator == "*":
        result = inputA * inputB

    elif operator == "/":
        if inputB == 0:
            result = "Can't divide by zero"
        else:
            result = inputA / inputB
    elif operator == "**" or operator == "^":
        result = inputA ** inputB

    elif operator == "log":
        result = math.log(inputA)
    elif operator == "sin":
        result = math.sin(inputA)
    elif operator == "cos":
        result = math.cos(inputA)
    elif operator == "tan":
        result = math.tan(inputA)
    elif operator == "cot":
        result = 1 / math.tan(inputA)
    elif operator == "sqrt":
        result = math.sqrt(inputA)
    elif operator == "!":
        result = math.factorial(inputA)

    print(bold("Result: " + str(result) + "\n\r"))