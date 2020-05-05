import random
from string import digits

bankAppMain = True

def bankApp():
    start = input("\n1. Staff Login \n2. Close App\n\n")
    if start == "1":
        return staffLogin()
    elif start == "2":
        exit()

def staffLogin():
    with open('staff.txt', 'r') as f:
        users = f.read()
        user = input("Input your username: ")
        psw = input("Input your password: ")
        if user in users and psw in users:
            print("Login Successful \n")
            return operations()
        else:
            print("Wrong Credentials")
            return bankApp()

def operations():
    start = input("1. Create New Bank Account \n2. Check Account Details \n3. Logout\n")
    if start == "1":
        print("Please Input the following details to create an Account \n")
        name = input("Account Name: ")
        balance = int(input("Opening Balance: "))
        acc_type = input("Account Type: ")
        email = input("Account Email: ")
        secureRandom = random.SystemRandom()
        acc_number = "".join(secureRandom.choice(digits) for i in range(10))
        print("This is the customer's genrerated Account Number: ", acc_number)
        with open('customer.txt', 'a') as f:
            f.write("\n\nAccount Name: %s\n" % name)
            f.write("Opening Balance: %s\n" % balance)
            f.write("Account Type: %s\n" % acc_type)
            f.write("Email: %s\n" % email)
            f.write("Account Number %s" % acc_number)
            print("Acounted Created Successfully")
        return operations()
    
    elif start == "2":
        chk_acc = int(input("Enter Customer's Account Number: "))
        if chk_acc < 10:
            input("Enter A Valid Account Number: ")
        
    
    elif start == "3":
        return bankApp()

while (bankApp):
    program = bankApp()
    operations = operations()