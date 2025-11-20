import re

def primary_inputs():
    while True:
        try:
            customer_name = input("\nplease enter your name please: ").title()
        except ValueError:
            print("invalid data type for customer name inputted. \n")
            continue
        if len(customer_name) <= 1:
            print("NOTE: No name or invalid name length inputted, did you mean to input a valid name? \n")
            continue
        if any(char.isdigit() for char in customer_name) == True:
            print("no digits are allowed, please only enter text. \n")
            continue
    
        while True:
            address_pattern = r"^[\d+ 0-9]{1,3}\s+[a-z A-Z]{3,16}\s+[a-z A-Z]{4,7}$"
            user_address_1 = input("\nPlease input your door number and street name: ")
            if len(user_address_1) <= 0:
                print("NOTE: No address 1 inputted, did you mean to input your address? \n")
                continue
            if any(char.isdigit() for char in user_address_1) == False:
                print("no door number inputted, please input your door number as well as your street name. \n")
                continue
            if re.fullmatch(address_pattern, user_address_1) is None:
                print("L")
                continue
            break
        while True:
            user_address_2 = input("\nplease input your village or town of residence (optional): ")
            user_address_3 = input("\nplease input your county (optional): ")
        
            break
        while True:
            try:
                phone_pattern = r"^\d{10,11}$"
                user_phone_number = int(input("\nplease enter your phone number: "))
            except ValueError:
                print("invalid data type entered. \n")
                continue
            break
        break

def secondary_inputs():
    while True:
        try:
            
    
print(primary_inputs())