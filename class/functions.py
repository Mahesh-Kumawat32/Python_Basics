# # SIMPLE PYTHON FUNCTION
# def helloworld():
#     print("Hello World")
# helloworld()

# # FUNCTION WITH ARGUMENT AND PARAMETER
# def greet(name):
#     print(f"Hello {name}")
# greet("Mahesh")

# # SUM OF TWO NUMBER USING FUNCTION---------
# def sum(a,b):
#     return a+b
# b = (sum(10,20))

# # SQUARE OF A NUMBER --------------
# a = int(input("Enter a number : "))
# def square(a):
#     print(f"The square of {a} is {a**2}")
#     # print("The square of ",a," is ",(a**2))
# square(a)

# # SHOW NAME AND AGE OF USERS-------------
# name = input("Enter name : ")
# age = int(input("Enter age : "))
# def show(name,age):


#     print(f'''\tName : {name} 
#     \tAge : {age}''')
# show(name,age)

# # RETURN STATEMENT
# def sum(a,b):
#     return a+b
# b = (sum(10,20))
# print(b)


# # MULITPLE FUNCTIONS IN SAME PYTHON FILE
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))

# def subs(a,b):
#     print(f"The difference of {a} and {b} is {a-b}")
# print(subs(a,b))

# def multi(a,b):
#     print(f"The mulitplication of {a} and {b} is {a*b}")
# print(multi(a,b))
    
# # EVEN ODD USING FUNCTIONS
# n = int(input("Enter a number : "))
# def evenodd(n):
#     if n%2==0:
#         print(f"The number {n} is even")
#     else:
#         print(f"The number {n} is odd")
# evenodd(n)

# # FIND LARGE OF TWO NUMBERS USIGN IF ELSE WITH FUNCTIONS------------
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def large_of_two(a,b):
#     if a>b:
#         print(f'The number {a} is greater than {b}')
#     else:
#         print(f'The number {b} is greater than {a}')
# large_of_two(a,b)

# # FIND FACTORIAL USING FUNCTIONS------------
# n = int(input("Enter a number : "))
# def facto(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     print(f'The factorial of {n} is {fact}')
# facto(n)

# # FIND MINIMUM OF TWO NUMBERS USING IF ELSE WITH FUNCTIONS------------
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def small_of_two(a,b):
#     if a<b:
#         print(f'The number {a} is less than {b}')
#     else:
#         print(f'The number {b} is less than {a}')
# small_of_two(a,b)

# # FIND NUMBER IS + OR - IF ELSE WITH FUNCTIONS------------
# n = int(input("Enter a number : "))
# def posi_nege(n):
#     if n>0:
#         print(f"{n} is positive")
#     elif n==0:
#         print(f"number entered by you is zero")
#     elif n<0:
#         print(f"{n} is negative")
#     else:
#         print(f"{n} is not a valid number")
# posi_nege(n)

# # FIND AVG OF THREE NUMBERS IF ELSE WITH FUNCTIONS------------
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# c = int(input("enter third one : "))
# def avg_three(a,b,c):
#     avg = 0
#     avg = (a+b+c)/3
#     print(f"The average of {a},{b} and {c} is {avg}")
# avg_three(a,b,c)


# # CHECK NUMBER IS DIVISIBLE BY 10 USING FUNCTIONS------------
# n = int(input("Enter a number : "))
# def divi_ten(n):
#     if n % 10==0:
#         print(f"The number {n} is divisible by 10")
#     else:
#         print(f"The number {n} is not divisible by 10")
# divi_ten(n)
