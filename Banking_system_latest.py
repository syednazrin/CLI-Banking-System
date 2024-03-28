#Syed Nazrin Bin Syed Nurshadir
#TP066789
#Banking System Assignment
#==============================================
#All libraries required will be included here
from datetime import datetime
import os
import sys
#==============================================
#common functions for Registration of staff and customer 
#==============================================
#Create all files of concern
if os.path.isfile('customer.txt')==False:#check if file exists
    fh = open("customer.txt", "w")
    fh.write(','.join(['ID','CustomerAccountNumber','FirstName','SecondName','UserID','Password','Address','DOB','Timestamp','PN'+'\n']))
    fh.close()
if os.path.isfile('customer_banking_data.txt')==False:#check if file exists
       fh = open("customer_banking_data.txt", "w")
       fh.write(','.join(['ID','AccountID','Balance','AccountType','Timestamp','AccountStatus'+'\n']))
       fh.close()
if os.path.isfile('staffdata.txt')==False:#check if file exists
       fh = open("staffdata.txt", "w")
       fh.write(','.join([['ID','StaffID','FirstName','SecondName','PN','Password','Type','Timestamp']]))
       fh.close()
if os.path.isfile('staff_trans_data.txt')==False:#check if file exists
       fh = open("staff_trans_data.txt", "w")
       fh.write(','.join([['ID','StaffID','CustomerID','Timestamp','Status','Password']]))
       fh.close()
if os.path.isfile('superuser_trans_data.txt')==False:#check if file exists
       fh = open("superuser_trans_data.txt", "w")
       fh.write(','.join([['ID','SuperUserID','Activity','StaffID']]))
       fh.close()
#================================================
def PhoneNumRegister():
    '''takes the dob of a customer. 
	Must be exactly 11 character including 2 "-" to proceed
	Must be all numeric
	User is allowed three attempts'''
    k=0
    while k<3:
        PN = input("Enter the Phone Number (XXX-XXXXXXX):")
        if (len(PN) == 11) and ('-' in PN):
            if(PN.replace('-','').isnumeric()==True):
                break
            else:
                print('The typed in values are incorrect.')
                PN=''
                k=k+1
        else:
            print("The length/format is incorrect.")
            PN=''
            k=k+1
            if k<3:
                print("Please try again!")
                continue
            else:
		print('Maximum attempts exceeded.')
    return(PN)

def NameRegister(x): 
    '''This function takes the first name of customer; 
	must be more than 2 letters
	user gets 3 attempts
	must be all letters'''
    k=0
    while k<3:
        FirstName = input(x+":")
        if  (len(FirstName) < 2) :
            print ("There is an error in the entered value")
            FirstName=''
            k=k+1
            if k<3:
                print("Please try again!")
                continue
            else:
                print('Maximum attempts exceeded.')
        else:
            break
    return (FirstName)
		
def AddressRegister ():
    '''This function takes the address of the customer; 
    must be more than 2 letters
    User provided with 3 attempts'''
    k=0
    while k<3:
        Address = input("Fill in Address information")
        print ("Your Address is:", Address)
        if len(Address)<2:
            print('Address cannot be shorter than 2 letters')
            Address=''
            k=k+1
            if k<3:
                print("Please try again!")
                continue
            else:
                print('Maximum attempts exceeded.')
        else:
            break
    return (Address)

def PasswordGenerator (FirstName, SecondName, DOB): 
    '''takes the first 4 characters variable firstName, first 3 of SecondName and last two character in DOB and joins them to create a username'''
    Password = str(FirstName[:4] + SecondName[:3] + DOB.replace('/','')[:-2])
    return (Password)

def DOBRegister ():
    '''takes the dob of a customer. Must be exactly 10 character including 2 / to proceed'''
    k=0
    while (k<3):
        DOB = input ("Date of birth (DD/MM/YYYY) :")
        if (len(DOB) == 10) and (DOB.count('/')==2):
            DOBCheck = dt.datetime.strptime(DOB,'%d/%m/%Y')
            DateNow = dt.datetime.now()
    
            if DateNow<DOBCheck+relativedelta(years=18):
                print("You are underage to register independently for an account.\nPlease head over to our nearest bank with a guardian to register manually")
                DOB=''
                break
            else:
                print("You are eligible!")
                break               
        else:
            DOB=''
            k=k+1
            if k>3:
                print("Exceeded maximum attempts")
                break
            else:
                print("Please try again!")
                continue
    return (DOB)
            
def getRowCountUnique(filename):
    '''This function counts the unique number of account numbers in any given file'''
    fh = open(filename, "r")
    ar = len(set([m.strip()[1] for m in fh.readlines()]))
    fh.close()
    return(ar)

