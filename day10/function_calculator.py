def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

oprations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculator():
    num1 = int(input("type a 'number': "))
    should_continue = True
    while should_continue:
        for symbols in oprations:
            print(symbols)
        opration_symbols = input("pic a 'symbol': ")
        num2 = int(input("type a 'number': "))
        answer = oprations[opration_symbols](num1, num2)
        print(f"{num1} {opration_symbols} {num2} = {answer}")
        restart = input("want to continue the calculation: type 'y' for yes and 'n' for no: ").lower()
        if restart == "y":
            num1 = answer
        else:
            should_continue = False

calculator()