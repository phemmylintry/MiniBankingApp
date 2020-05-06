import random
from string import digits
import os
import datetime

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
            with open('session.txt', 'w') as f:
                f.write("Session started: " + str(datetime.datetime.now()))
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
        with open('customer.txt', 'a') as f1, open('session.txt', 'a') as f2:
            f1.write("\n\nAccount Name: %s\n" % name)
            f1.write("Opening Balance: %s\n" % balance)
            f1.write("Account Type: %s\n" % acc_type)
            f1.write("Email: %s\n" % email)
            f1.write("Account Number %s\n" % acc_number)
            f2.write("\n\nAccount Name: %s\n" % name)
            f2.write("Opening Balance: %s\n" % balance)
            f2.write("Account Type: %s\n" % acc_type)
            f2.write("Email: %s\n" % email)
            f2.write("Account Number %s\n" % acc_number)
            print("Acounted Created Successfully")
        return operations()
    
    elif start == "2":
        with open('session.txt', 'r') as f:
            details = f.read()
            chk_acc = input("Enter Customer's Account Number: ")
            if chk_acc in details:
                print(details)
                f.close()
                return operations()
            else:
                print('Not found')
                return operations() 

    elif start == "3":
        os.remove('session.txt')
        return bankApp()

while (bankAppMain):
    program = bankApp()