import re

def check_digits(num):
    if len(num) !=4: return False
    for i in range(1, 4):
        for j in range(i):
            if num[i] == num[j]:return False
    return True


def create():
    card_number = ""
    pin_number = ""
    email = ""
    extra_service = []
    while True:
        card_number = input('Enter card number(4-digits).')
        if check_digits(card_number): break
    
    while True:
        pin_number = input('Enter PIN number(4-digits).')
        if check_digits(pin_number): break

    while True:
        email = input('Enter KFUPM email.')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]kfupm.edu.sa$'
        if(re.search(regex, email)):break

    while True:
        if len(extra_service) == 0:
            e = input('Enter extra service.')
        else:
            e = input('Enter extra service (enter "X" to end).')
        if e.upper == "X":
            if len(extra_service) > 0: break
        else:
            if e != "":
                extra_service.append(e)
            


def login():
    pass


def show(file):
    pass

    
def changePINFun(currentPIN, cardNumber, file):
    pass

    
def withdrawFun(money, cardNumber, file):
    pass

    
def depositFun(file, nMoney, cardNumber):
    pass

    
def payBillFun(file, nMoney, cardNumber):
    pass

    
def viewTransactionsFun(cardNumber):
    pass

    
def terminateFun(file, nMoney, cardNumber):
    pass

    


while True:
    login = input('Enter "L" to log in or "S" to sign up.')
    if login.upper() in ["L", "S"]: break

if login.upper() == "L":
    # to login()
    login()
else:
    # to create()
    create()

# print(str(check_digits("2445")))
