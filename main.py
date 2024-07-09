def deposite():
    while True:
        amount = input("what would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter a positive number")
                
        else:
            print("Please enter a number")
    return amount 

deposite() #function call