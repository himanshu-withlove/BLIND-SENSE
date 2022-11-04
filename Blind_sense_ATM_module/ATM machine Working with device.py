import myfunc

acc_no=1020
acc_name="HIMANSHU VERMA"
acc_name_f="VINOD KUMAR VERMA"
acc_bal=25000
pin=1234

print("Welcome to Laxmi Bank")
te = "Welcome to Laxmi Bank."
myfunc.newfunc(te)
print("1 cardless \n 2 for card")
te="1 cardless 2 for card."
myfunc.newfunc(te)
op1=input()
c_op1=int(op1)

if c_op1==(1):
    print("You choosed cardless Transection \nPlease Enter Your Account Number")
    te="You choosed cardless Transection Please Enter Your Account Number."
    myfunc.newfunc(te)
    acc_no_enter=input()
    c_acc_no_enter=int(acc_no_enter)
    te="Enter Your Account Number Again."
    myfunc.newfunc(te)
    acc_no_enter2=input("Enter Your Account Number Again\n")
    
    c_acc_no_enter2=int(acc_no_enter2)
   # if (c_acc_no_enter==c_acc_no_enter2) :
    if (c_acc_no_enter==c_acc_no_enter2==acc_no):
        print("Welcome! ",acc_name,"S/O",acc_name_f,"Account No.",acc_no)
        te="Welcome"+str(acc_name)+"S/O"+str(acc_name_f)+"Account No."+str(acc_no)+"."
        myfunc.newfunc(te)
        print("Choose accordingly :\n (1) Balance Enquiry \n (2) Widrawal Money")
        te="1 Balance Enquiry  2 Widrawal Money."
        myfunc.newfunc(te)
        op1_1=input()
        cop1_1=int(op1_1)
        if cop1_1 ==(1):
            print("Hey!",acc_name,"You Choosed Balance Enquiry\nYour Current Balence is :",acc_bal)
            te="Hey!"+str(acc_name)+"Your Current Balence is"+str(acc_bal)+"."
            myfunc.newfunc(te)
        elif cop1_1==2:
            print("Hey!",acc_name,"You choosed Balence Widrawal\nPlease Enter the money :")
            te="Hey!"+str(acc_name)+"Please Enter the money ."
            myfunc.newfunc(te)

            wid_money=input("Rupees: ")
            c_wid_money=int(wid_money)
            print("Enter The Pin")
            te="enter the pin."
            myfunc.newfunc(te)
            pin_enter=input("Please Don't share your pin with anyone\n")
            c_pin_enter=int(pin_enter)
            if c_pin_enter==pin:
                if c_wid_money>acc_bal:
                    print("You Don't Have Sufficent money in account\n Please try again")
                    te="You Don't Have Sufficent money in account Please try again."
                    myfunc.newfunc(te)
                else :
                    print()
                    ava_bal=acc_bal-c_wid_money
                    print("Transection Completed.\n Kindly Collect your cash. \n Avaliable Balence :",ava_bal,"Rupees. \n Thank-you for using our service.")
                    te="Transection Completed, Kindly Collect your cash."
                    myfunc.newfunc(te)
                    te="avaliable balence"+str(ava_bal)+"."
                    myfunc.newfunc(te)
            else:
                print("Incorrect Pin Entered")
                te="Incorrect Pin Entered."
                myfunc.newfunc(te)
    else:
        print("Account Number is Incorrect not Matched  \n Please Try Again.")
        te="Account Number is Incorrect not Matched Please Try Again."
        myfunc.newfunc(te)

elif c_op1==2:
    print("Please Enter Your card")
    te="please enter your card."
    myfunc.newfunc(te)
    card=input()
    print("\nCard Inserted sucessfully, don't Remove Untill the tansection is completed\n")
    te="Card Inserted sucessfully, donot Remove Untill the tansection is completed."
    myfunc.newfunc(te)
    print("Welcome! ",acc_name,"S/O",acc_name_f,"Account No.",acc_no)
    te="Welcome! "+str(acc_name)+"S/O"+str(acc_name_f)+"Account No."+str(acc_no)+"."
    myfunc.newfunc(te)
    print("Choose accordingly :\n (1) Balance Enquiry \n (2) Widrawal Money")
    te="Choose accordingly  1 Balance Enquiry 2 Widrawal Money."
    myfunc.newfunc(te)
    op1_1=input()
    cop1_1=int(op1_1)
    
    if cop1_1 ==(1):
            
            print("Hey!",acc_name,"You Choosed Balance Enquiry")
            te="Hey!"+str(acc_name)+"You Choosed Balance Enquiry."
            myfunc.newfunc(te)
            te="hey"+str(acc_name)+"."
            print("Enter The Pin")
            myfunc.newfunc(te)
            te="enter the pin."
            pin_enter=input("Please Don't share your pin with anyone\n")
            c_pin_enter=int(pin_enter)
            if c_pin_enter==pin:
                print("\nYour Current Balence is :",acc_bal)
                te="ur Current Balence is"+str(acc_bal)+"."
                myfunc.newfunc(te)
            else:
                print("Incorrect Pin Entered")
                te="incorrect pin entered."
                myfunc.newfunc(te)
    elif cop1_1==2:
        print("Hey!",acc_name,"You choosed Balence Widrawal")
        te="hey"+str(acc_name)+"you choosed balence widrawal."
        myfunc.newfunc(te)
        wid_money=input("Enter The Rupees: ")
        c_wid_money=int(wid_money)
        print("\nPlease Enter the pin")
        te="please enter the pin."
        myfunc.newfunc(te)
        pin_enter=input("Please Don't share your pin with anyone\n")
        c_pin_enter=int(pin_enter)
        if c_pin_enter==pin:
               
            # print("Enter The Pin")
            # pin_enter=input("Please Don't share your pin with anyone\n")
            # c_pin_enter=int(pin_enter)
            # if c_pin_enter==pin:
            if c_wid_money>acc_bal:
                print("You Don't Have Sufficent money in account\n Please try again")
                te="you donot have sufficent money in your account please try again."
                myfunc.newfunc(te)
            else :
                print()
                print("Transection Completed.\n Kindly Collect your cash. \n Avaliable Balence :",acc_bal-c_wid_money,"Rupees. \n Thank-you for using our service.")
                te="transection completed kindly collect your cash."
                myfunc.newfunc(te)
    else:
        print("Incorrect Pin Entered")
        te="incorrect pin entered."
        myfunc.newfunc(te)
else:
    print("Account Number is Incorrect not Matched  \n Please Try Again.")
    te="account number is incorrect not matched please try again."
    myfunc.newfunc(te)


