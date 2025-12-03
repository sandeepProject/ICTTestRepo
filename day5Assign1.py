#Bank Account Manager
#a. Simulate a bank account with deposit, withdrawal, and balance
#enquiry operations
#b. Use variables and data types to store account information
#c. Implement conditional statements to check for sufficient balance
#before withdrawal
#d. Use functions to perform deposit, withdrawal, and balance inquiry
#operations.
#flag 1 : deposit
#flag 2 : withdrawal
#flag 3 : Balance Enquiry

def account_Manage(acNo,flag,amount):
    account_No = 2252
    ac_Balance= 1000
    if flag ==1 and account_No==acNo:
        ac_Balance=ac_Balance+amount
        #print(ac_Balance)
    elif flag==2 and account_No==acNo:
        if ac_Balance>1000:
            ac_Balance=ac_Balance-amount
            #print(ac_Balance)
        else:
            print("Insufficient Balance for the withdrawal. Try again!")
    elif flag==3 and account_No==acNo:
        print(f"Account Balance is {ac_Balance}")
    else:
        print("Error")
    return(ac_Balance)
trans_AcNo = input("Account Number :")
trans_Amount = input("Amount :")
print("1 : deposit, 2: Withdrawal, 3: Balance Check")
trans_Type= int(input("Transaction Type :"))
Bank_Balance=account_Manage(float(trans_AcNo),int(trans_Type),float(trans_Amount))
if(trans_Type==1 or trans_Type==2):
    print(f"Account Balance is : {Bank_Balance}")
else:
   print("Error")





