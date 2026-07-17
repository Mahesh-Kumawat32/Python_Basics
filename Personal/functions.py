#1
# def helloworld():
#     print("Hello World")
# helloworld()

#2
# def greet(name):
#     print(name)
# greet("Mahesh")

#3
# def greet(name):
#     print("Hello ",name)
# greet("Mahesh")

#4
# def sum(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")
# sum(10,20)

#5
# a = int(input("Enter a number which square you want : "))
# def square(n):
#     print(f"The square of {n} is {n**2}")
# square(a)

#6
# n = int(input("Enter a number which cube you want : "))
# def cube(n):
#     print(f"The cube of {n} is {n*n*n}")
# cube(n)

#7
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def large_of_two(a,b):
#     if a>b:
#         print(f'The number {a} is greater than {b}')
#     else:
#         print(f'The number {b} is greater than {a}')
# large_of_two(a,b)

#8
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# def small_of_two(a,b):
#     if a<b:
#         print(f'The number {a} is less than {b}')
#     else:
#         print(f'The number {b} is less than {a}')
# small_of_two(a,b)

#9
# l = float(input("Enter length of rectangle : "))
# b = float(input("Enter width of rectangle : "))
# def rectangle_area(l,b):
#     print(f"The area of rectangle which length is {l} and width is {b} is : {l*b}")
# rectangle_area(l,b)

#10
# l = float(input("Enter length of rectangle : "))
# b = float(input("Enter width of rectangle : "))
# def rectangle_perimeter(l,b):
#     print(f"The perimeter of rectangle which length is {l} and width is {b} is : {2*(l+b)}")
# rectangle_perimeter(l,b)

#11
# n = int(input("Enter a number : "))
# def evenodd(n):
#     if n%2==0:
#         print(f"The number {n} is even")
#     else:
#         print(f"The number {n} is odd")
# evenodd(n)

#12
# n = int(input("Enter a number : "))
# def absolute_value(n):
#     if n>0:
#         print(f"You enter {n}")
#     elif n<0:
#         print(f"You enter {-1*(n)}")
#     elif n==0:
#         print(f"You enter zero")
#     else:
#         print('You enter a wrong number')
# absolute_value(n)

#13
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# c = int(input("enter third one : "))
# def avg_three(a,b,c):
#     avg = 0
#     avg = (a+b+c)/3
#     print(f"The average of {a},{b} and {c} is {avg}")
# avg_three(a,b,c)

#14
# a = int(input("Enter first value (must integer): "))
# b = int(input("Enter second value (must integer): "))
# def swap_two_numbers(a,b):
#     temp = a
#     a = b
#     b = temp
#     print(f"The swaped number are a = {a} and b = {b}")
# swap_two_numbers(a,b)

#15
# n = int(input("Enter a number : "))
# def find_last_digit(n):
#     last_digit = n%10
#     print(f"The last digit of the number {n} is {last_digit}")
# find_last_digit(n)

#16
# n = int(input("Enter the number which factorial you want : "))
# def fact(n):
#     facto = 1
#     for i in range(1,n+1):
#         facto = facto*i
#     print(f"The value of factorial of {n} is {facto}")
# fact(n)

#17
# n = int(input("Enter the number : "))
# def sum_of_n_num(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     print(f"The sum of first {n} number is {sum}")
# sum_of_n_num(n)

#18
# n = int(input("Enter the number which mulitplication table you want : "))
# def multiplication(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# multiplication(n)

#extra sum of 1-100 even number and same for odd number with minor changes
# n = int(input("Enter the number : "))
# def sum_of_n_num(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum = sum + i
#         else:
#             continue
#     print(f"The sum of first {n} number is {sum}")
# sum_of_n_num(n)

#19
# n = int(input("Enter a number upto to which you want even numbers : "))
# def evennum(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
#         else:
#             continue
# evennum(n)

#20
# n = int(input("Enter a number upto to which you want even numbers : "))
# def oddnum(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             print(i)
#         else:
#             continue
# oddnum(n)

#21
# n = (input("Enter a number : "))
# def return_num_total(n):
#     total_digit = len(n)
#     print(f"The total digit in number {n} is {total_digit}")
# return_num_total(n)

#22
# n = int(input("Enter a number : "))
# temp = n
# def reverse_num(temp):
#     reverse = 0
#     remainder = 0
#     while temp>0:
#         remainder = temp %10
#         reverse = reverse * 10 + remainder
#         temp = temp // 10
#     print(f"The Reverse number of {n} is {reverse}")
# reverse_num(temp)

#23
# n = int(input("Enter a number : "))
# temp = n
# def reverse_num(temp):
#     reverse = 0
#     remainder = 0
#     while temp>0:
#         remainder = temp %10
#         reverse = reverse * 10 + remainder
#         temp = temp // 10
#     if reverse==n:
#         print(f"{n} is a pelindrome number")
#     else:
#         print(f"{n} is not pelindrome")
# reverse_num(temp)

#24

