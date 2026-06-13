balance = 100000
record = []
print("====welcome to atm====")
while True:
    
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.View statement")
    print("5.exit")
    
    choice = int(input("Enter a choice:"))
    
    if choice == 1:
        print("your balance is:",balance)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit:"))
        if amount>0:
            balance = balance + amount
            record.append(f"Deposited:+{amount}")
            print("Your  new balance is:",balance)
        else:
            print("invalid amount")
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount>0 and amount<=balance:
            balance = balance - amount
            record.append(f"Withdraw:{amount}")
            print("Your new balance is :",balance)
        elif amount<=0:
            print("Invalid amount")
        else:
            print("Insufficient balance")
    elif choice ==4:
        print("\n---Transaction statement---")
        if not record:
            print("No transaction yet")
        else:
            for history in record:
                print(history)
                print("---------------")
    elif choice == 5:
        print("Thankyou for using Ayush atm")
    else:
        print("Invalid choice,plz try again")
                
    
    
            
        
        