def getRowCount(filename):
    '''This function counts the unique number of account numbers in any given file'''
    fh = open(filename, "r")
    ar = len(fh.readlines())+1
    fh.close()
    return(ar)

def ClientSearch(ACNumber):
    '''This function fetches all the transactions for one account number'''
    fh = open("customer_banking_data.txt","r")
    L = fh.readlines()
    RL=[]
    if (ACNumber not in [int(m.strip().split(',')[1]) for m in L[1:]]):
        print('Customer transactions not found')
        return(RL)
    else:
        for record in L[1:]:
            if int(record.split(',')[1])==ACNumber:
                RL.append(record)
        return RL

def AccountStatement(dem_record,trans_record):
	print(record)

def Report_Generator(dem_record, trans_record)
'''This function is used to generate a report for chosen specific amount of time'''
    print ("From what period would you like the report to reflect?")
    print ("1.One week\n2.One month\n3.Six Months ago\n.4.One year")
    TimePeriod = int(input)
    if TimePeriod == 1 
    elif TimePeriod == 2
    elif TimePeriod == 3
    elif TimePeriod == 4
#===================================================================
#The following section deals with codes involved in making a new user
#===================================================================
def CustomerAccountNoGenerator():
    '''This function counts the number of accounts already made, then makes new acc number'''
    aa = getRowCount('customer.txt')
    CustomerAccountNumber = aa
    return(CustomerAccountNumber)
		
def CSAccountRegister(x='Savings'):
    '''This function asks the users if they want to open an account.
    If yes, they are asked to deposit an amount which is compared
    to the minimum balance of 500 for savings and 100 for current.'''
    choice = int(input("hello, would you like to open a "+x+" account\n press 1 for yes and 2 for no"))
    Balance = -1# -1 is any dummy value 
    status='null'  
    #setting minimum balance
    if x=='Savings':
        mb=500
    else:
        mb=100     
    if choice == 1:
        print ("Minimum balance must be RM"+str(mb))
        Balance = float(input("Please input deposit amount"))
        if Balance < mb:
            status="balance insufficient" 
        else:
            status='ok'
    elif choice==2:
        status='NA'
    return([Balance,status])

def newcustomermainpage(): 
    '''function to allow a customer to register for an acc that will ask for personal information that consist of First and Second names, their phone number, DOB and address.
    Also, with the information, it will generate their customer account number, Name Register'''
    fh = open("customer.txt", "a")
    th = open("customer_banking_data.txt", "a")
    # this is to see if an account has been made; if not it will create a new one by writing into the file 
    choice = int(input("Hello, would you like to open an account with the bank of Nazrin?\npress 1 for Yes and 2 for No"))
    if choice == 1:
        FirstName=NameRegister('First Name')
        SecondName=NameRegister('Second Name')
        print('Welcome:',FirstName+' '+SecondName)

        Address=AddressRegister()
        print ('Address',Address)

        DOB=DOBRegister()
        print ('Date Of Birth:',DOB)

        PN=PhoneNumRegister()
        print ('Phone Number:',PN)

        CustomerAccountNumber=CustomerAccountNoGenerator()
        print ("Your customer account number is :", CustomerAccountNumber)

        UserID=NameRegister('UserID')
        print("Your UserID:",UserID)
        
        password=PasswordGenerator(FirstName, SecondName, DOB)
        print ("Your default password is:", password)

        CurrentBalance=CSAccountRegister('Current')
        SavingsBalance=CSAccountRegister('Savings')
	
	if (FirstName =='') or (SecondName=='') or (Address=='') or (CurrentBalance[1]=='balance ufficient') or 	(SavingsBalance[1]=='balance insufficient') or	(PN==''):
		print('Account cannot be created')
	else:
		ID1=getRowCount('customer.txt')
        	ID2=getRowCount('customer_banking_data.txt')

	        print ("your account has been created")#### new addition
		conf=int(input("Enter 1 for account activation"))
		if conf==1:
			status='active
		else:
			status='pending''
        	fh.write(','.join([str(ID1),str(CustomerAccountNumber),FirstName,SecondName,UserID,password,Address,DOB,str(dt.datetime.now()),PN+'\n'])) #addition of status at end of writing customer file
        th.write(','.join([str(ID2),str(CustomerAccountNumber),str(CurrentBalance[0]),'Current',str(dt.datetime.now()),CurrentBalance[1],status+'\n'])) 
        th.write(','.join([str(ID2+1),str(CustomerAccountNumber),str(SavingsBalance[0]),'Savings',str(dt.datetime.now()),SavingsBalance[1],status+'\n']))
        
        fh.close()
        th.close()
        print ("Customer account has been successfully created")

        #ReturningCustomerMainPage()

    elif choice == 2:
        print('Thank you!')
    else:
        print("invalid choice")
