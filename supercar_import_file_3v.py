

def primary_inputs():
    import re
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
            user_phone_number = input("\nplease enter your phone number: ")
            if any(char.isdigit() for char in user_phone_number) == False:
                print("phone number must only contain digits. \n")
                continue
            if len(user_phone_number) < 10 or len(user_phone_number) > 11:
                print("invalid phone number length. \n")
                continue
            break
        export_list = [customer_name, user_address_1, user_address_2, user_address_3, user_phone_number]
        def exports():
            print("your personal info: \n")
            print("your name is: " + export_list[0] + "\n")
            print("your door number and street name are: " + export_list[1] + "\n")
            print("your village or town of residence is: " + export_list[2] + "\n")
            print("your county is: " + export_list[3] + "\n")  
            print("your phone number is: " + export_list[4] + "\n")              
        return export_list, exports()
        break
        

def secondary_inputs():
    while True:
        try:
            cars_amount = int(input("How many cars do you want to test? (max of 5)"))
        except ValueError:
            print("invalid data type for the amount of cars inputted. \n")
            continue
        if cars_amount <= 0:
            print("You did not place a valid number for the amount of cars you want to input, would you like to try again?")
            continue
        if cars_amount >= 5:
            print("The max of cars you can test is 5")
            continue
            
