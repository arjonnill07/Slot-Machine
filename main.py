MAX_LINES = 3 #Global Constant
MAX_BET = 100
MIN_BET = 10

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

def get_bet():
    while True:
        bet = input("what would you like to bet?$ ") #string_conversion and concatanation
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: #checking if value is inbetween
                break
            else:
                print(f"Please enter a valid number of bet inbetween ${MIN_BET} and ${MAX_BET}") #string conversion with fuction 
        else:
            print("Please enter a number")
    return bet

        
def main():
    balance = deposite() #function call
    lines = get_no_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    

main()
    
    