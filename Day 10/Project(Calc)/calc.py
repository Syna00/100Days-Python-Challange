from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(ku1, ku2):
    return ku1 - ku2
def multiply(kal1, kal2):
    return kal1*kal2
def devide(bag1, bag2):
    return bag1/bag2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide,
}
def calculator():
    should_acumulate = True
    num1 = float(input("What is the first number?: "))  

    while should_acumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick the operation : ")
        num2 = float(input("What is the next number?: "))
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : \n").lower()
        if choice == "y":
            num1 = answer
        else:
            should_acumulate = False
            print("\n" * 20)
            calculator()

calculator()