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
# ARMSTRONG NUMBER : An Armstrong number (also called a Narcissistic number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits in the number.
# n = int(input("Enter a number : "))
# def armstrong_or_not(n):
#     global temp
#     temp = n
#     digits = len(str(n))
#     total = 0
#     while n>0:
#         digit = n%10
#         total = total+(digit**digits)
#         n = n//10
#     return temp == total
# if armstrong_or_not(n):
#     print(f"{temp} is a armstrong number")
# else:
#     print(f"{temp} is not a armstrong number")

#25
# A prime number is a natural number greater than 1 that has exactly two factors:
    # means only divisible by 1, or itself
# n = int(input("Enter a number : "))
# def prime_or_not(n):
#     global cnt
#     cnt = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             cnt = cnt +1
#         else:
#             continue
#     return cnt
# if prime_or_not(n)==2:
#     print(f"{n} is a prime number ")
# else:
#     print(f"{n} is not a prime number")

#=======================================================
#ANOTHER SET
#=======================================================
#1
# l = float(input("Enter Length : "))
# b = float(input("Enter Width : "))
# def calculate_area(l,b):
#     print(f"The area of rectangle which length is {l} and width is {b} is : {l*b}")
# calculate_area(l,b)
    
#2
# def evenodd(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
# n = int(input("Enter a number : "))
# evenodd(n)

#3
# def max_or_min(a,b,c):
#     if a>b and a>c:
#         print(f"{a} is maximum")
#     elif b>a and b>c:
#         print(f"{b} is maximum")
#     else:
#         print(f"{c} is maximum")
# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))
# max_or_min(a,b,c)

#4
# def calcius_to_feranhide(c):
#     far = (c*(9/5))+32 
#     return far
# c = float(input("Enter temprature in celcius : "))
# print(f"""Calcius = {c}\nFahrenheit = {calcius_to_feranhide(c)}""")

#5
# something = input("Enter a word : ")
# def find_vowel(something):
#     cnt = 0
#     for i in something:
#         if i=='a' or i=="e" or i=='i' or i == 'o' or i =='u' or i=='A' or i=="E" or i=='I' or i == 'O' or i =='U':
#             cnt = cnt +1
#         else:
#             continue
#     return cnt
# print(f"The vowel in the word {something} are total : {find_vowel(something)}")

#6
# n = int(input("Enter a number : "))
# def find_pelindrome_or_not(n):
#     temp = n
#     remain = 0
#     reverse = 0
#     while temp>0:
#         remain = temp %10
#         reverse = reverse * 10 + remain
#         temp = temp //10
#     if reverse==n:
#         print(f"The number {n} is a pelindrome number because {n} = {reverse}")
#     else:
#         print(f"{n} is not a pelindrome number because {n} != {reverse}")
# find_pelindrome_or_not(n)

#7
# def find_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     print(f"The factorial of the number {n} is {fact}")
# n = int(input("Enter a number which factorial you want : "))
# find_fact(n)

#8
# n = int(input("Enter a number to check it is prime or not : "))
# def find_prime_or_not(n):
#     cnt = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             cnt += 1
#         else:
#             continue
#     if cnt ==2:
#         print(f"The number {n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")
# find_prime_or_not(n)

#9
# method -1: using type conversion list --->set-->list
# l = []
# while True:
#     n = int(input("Enter element of list : "))
#     l.append(n)
#     choice = input("You want to add more element to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_unique_from_list(l):
#     l = set(l)
#     l.union()
#     l = list(l)
#     print(f"After removing duplicate elements list is {l}")
# print(f"\n\n\nBefore removing duplicate elements list is {l}")
# find_unique_from_list(l)


#method -2: using list itself
# l = []
# while True:
#     n = int(input("Enter element of list : "))
#     l.append(n)
#     choice = input("You want to add more element to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_unique_from_list(l):
#     cnt = 0
#     for i in range(0,len(l)):
#         cnt = l.count(i)
#         if cnt==1:
#             continue
#         else:
#             while l.count(i)>1:
#                 l.remove(i)
#     print(sorted(l))
# find_unique_from_list(l)


#10
# marks = []
# while True:
#     n = int(input("Enter marks : "))
#     marks.append(n)
#     choice = input("You want to add more student marks to list (yes/no) : ")
#     if choice =="Yes" or choice =="yes":
#         continue
#     elif choice =="No" or choice == "no":
#         break
# def find_avg_marks(marks):
#     sum = 0
#     for i in range(0,len(marks)):
#         sum = sum + marks[i]
#     avg_result = sum/len(marks)
#     return avg_result
# print(f"The Average Result of institute is {find_avg_marks(marks)}")

#11
# l = [1,2,3,4,1,5,6,2,4]
# def find_second_largest(l):
#     l = set(l)
#     l.union()
#     l = list(l)
#     sorted(l)
#     print(l)
#     print(l[len(l)-2])
# find_second_largest(l)

#12
# sentence = input("Enter a sentence : ")
# s=sentence.lower()
# data = {}
# def word_frequency(s):
#     l = s.split()
#     cnt = 0
#     for i in range(0,len(l)):
#         cnt = l.count(l[i])
#         data[l[i]] = cnt
#     print(data)
# word_frequency(s)

#13

#14

#15

#16
# heading = "GET RESULT"
# print("\n",heading.center(100,"*"))
# student_name = input("Enter Your Name : ")
# student_roll_no = int(input("Enter Your Roll No : "))
# result = float(input("Enter Your Marks : "))
# def get_result(student_name,student_roll_no, result):
#     result_head = "MARKSHEET"
#     print(result_head.center(30,"="))
#     if result>=90 and result<100:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : A""")
#     elif result>=80 and result<90:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : B""")
#     elif result>=70 and result<80:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : C""")
#     elif result>=60 and result<70:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : D""")
#     elif result>=40 and result<60:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Pass\nGrade : F""")
#     elif result<40:
#         print(f"""Name : {student_name}\nRoll No : {student_roll_no}\nMarks(%) : {result}\nResult : Fail\nGrade : __""")
#     else:
#         print("You Entered Something Wrong")
#     print(f"\t\t\nTHANK YOU")
# get_result(student_name,student_roll_no, result)
# ending = "*"
# print(ending.center(100,"*"))

#17

#18

#19

#20