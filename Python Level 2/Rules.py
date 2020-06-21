# #Global level
# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# print(x)
# print(my_func())
# my_func()
# print(x)

# #LOCAL level
# lambda x: x**2
#
# #Enclosing function locals
# name = "This is a global name!"
#
# def greet():
#     name = "Sammy"
#
#     def hello():
#         print("hello "+name)
#
#     hello()
#
# greet()
# print(name)

# Build-in level
x = 50

# def func(x):
    # print("x is ",x)
    # x = 1000
    # print("Local x changed to:",x)

# func(x)
# print(x)

# def func():
#     global x
#     x = 1000
#
# print("Before function call, x is: ",x)
# func()
# print("After function call, x is: ",x)

def func():
    x = 1000
    return x

print("Before function call, x is: ",x)
x = func()
print("After function call, x is: ",x)    
