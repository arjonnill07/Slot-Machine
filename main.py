MAX_LINES = 3 #Global Constant

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

def get_no_of_lines():
    while True:
        lines = input("How many lines would you like to play? (1-" + str(MAX_LINES) + "):? ") #string_conversion and concatanation
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #checking if value is inbetween
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

        
def main():
    balance = deposite() #function call
    lines = get_no_of_lines()
    print(balance,lines)

main()
    
    