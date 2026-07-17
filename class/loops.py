#FOR LOOPS **********************************

# n = 4 
# for i in range(1,n):
#     print(i)

# for i in range(1,101):
#     print(i)

# fact =1
# n= int(input("enter a number : "))
# for i in range(1,n+1):
#     fact = fact * i
# print(f"The factorial of the number {n} is {fact}")


#WHILE LOOPS **********************************
# n =20
# while n>12:
#     print(n)
#     n = n-1

# n = 1
# while n<=5:
#     print("Hello")
#     n = n+1
# n=1
# while n<=100:
#     if n%2!=0:
#         print(n)
#     n= n+1

# n = 10
# while n <=100:
#     print(n)
#     n = n+2

# while n>0:
#     print(n)
#     n = n-1
# while n>0:
#     print(n)
#     n = n-2

# n = int(input("Enter a number which factorial you want  : "))
# temp =n
# fact = 1
# while temp>0:
#     fact = fact * temp
#     temp =temp-1
# print(temp)
# print(f"the factorial of {n} is {fact}")


n = int(input("Enter a number which table you want : "))
i=1
while i>0:
    if i ==11:
        break
    else:
        print(f"{n} X {i} = {n*i
                             /}")
        i = i + 1


