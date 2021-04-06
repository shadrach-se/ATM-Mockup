from datetime import datetime   #module used for accessing date and time
import random   #module used for generating account numbers.
database = {}   #for storing user data.


def init():
    """
    Info: This function checks if the user has an account with ZURIBANK, proceeds to login if yes otherwise register the user on ZURIBANK.
    """
    print("********** Welcome to ZURIBANK **********")
    while True:
        accountHolder = int(
            input("Do you have an account with us? \n1. Yes \n2. No \nEnter here: "))
        if accountHolder == 1:
            login()
            break
        elif accountHolder == 2:
            register()
            break
        else:
            print("Invalid option selected. Please try again.\n")
            continue


def login():
    """
    Info: This function verifies account number and password in the database, proceeds to banking operations if valid otherwise print error message.
    """
    print("*************** Login **************")
    while True:
        userAccNumber = int(input("Enter your account number: "))
        passwrd = input("Enter your password: ")
        if (userAccNumber in database) and (database[userAccNumber][3] == passwrd):
            userDetails = database[userAccNumber]
            print("\nWelcome %s %s" % (userDetails[0], userDetails[1]))
            dateAndTime()
            bankOperation()
            break
        else:
            print("Incorrect account number or password. Please try again. \n")
            continue


def dateAndTime():
    """
    Info: This function prints out the current date and time.
    """
    curr = datetime.now()
    print("Today's date is %02d-%02d-%d and the time is %02d:%02d" %
          (curr.day, curr.month, curr.year, curr.hour, curr.minute))


def bankOperation():
    """
    Info: This function contains all the banking operations on ZURIBANK.
    """
    selectedOption = int(input("\nWhat would you like to do?\n1. Deposit. \n2. Withdrawal. \n3. Logout. \n4. Exit. \nEnter here: "))
    if selectedOption == 1:
        deposit()
    elif selectedOption == 2:
        withdrawal()
    elif selectedOption == 3:
        logout()
    elif selectedOption == 4:
        close()
    else:
        print("Invalid option selected. Please try again.\n")
        bankOperation()


def withdrawal():
    """
    Info: This function handles withdrawal.
    """
    withdraw = int(input("How much would you like to withdraw: "))
    print("Take your cash... #%d \n" % withdraw)
    while True:
        anotherTransaction = int(input("Would you like to perform another transaction? \n1. Yes. \n2. No. \nEnter here: "))
        if anotherTransaction == 1:
            bankOperation()
            break
        elif anotherTransaction == 2:
            close()
            break
        else:
            print("Invalid option selected. Please try again.\n")
            continue


def deposit():
    """
    Info: This function handles deposits.
    """
    deposit = int(input("How much would you like to deposit: "))
    print("Your deposit has been completed.\n")
    while True:
        anotherTransaction = int(
            input("Would you like to perform another transaction? \n1. Yes. \n2. No. \nEnter here: "))
        if anotherTransaction == 1:
            bankOperation()
            break
        elif anotherTransaction == 2:
            close()
            break
        else:
            print("Invalid option selected. Please try again.")
            continue


def logout():
    """
    Info: This is a logout function.
    """
    print("Logging out...\n")
    login()


def close():
    """
    Info: This function exits the banking system.
    """
    return


def register():
    """
    Info: This function accepts user data for registration, creates account, display account number, then proceed to login.
    """
    print("*************** REGISTER ***************")
    firstName = input("Enter your first name here: ")
    lastName = input("Enter your last name here: ")
    email = input("Enter your email address here: ")
    while True:
        password = input("Enter your password: ")
        confpassword = input("Confirm password: ")
        if password == confpassword:
            print("Password saved.\n")
            break
        else:
            print("Password does not match. Please try again.\n")
            continue
    accNumber = accNumberGeneration()
    database[accNumber] = [firstName, lastName, email, password]
    print("Your account has been created.")
    print("**** ******* *** **** *******")
    print("Your account number is: %d" % accNumber)
    print("**** ******* ****** *** **********")
    print("You can now login with your account number and password.\n")
    login()


def accNumberGeneration():
    """
    Info: This function generates user account number.
    """
    return random.randrange(1111111111, 9999999999)

### Initializing the ZURI banking system ####
init()
