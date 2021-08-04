# Created by Adam Jost 08/02/2021
      
def get_account_balance_from_file():
    i = open('account_balance.txt', 'r') 
    account_balance = float(i.read())
    i.close()
    return account_balance

def print_heading_and_command_key():
    print_heading()
    print_command_key()
    
def print_heading():
    print_separator('=')
    print_centered_text("WELCOME TO SAINT CHARLES COMMUNITY BANK ATM")
    print_separator('=')
    
def print_command_key():
    commands = ["DEPOSIT", "WITHDRAWAL", "BALANCE", "QUIT"]
    command_descriptions = ["Deposit money into your account", 
                        "Withdrawal money from your account", 
                        "View the current balance of your account",
                        "Quit and exit the system"]
    print_centered_text("Available Commands List")
    print_separator('-')
    print_commands_and_descriptions(commands, command_descriptions)
    print_separator('=')
    print_centered_text("Type any above command to continue")
    print_separator('=')
    
def print_separator(separator_char):
    separator = separator_char * 60
    print(separator)

def print_centered_text(text_to_center):
    half_of_gui = 30
    half_of_text = len(text_to_center) / 2
    
    num__of_spaces_to_print = (int) (half_of_gui - half_of_text)
    centering_space = ' ' * num__of_spaces_to_print
    
    print(centering_space, end='')
    print(text_to_center)

def print_commands_and_descriptions(commands, description):
    i = 0
    while i < len(commands):
        print(commands[i] + " - " + description[i])
        i += 1

def get_user_command():
    command = str(input("Enter the operation command you would like to perform: \n"))
    return command.lower().strip()

def print_invalid_command_msg(command):
    print("* Error: " + command + " is not a valid command.")

def print_value_error_msg():
    print("* Error: Invalid dollar amount.")
    
def print_amount_is_negative_error_msg():
    print("* Error: Amount cannot be a negative amount.")
    
def request_deposit_amount():
    deposit_amount = 0
    while deposit_amount == 0: 
        try:
            deposit_amount = int(input("Please enter the amount you would like to deposit: \n"))
        except: 
            print_value_error_msg()
        if is_negative(deposit_amount):
                print_amount_is_negative_error_msg()
                deposit_amount = 0
    return deposit_amount
    
def request_withdrawal_amount():
    withdrawal_amount = 0
    while withdrawal_amount == 0: 
        try:
            withdrawal_amount = int(input("Please enter the amount you would like to withdrawal: \n"))
        except: 
            print_value_error_msg()
        if is_negative(withdrawal_amount):
                print_amount_is_negative_error_msg()
                withdrawal_amount = 0
    return withdrawal_amount

def is_negative(dollar_amount):
    amount_is_negative = dollar_amount < 0
    return amount_is_negative

def check_for_available_funds(account_balance, withdrawal_amount):
    funds_are_available = account_balance - withdrawal_amount >= 0
    return funds_are_available

def display_not_enough_funds_msg():
    print("* Error: You do not have enough funds for this transaction")

def deposit_into_account(account_balance, deposit_amount):
    account_balance += deposit_amount 
    display_new_account_balance(account_balance)
    return account_balance
    
def withdrawal_from_account(account_balance, withdrawal_amount):
    account_balance -= withdrawal_amount 
    display_new_account_balance(account_balance)
    display_warning_when_balance_is_low(account_balance)
    return account_balance
    
def display_account_balance(account_balance):
    print("Your current account balance is ${0:.2f}".format(account_balance))
    
def display_new_account_balance(account_balance):
    print("Your new account balance is ${0:.2f}".format(account_balance))
    
def display_warning_when_balance_is_low(account_balance):
    if account_balance < 100: 
        print("* Warning: Your current balance is less than $100.00")

def print_ending_balance_to_file(account_balance):
    o = open('account_balance.txt', 'w')
    o.write(account_balance)
    o.close()

def print_thank_you_message():
    print_separator('=')
    print_centered_text("Thank you for choosing Saint Charles Community Bank ATM")
    print_separator('=')
    
def exit_system(account_balance):
    print_ending_balance_to_file("{0:.2f}".format(account_balance))
    print_thank_you_message()

def main():
    account_balance = get_account_balance_from_file()
    print_heading_and_command_key()
        
    while True: 
        command = get_user_command()
        
        if command == "deposit":
            deposit_amount = request_deposit_amount()
            deposit_into_account(account_balance, deposit_amount)
        elif command == "withdrawal":
            withdrawal_amount = request_withdrawal_amount()
            if check_for_available_funds(account_balance, withdrawal_amount):
                account_balance = withdrawal_from_account(account_balance, withdrawal_amount)
            else:
                display_not_enough_funds_msg()
        elif command == "balance":
            display_account_balance(account_balance)
        elif command == "quit":
            exit_system(account_balance)
            break;
        else: 
            print_invalid_command_msg(command)

if __name__=="__main__":
    main()