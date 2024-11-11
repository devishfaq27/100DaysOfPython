#           Project: Simple Calculator
#TODO- Define a function add that takes two numbers and returns their sum.
#TODO- Define a function subtract that takes two numbers and returns the difference.
#TODO- Define a function multiply that takes two numbers and returns their product.
#TODO- Define a function divide that takes two numbers and returns their quotient.
#TODO- Create a main function that:
#TODO- Asks the user to pick an operation: add, subtract, multiply, or divide.
#TODO- Asks the user for two numbers.
#TODO- Calls the appropriate function based on the user’s choice.
#TODO- Prints the result.
#TODO- Add a loop to keep asking the user if they want to perform another calculation until they choose to quit.

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Error: Division by zero is undefined"
    return a/b

def main():
    while True:
        user_answer = input("do you want to perfom an opration: ")
        if user_answer == "yes":
            number_a = int(input("pick a number: "))
            oprations = input("pick the opration: + - * / : ")
            number_b = int(input("pick a number: "))
            if oprations == "+":
                print(f"{number_a} {oprations} {number_b} = {add(number_a,number_b)}")
            elif oprations == "-":
                print(f"{number_a} {oprations} {number_b} = {sub(number_a,number_b)}")
            elif oprations == "*":
                print(f"{number_a} {oprations} {number_b} = {mul(number_a,number_b)}")
            elif oprations == "/":
                print(f"{number_a} {oprations} {number_b} = {div(number_a,number_b)}")
        else:
            print("thanks!")
            break



main()