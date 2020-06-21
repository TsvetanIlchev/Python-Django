# def my_func(param1='default'):
#     print("My first python function!")
#
# my_func()

# def hello():
#     print("hello")
#
# hello()

# def hello():
#     return ("hello")
#
# hello()
#
# result = hello()
#
# print(result)

# def addnum(num1, num2):
#     return num1+num2
#
# result = addnum(2, 3)
# print(result)
# result = addnum("2", "3")
# print(result)
# print(type(result))

# def addnum(num1, num2):
#     if type(num1)==type(num2)==type(10):
#         return num1+num2
#     else:
#         return "Sorry, I need integers!"
#
# result = addnum(2, 3)
# print(result)
# result = addnum("2", "3")
# print(result)

# # Lambda Expression
# mylist = [1,2,3,4,5,6,7,8]
#
# evens = filter(lambda num:num%2 == 0, mylist)
# print(list(evens))
#
# # Filter
# mylist = [1,2,3,4,5,6,7,8]
#
# def even_bool(num):
#     return num%2 == 0
#
# evens = filter(even_bool, mylist)
# print(list(evens))
