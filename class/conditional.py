# age = int(input("Enter your age : "))
# if  age>18:
#     print("you are eligible to drive")
# else:
#     print("you are note eligible to drive")

#**********TICCKET BUYING SYSTEM
# age = int(input("Enter your age : "))
# if age<=12:
#     print("Travel Free")
# else:
#     print("You have to buy a ticket")

#EVEN AND ODD
# n = int(input("enter a number which you want to check even or odd : "))
# if n%2==0:
#     print(f"number {n} is even ")
# else:
#     print(f"number {n} is odd")


#*************SOME PROJECTS BASED ON CONDITIONAL STATEMENTS******************
#FIND NUMBER IS POSSITIVE OR NEGATIVE
# n = int(input("enter a interger : "))
# if n>0:
#     print(f"{n} is possitive")
# elif n==0:
#     print(f"you enter zero")
# else:
#     print(f"{n} is negative")
    

#CHECK STUDENT MARKS >35: PASS AND <35: FAIL
# marks = float(input("Enter your marks : "))
# if marks<=35:
#     print("You are failed")
# elif marks>=35 and marks<=100:
#     print("You are passed")
# else:
#     print("You entered wrong marks")

#DELIEVERY APP : USER AMOUNT >1000 GIVE FREE DELIEVERY AND <1000 PAY
# amt = float(input("Enter amount you pay for purchase : "))
# if amt>=1000:
#     print("Free delivery")
# elif amt<=1000 and amt>0:
#     print("You have to pay Delivery charge",amt/10)
# else:
#     print("you enter wrong price")


#DRIVING LICENSE : IF AGE IS 18 THEN DRIVE ELSE NOT
# age = int(input("Enter your age : "))
# if age==0:
#     print("you want to first born on this earth")
# elif age>=18 and age<=70:
#     print("You are eligible for driving license")
# elif age>=70 and age<=100:
#     print("kaka/kaki aaram karo")
# else:
#     print("you are not human")


#LOGIN SYSTEM 
# greeting = 'LOGIN'
# print(greeting.center(60,"-"))
# username = input("Enter Your username : ")
# pwd = input("Enter Your Password : ")
# print('''                   Your credential successfully stored👨
#                     Remember Your Credential to login👍👍
#                                 VISIT AGAIN 😊''')
# while True:
#     permission = input("You want to login again (yes/no) : ")
#     if permission == "yes" and "Yes":
#         enter_name = input("Enter Username : ")
#         enter_pwd = input("Enter Password : ")
#         if enter_name==username and enter_pwd==pwd: 
#             print("You are logged in successfully")
#             break
#         else:
#             print("wrong credential")
    

# practice just
# age = int(input("Enter your age : "))
# if age<=12 and age>0:
#     print("You are child")
# elif age<=19 and age>12:
#     print("You are teenager")
# elif age<=25 and age>19:
#     print("You are young")
# else:
#     print("Adult")

# marks = int(input("Enter your marks : "))
# if marks<=100 and marks>80:
#     print("You are passed with A++")
# elif marks>=80 and marks<100:
#     print("You are passed with A grade")
# elif marks>=60 and marks<80:
#     print("You are passed with B grade")
# elif marks>33 and marks<60:
#     print("You are passed with C grade")
# else:
#     print("You are failed")

#nested else-if

# greeting = 'LOGIN'
# print(greeting.center(60,"-"))
# username = input("Enter Your username : ")
# pwd = input("Enter Your Password : ")
# print('''                   Your credential successfully stored👨
#                     Remember Your Credential to login👍👍
#                                 VISIT AGAIN 😊''')
# while True:
#     permission = input("You want to login again (yes/no) : ")
#     if permission == "yes" and "Yes":
#         enter_name = input("Enter Username : ")
#         enter_pwd = input("Enter Password : ")
#         if enter_name==username and enter_pwd==pwd: 
#             print("You are logged in successfully")
#             break
#         else:
#             print("wrong credential")

# while True:
#     num = int(input("Enter a number (1-7): "))
#     match num:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday")
#         case _:
#             print("You entered wrong day")
#     p = input("Enter your choice again : ")
#     if p =='yes' or 'Yes':
#         continue
#     else:
#         break
    

#MAKE ATM SYSTEM *************************
    # PRINT BALANCE
    # TAKE USER INPUT FOR DEPOSIT OR ADD AMOUNT
    # TAKE USER INPUT AND WITHDRAWL AMOUNT
    # PRINT STATEMENT DEPOSTI WITHDRAWL AND CURRENT BALANCE
    # DEFAULT EXIT TO THE SYSTEM 
greet = 'WELCOME TO ATM'
print(greet.center(50,"-"))
name = input("Enter Your Name : ")
Ac = input("Enter Your Account Number : ")
blc = 10000
print(f'''\t\t\t\t\tName : {name}
\t\t\t\t\tAccount Number : {Ac}\n\t\t\t\t\tDate : 06-07-2026\n\t\t\t\t\tCurrent Balance : {blc}''')
choice = int(input("For Withdrawl Enter -> 1\nFor Deposit Enter -> 2 : "))
match choice:
    case 1:
        amt = int(input("Enter amount you want to Withdrawl : "))
        print("Your amount is Withdrawled")
        print(f'''Withdrawl Amount : {amt}\nCurrent Amount : {blc-amt}''')
    case 2:
        amt1 = int(input("Enter amount you want to Credit : "))
        print("Your amount is Deposited")
        print(f'''Credited Amount : {amt1}\nCurrent Amount : {blc+amt1}''')
    case _: 
        print("You enter wrong input")