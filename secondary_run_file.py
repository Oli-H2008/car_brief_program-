import supercar_import_file4v
import Main_run_file



export_list = [customer_name, user_address_1, user_address_2, user_address_3, user_phone_number]
def exports():
    print("your personal info: \n")
    print("your name is: " + export_list[0] + "\n")
    print("your door number and street name are: " + export_list[1] + "\n")
    print("your village or town of residence is: " + export_list[2] + "\n")
    print("your county is: " + export_list[3] + "\n")  
    print("your phone number is: " + export_list[4] + "\n")              
    return export_list, exports()