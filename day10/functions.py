# def format_name(f_name, l_name): #paramaters
#     print(f_name.title())
#     print(l_name.title())
#
# format_name("aNGela", "ANGELA")

# def function_1(text):
#     return text + text
# def function_2(text):
#     return text.title()
# output = function_2(function_1("Hello"))
# print(output)

#Functions with multiple return
 # def my_func(f_name, l_name):
 #    """hey this is doc string (this mean we can tell our function
 #        defination to others )"""
 #    if f_name == "" or l_name == "":
 #        return "you have provide your frist name and last name, EXIT FUNCTION...."
 #    formated_f_name = f_name.title()
 #    formated_l_name = l_name.title()
 #    return f"{formated_f_name}, {formated_l_name}"

# output = my_func(input("what is your frsit name: "), input("what is your last name: "))
# print(output)

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def cal(num1, num2, symbol):
#     input1 = input("enter the num1: ")
#     input2 = input("+\n-\n*\n/ \n enter the symbol: ")
#     input3 = input("enter the num2: ")
#     input1 = num1
#     input2 = symbol
#     input3 = num2
#     if input2 == "+":
#         return input1 + input3
#     elif input2 == "-":
#         return input1 - input3
#     elif input2 == "*":
#         return input1 * input3
#     elif input2 == "/":
#         return input1 / input3
#
# cal(input1, input2, input3)