#============================================================================
#The following section deals with codes involved in working with existing user
#============================================================================
def ReturningCustomerLogin(): 
    while True:
        fh = open("customer.txt","r")
        IDLogin = input("Hello!Please enter Customer Number")
        L = fh.readlines()
        for i in L:
            L2 = i.split(',')[0]
            if IDLogin in L2:
                L3=i.split (',')[-1] # new addition to check the active status of the account 
                if L3 == unactive:#
                    print ("account is currently unactive, please head to our nearest outlet to re-activate account")#
                    break#
                elif L3 = active 
                    passwordLogin = input("Account identified; please enter password to verify user:")
                    L4=i.split(',')[5]
                    if passwordLogin in L2:
			ClientSearch(IDLogin)
                        AccountService(i)
                         fh.close() # closing of file 
                    else :
                       print ("invalid password")
                       continue

def AccountService(record):
    RT=ClientSearch(int(record.strip().split(',')[1]))
    print(RT)
    actype=['Savings','Current']
    minbal=[500,100]
    print("What transaction would you like to do today: ?\n1 : Check Balance of account\n2 : withdraw money\n3 : deposit money\n4 : Account settings\n5 : Customer Account report\n6 : Exit ")
    AccountTransaction = int(input("please enter the type of transaction you would like to proceed with"))
    if AccountTransaction   == 1:
        BalanceCheck(record,RT)
    elif AccountTransaction == 2:
        NameAcc=int(input("Choose your account:\n press 1 for savings and 2 for current"))
        if NameAcc in [1,2]:
            RTS=[m for m in RT if m.strip().split(',')[3]==actype[NameAcc-1]]
            print(RTS)
            if len(RTS)==1:
                NR=Withdraw(RTS[0],minbal[NameAcc-1])
            else:
                NR=Withdraw(RTS[-1][0],minbal[NameAcc-1])
            if NR is not None:
                th = open("customer_banking_data.txt", "a")
                th.write(NR)
                th.close()
    elif AccountTransaction == 3:
        NameAcc=int(input("Choose your account:\n press 1 for savings and 2 for current"))
        if NameAcc in [1,2]:
            RTS=[m for m in RT if m.strip().split(',')[3]==actype[NameAcc-1]]
            print(RTS)
            if len(RTS)==1:
                NR=Deposit(RTS[0])
            else:
                NR=Deposit(RTS[-1][0])
            if NR is not None:
                th = open("customer_banking_data.txt", "a")
                th.write(NR)
                th.close()
        elif AccountTransaction == 4:
            Settings(record)
        elif AccountTransaction == 5:
            Report_Generator(record,RT)
        elif AccountTransaction == 6:
            sys.exit()
        else:
          print ("no type of Transaction is available")
    else:
       print('invalid choice')

#### addition of code 
def ShowBalance(record):
    AccountChosen = AccountType()
    if AccountChosen = "Current":
        print ("Your current balance is :",record.split(',')[-1])
    elif  AccountChosen = "Saving":
        print ("Your current balance is :",record.split(',')[-2]))

def Withdraw(record,mb):
        WithdrawAmount = float(input("how much money do you want to want to withdraw?"))
        CurrentBalance=float(record.strip().split(',')[2])
        print(CurrentBalance)
        if (CurrentBalance-WithdrawAmount)  < mb:
            #this will add back the amount wanted to be taken out and
            #then informing that transaction did go through
            print ("account balance insufficient\ntransaction did not go through")
            return(None)
        else:
            CurrentBalance-=WithdrawAmount
            print ("your current balance is :",CurrentBalance)
            ID=getRowCount('customer_banking_data.txt')
            newrecord=record.strip().split(',')
            newrecord[0]=str(ID)
            newrecord[2]=str(CurrentBalance)
        return(','.join(newrecord)+'\n')

def Deposit(record):
        DepositAmount = int(input("how much money do you want to want to deposit?"))
        CurrentBalance=float(record.strip().split(',')[2])
        CurrentBalance += DepositAmount
        print ("your current balance is :",CurrentBalance)
        ID=getRowCount('customer_banking_data.txt')
        newrecord=record.strip().split(',')
        newrecord[0]=str(ID)
        newrecord[2]=str(CurrentBalance)
        return(','.join(newrecord)+'\n')

def PasswordSetting(record):
    '''This function ask for a password confirmation from a user and if password is correct;
the user is allowed to create new password with same minimum length of 9 characters'''
    newrecord = record.strip().split(',')
    while True:
        NewPassword = str(input("please enter a new password"))
        if len(NewPassword) <9:
            print ("Password must be a minimum of 9 characters.\nPlease re-enter a new password")
            continue
        else:
            print("password is accepted")
            newrecord[5] = NewPassword
            print("your new password is:", NewPassword)
            return(','.join(newrecord)+'\n')
