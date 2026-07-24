#ATM PROJECT

import random
#EVERY DAY YOU CAN ADD MORE CUSTOMER WHO CAN CREATE THERE ACCOUNT 
#TODAY LIMITATION ONLY 10 PEOPLE CAN CREATE NEW ACCOUNT
customer_data = {
    'cst1' : {},
    'cst2' : {},
    'cst3' : {},
    'cst4' : {},
    'cst5' : {},
    'cst6' : {},
    'cst7' : {},
    'cst8' : {},
    'cst9' : {},
    'cst10' : {}
}
def create_account(name,permanent_address,current_address,amount_to_first_deposit):
    customer_name = name
    customer_ac = random.randint(10000000,99999999)
    ifsc_code = "SBIN0001234"
    branch_location = "ISANPUR"
    branch_city = "AHMEDABAD"
    current_date = "24-07-2026"
    customer_permanent_address = permanent_address
    customer_current_address = current_address
    customer_first_deposit = amount_to_first_deposit
    print(f"\nYOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY ✔\nYOUR DETAILS ARE AS BELOW :\n")
    customer_data['cst1']["NAME"] = customer_name
    customer_data['cst1']["AC/NO"] = customer_ac
    customer_data['cst1']["IFSC CODE"] = ifsc_code
    customer_data['cst1']["BRANCH NAME"] = branch_location
    customer_data['cst1']["BRANCH CITY"] = branch_city
    customer_data['cst1']["DATE OF AC CREATE"] = current_date
    customer_data['cst1']["CURRENT ADDRESS"] = customer_current_address+", "+branch_location+", "+branch_city
    customer_data['cst1']["PERMANENT ADDRESS"] = customer_permanent_address
    customer_data['cst1']["CURRENT BALANCE"] = customer_first_deposit

    print(80*"-")
    for a,b in customer_data['cst1'].items():
        print(f"{a} : {b}")
    print(80*"-")


def deposit_money():
    print(f'You can deposit money')
def withdrawl_money():
    pass
def check_balance():
    pass
def transaction_history():
    pass



heading = " STATE BANK OF INDIA "
print(heading.center(100,"*"))
while True:
    permission_to_create_ac = input("TO PROCEED FURTHER ENTER => (YES/NO): ").upper()
    if permission_to_create_ac=="YES":
        print("\n")
        choice = input("TO CREATE A NEW ACCOUNT (PRESS) => A\n> TO DEPOSIT MONEY (PRESS) => D\n> TO WITHDRAWL MONEY (PRESS) => W\n> TO CHECHING BALANCE (PRESS) => CB\n> TO CHECK TRANSACTION HISTORY (PRESS) => H\n=>").upper()
        match choice:
            case 'A':
                name = input("ENTER YOUR FULL NAME : ").upper()
                permanent_address = input('ENTER YOUR PERMANENT ADDRESS : ').upper()
                current_address = input("ENTER YOUR CURRENT ADDRESS : ").upper()
                amount_to_first_deposit = int(input("ENTER AMOUNT YOU WANT TO DEPOSIT FIRST (MINIMUM 500/-) : "))
                create_account(name,permanent_address,current_address,amount_to_first_deposit)
            case 'D':
                deposit_money()
            case 'W':
                withdrawl_money()
            case 'CB':
                check_balance()
            case 'H':
                transaction_history()
            case _:
                print("YOU ENTER SOMETHING WRONG! PLEASE TRY AGAIN")
    else:
        break
    print(100*"*")
