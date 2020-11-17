import re
from time import sleep
from os import system, name 
from datetime import datetime


def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def check_digits(num):
    if len(num) !=4: return False
    for i in range(1, 4):
        for j in range(i):
            if num[i] == num[j]:return False
    return True


def current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d, %H:%M:%S")


def create():
    card_number = ""
    pin_number = ""
    email = ""
    extra_service = []
    while True:
        clear()
        card_number = input('Enter card number(4-digits): ')
        if check_digits(card_number): break
    
    while True:
        clear()
        pin_number = input('Enter PIN number(4-digits): ')
        if check_digits(pin_number): break

    while True:
        clear()
        email = input('Enter KFUPM email: ')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]kfupm.edu.sa$'
        if(re.search(regex, email)):break

    while True:
        clear()
        if len(extra_service) == 0:
            e = input('Enter extra service: ')
        else:
            e = input('Enter extra service (enter "X" to end): ')
        if e.upper() == "X":
            if len(extra_service) > 0: break
        else:
            if e != "":
                extra_service.append(e)

    # Write into cardNumber.txt
    with open('cardNumber.txt', 'w') as out_file:
        out_file.write("card number: " + card_number)
        out_file.write("\nPIN number: " + pin_number)
        out_file.write("\nemail: " + email)
        out_file.write("\nextra service: " + "; ".join(extra_service))
        out_file.write("\nmoney: 0\n")
    out_file.close()
    
    sleep(3)
    login()


def login():
    card_number = ""
    pin_number = ""
    try:
        with open('cardNumber.txt', 'r') as in_file:
            card_number = in_file.readline()
            card_number = card_number[len("card number: "):-1]
            pin_number = in_file.readline()
            pin_number = pin_number[len("PIN number: "):-1]
        in_file.close()
    except:
        print("Warning: There are no registered users.")
        sleep(2)
        return False

    while True:
        clear()
        print("\t" * 2 + "LOG IN")
        print("=" * 40)
        if input("\nEnter card number: ") == card_number: break

    while True:
        clear()
        print("\t" * 2 + "LOG IN")
        print("=" * 40)
        if input("\nEnter PIN number: ") == pin_number: break

    sleep(3)
    return True


def show(file):
    with open(file, 'r') as in_file:
        clear()
        print("\t" + "Show account information")
        print("=" * 40 + "\n")
        print(in_file.read())
    in_file.close()
    sleep(3)

    
def changePINFun(currentPIN, cardNumber, file):
    clear()
    print("\t" + "Change PIN number")
    print("=" * 40)
    pin_number = ""
    if input("\nEnter current PIN number: ") != currentPIN:
        print("\nWarning: Wrong PIN number")
    else:        
        while True:
            clear()
            print("\t" + "Change PIN number")
            print("=" * 40)
            pin_number = input('\nEnter new PIN number(4-digits): ')
            if check_digits(pin_number): break
        content = []
        with open('cardNumber.txt', 'r') as in_file:
            content = in_file.readlines()
        in_file.close()
        content[1] = "PIN number: " + pin_number + "\n"
        with open('cardNumber.txt', 'w', newline="") as out_file:
            out_file.write("".join(content))
        out_file.close()

    sleep(3)

    
def withdrawFun(money, cardNumber, file):
    amount = 0
    while True:
        clear()
        print("\t" + "Withdraw amount of money")
        print("=" * 40)
        amount = input('\nEnter the amount to withdraw: ')
        try:
            if float(amount) <= money: break
        except:
            pass
    try:
        amount = round(money - float(amount), 4)
        with open('cardNumber.txt', 'r') as in_file:
            content = in_file.readlines()
        in_file.close()
        content[4] = "money: " + str(amount) + "\n"
        content = content[:5]
        content.append("updated time: " + current_time() + "\n")
        with open('cardNumber.txt', 'w', newline="") as out_file:
            out_file.write("".join(content))
        out_file.close()
    except:
        pass
    sleep(3)
    sleep(3)

    
def depositFun(file, nMoney, cardNumber):
    clear()
    print("\t" + "Deposit amount of money")
    print("=" * 40)
    amount = input('\nEnter the amount to be deposited: ')
    try:
        amount = round(float(amount) + nMoney, 4)
        with open('cardNumber.txt', 'r') as in_file:
            content = in_file.readlines()
        in_file.close()
        content[4] = "money: " + str(amount) + "\n"
        content = content[:5]
        content.append("updated time: " + current_time() + "\n")
        with open('cardNumber.txt', 'w', newline="") as out_file:
            out_file.write("".join(content))
        out_file.close()
    except:
        pass
    sleep(3)

    
def payBillFun(file, nMoney, cardNumber):
    sleep(3)

    
def viewTransactionsFun(cardNumber):
    sleep(3)

    
def terminateFun(file, nMoney, cardNumber):
    pass


def start():
    while True:
        clear()
        user_input = input('Enter "L" to log in or "S" to sign up: ')
        if user_input.upper() in ["L", "S"]:
            if user_input.upper() == "S":
                create()
            if login(): break
            


def main():
    start()
    card_number = ""
    pin_number = ""
    email = ""
    extra_service = ""
    money = 0
    file = "cardNumber.txt"
    
    while True:
        with open('cardNumber.txt', 'r') as in_file:
            card_number = in_file.readline()
            card_number = card_number[len("card number: "):-1]
            pin_number = in_file.readline()
            pin_number = pin_number[len("PIN number: "):-1]
            email = in_file.readline()
            email = email[len("email: "):-1]
            extra_service = in_file.readline()
            extra_service = extra_service[len("extra service: "):-1]
            money = in_file.readline()
            try:
                money = float(money[len("money: "):-1])
            except:
                pass
        in_file.close()
        clear()
        print("\t" + "Bank Account Progam")
        print("=" * 40)
        print("""\n1. Show account information
2. Change PIN number
3. Withdraw amount of money
4. Deposit amount of money
5. Pay bills
6. View the last transactions
7. Terminate a program\n""")
        print("=" * 40)
    
        user_input = input("\nEnter Your Feature: ")
        try:
            if user_input == "1":
                show(file)
            elif user_input == "2":
                changePINFun(pin_number, card_number, file)
            elif user_input == "3":
                withdrawFun(money, card_number, file)
            elif user_input == "4":
                depositFun(file, money, card_number)
            elif user_input == "5":
                payBillFun(file, money, card_number)
            elif user_input == "6":
                viewTransactionsFun(card_number)
            elif user_input == "7":
                terminateFun(file, money, card_number)
                break
        except:
            pass

    
main()