#==========================================================
#This section deals with the CREATION of the staff account 
#==========================================================
def StaffLoginPage():
     while True:
        fh = open("staffdata.txt","r")
        IDLogin = input("Hello!Please enter Account Number")
        L = fh.readlines()
        for i in L:
            L2 = i.split(',')[0]
            if  IDLogin in L2:
                passwordLogin = input("Account identified; please enter password to verify user:")
                L3=i.split(',')[4]
                if   passwordLogin in L2:
                    AccountService()
                else :
                   print ("invalid password")
                   continue 
            else :
                print ("Account not registered ")
                continue

def StaffIDgenerator():
    '''This function counts the number of accounts already made, then makes new acc number'''
    aa = getRowCount("staffdata.txt")
    StaffID = aa+1
    return(StaffID)

def RegisterStaffAccount():
        ID1=getRowCount('staffdata.txt')
        ID2=getRowCount('staff_trans_data.txt')

        fh = open("staffdata.txt", "a")
        th = open("staff_trans_data.txt", "a")

        FirstName=NameRegister('First Name')
        SecondName=NameRegister('Second Name')

        print ("Staff Name:",' '.join([FirstName,SecondName]))

        DOB=DOBRegister()

        PN=PhoneNumRegister()

        StaffID=StaffIDgenerator()

        PS=PasswordGenerator(FirstName,SecondName,DOB)

        print ("StaffPassword:",PS)
        activity='register'

        SU=input('Are you a super-user?Please enter 1 for Yes, 2 for No.')
        fh.write(','.join([str(ID1),str(StaffID),FirstName,SecondName,PN,PS,SU+'\n']))
        fh.close()
        th.write(','.join([str(ID2),str(StaffID),'NA',str(dt.datetime.now()),'New',activity+'\n']))
        th.close()
        if SU=="1":
            print ("Super User account has been successfully created")
        else:
            print ("Staff account created; pending approval by super user")
#===================================================================
#This section deals with the activities of a returning Staff Member besides updating info
#===================================================================
#addition of new code for the whole section
def  staffservices():
    print ("1:View Customer Details/n2:Suspend Customer Account/n3:Reinstate Customer Account/n4:Update Customer Details/n")
    StaffService = int(input())
    if StaffService == 1:
        ClientSearch()
    elif StaffService == 2:
        StatusEdit()
    elif StaffService == 4:
        UpdateCustomerDetails()
    else:
        ("service doesn not exist")
        continue 
 
def StatusEdit():
    clientsearch(L)
    for i in L:
        L2 = i.split(',')[-1]
        print ("the current status of customer is:", L2 \n "would you like to change the status?\n1.Yes\n2.No")
        updatechoice = int(input())
        if updatechoice == 1:
            fh = open("customer.txt","w")
            if L2 == active:
                L2 = L2.replace(L2,'unactive')
            elif L2 == unactive:
                L2 = L2.replace(L2,'active')
        fh.close()
####NOT DONE YET
'''assumption: if a customer wants to update status or info; must go to a nearby center so a staff can physically verify any change and update on status''')
def UpdateCustomerDetails():
    clientsearch(L)
    print ("what information would you like to update:\n1.Name\2.Phone Number\n3.Address\n4.Date of Birth")
    updatechoice == int(input())
    if updatechoice == 1:
        x = 1
        L2:i.split(',')[x]
        NameRegister()
        
    elif updatechoice == 2:
        x = 8
        L2:i.split(',')[x]
        NameRegister()
    elif updatechoice == 3:
        x = 6
        L2:i.split(',')[x]
        NameRegister()
    elif updatechoice == 4:
        x = 7
        L2:i.split(',')[x]
        NameRegister()
    else
        print ("the information does not exist")  
#===================================================================
#This section deals with the actions of the Super-User of the system
#===================================================================
def Super_UserAccountLogiN():
    while True:
        print("please enter super-User key:")
        super_User_Key = input()
        if super_User_Key == "BankofNazrin222":
            print("access granted as Super-User")
            print ("what service would you like to do")

        else:
            print("access denied. Invalid User detected")
            continue
#======================================================================
#Main Menu
#======================================================================
attempt_cn=0 
while True :
    print("Welcome to the bank of Nazrin")
    print("what type of user are you")
    print("1 : Returning Customer")
    print("2 : New Customer")
    print("3 : Staff")
    print("4 : Super-User")
    activityType = int(input())
    if  activityType == 1:
            ReturningCustomerLogin()
            break
    elif  activityType == 2:
            newcustomermainpage()
            break
    elif activityType == 3:
            StaffLoginPage()
            break
    elif activityType == 4:
            Super_UserAccountLogInPage()
            break 
    else:
            print("invalid activity choice. Please try again:")
	    attempt_cn+=1
            if attempt_cn>2:
             break
            else:
             continue

