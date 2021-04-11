from datetime import datetime
now = datetime.now()
import random
database = {}
print(now)

def init():
    print("Weclome to RP Bank")
    haveAccount = int(input("Do you have a bank account with us: 1 (yes) 2 (no) \n"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        print (register())
    else:
        print("You have selected invalid option")
        init()

def login():
    print("Log in to your account")
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser): 
            if(userDetails[3] == password):    
                bankOperation(userDetails)
    print("Invalid account or password information")     
    login()    

def register():
    print("***********Registeration***********")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n" )
    last_name = input("What is your last name? \n")
    password = input("Enter a new password \n")
    accountNumber = generationAccountNumber()
    database[accountNumber] = [ first_name, last_name, email, password ]
    print("Your Account Has been created \n")
    print("********************************")
    print("Your account number is %d" % accountNumber)
    print("********************************")
    login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1])) 
  
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) log out (4) exit "))
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        print("You have now logged out")
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)
        
def depositOperation():
    print("You have selected deposit")
    deposit = int(input ('How much would you like to deposit? \n'))
    newBalance = generateBalance() + deposit
    print ('The current balance is $ %d ' % newBalance )
    print ('\n')
    additionalOption()

def withdrawalOperation():
    print("You have selected withdrawal" )
    cash = int(input('How much would you like to withdraw? \n'))
    print("Your remaining balance is $ %d" % (generateBalance() -cash))
    print('Take your cash')
    print ('\n')
    additionalOption()

def generateBalance():
    return random.randrange(0,100000000000000000000000)

def generationAccountNumber():
    return random.randrange(1111111111111,9999999999999)

def logout():
    login()

def additionalOption(): 
    anythingElse = int(input('Can I help you with something else? Enter (1) yes, (2) No-Exit '))
    if(anythingElse == 1):
        bankOperation ()
    elif(anythingElse ==2):
        exit()
    else:
        print("Invalid option selected")
        additionalOption ()

init()



