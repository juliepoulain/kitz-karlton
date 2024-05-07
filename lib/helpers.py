# lib/helpers.py

from models.reservation import Reservation
from models.owner import Owner
from models.cat import Cat
import ipdb

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
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: See all Reservations")
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
    elif choice == "5":
        update_reservation()

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
    print("Please enter valid phone number")
    phone_number = input("> ")
    if (
        phone_number.isnumeric() == True
        and len(phone_number) == 10
    ):
        phone_number = int(phone_number)
        check_length_of_stay(phone_number)
        return phone_number
    else:
        print("INVALID: Phone number must be 10 digits with no spaces")
        create_reservation()

def check_length_of_stay(phone_number):
    print("Please enter valid length of stay")
    length_of_stay = input("> ")
    if (
        length_of_stay.isnumeric() == True
        and 0 < int(length_of_stay) < 15
    ):
        length_of_stay = int(length_of_stay)
        check_hotel_room_number(phone_number, length_of_stay)
        return length_of_stay
    else: 
        print("INVALID: Length of stay must be an integer between 1-14")
        check_length_of_stay(phone_number)

def check_hotel_room_number(phone_number, length_of_stay):
    print("Please enter valid hotel room number")
    hotel_room_number = input("> ")
    if (
        hotel_room_number.isnumeric() == True
        and 0 < int(hotel_room_number) < 11
    ):
        hotel_room_number = int(hotel_room_number)
        print("Thank you for making a reservation!")
        print("Reservation Details:")
        new_reservation = Reservation.create(phone_number, length_of_stay, hotel_room_number)
        print(Reservation.find_by_phone(phone_number))
        return new_reservation
    else:
        print("INVALID: Hotel Room Number must be an integer between 1-10")
        check_hotel_room_number(phone_number, length_of_stay)

def update_reservation():
    print(Reservation.get_all())
    print("Please enter the ID for the reservation you would like to update")
    id = input("> ")
    res_to_update = Reservation.find_by_id(id)
    print(Reservation.find_by_id(id))
    specify_reservation_update(res_to_update)

def specify_reservation_update(res_to_update):
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Update Phone Number")
    print("4: Update Length of Stay")
    print("5: Update Hotel Room Number")
    print("6: Delete Reservation")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        print("Please enter new phone number")
        res_to_update.phone_number = int(input("> "))
        res_to_update.update()
        print("Phone Number updated successfully:")
        print(res_to_update)














































































# HOLLIS WORK HERE






