# lib/helpers.py

from models.reservation import Reservation
from models.owner import Owner
from models.cat import Cat

def greeting():
    print("Welcome to the Kitz Karlton!")
    print("            ♡   ╱|、")
    print("               (˚ˎ 。7")
    print("                |、˜〵")
    print("                じしˍ,)ノ")

def main_menu():
    print("To select a menu option, please type in a number and hit enter")
    print("0: Exit Program")
    print("1: Make a Reservation")
    print("2: Employee Portal")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        print("res portal")
    elif choice == "2":
        employee_portal()

def exit_program():
    print("Goodbye!")
    exit()

def return_main_menu():
    main_menu()

def employee_portal():
    print("Welcome to the employee Portal!")
    print("To select a menu option, please type in a number and hit enter")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Manage Reservations")
    print("3: Manage Owners")
    print("4: Manage Cats")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_manage_res()
    elif choice == "3":
        employee_manage_owner()
    elif choice == "4":
        employee_manage_cat()
    
def employee_manage_res():
    print("Reservation data:")
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: See all")
    print("4: Create Reservation")
    print("5: Update Reservation")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        Reservation.get_all()
    elif choice == "4":
        create_reservation()

def employee_manage_owner():
    print("Owner data:")
    print(Owner.get_all())
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()

def employee_manage_cat():
    print("Cat data:")
    print(Cat.get_all())
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()

def create_reservation():
    print("Please input phone number")
    phone_number = input("> ")
    if (
            isinstance(phone_number, int) 
            and len(str(phone_number)) == 10
        ):
        print("Please enter length of stay")
        length_of_stay = input("> ")
        if length_of_stay:
            print("Please enter hotel room number")
            hotel_room_number = input("> ")
            Reservation.create(phone_number, length_of_stay, hotel_room_number)
        else:
            length_of_stay()
    else:
        print("INVALID: Phone number must be 10 digits with no spaces")
        create_reservation()
    

def create_length_of_stay():
    print("Please enter length of stay")
        length_of_stay = input("> ")
        if length_of_stay:
            print("Please enter hotel room number")
            hotel_room_number = input("> ")
            Reservation.create(phone_number, length_of_stay, hotel_room_number)
        else:
            print("INVALID: Phone number must be 10 digits with no spaces")
            create_reservation()


















































































# HOLLIS WORK HERE






