# lib/helpers.py

from models.reservation import Reservation
from models.owner import Owner
from models.cat import Cat
import time
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
    print("Cat Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: See all Cats")
    print("4: Create Cat")
    print("5: Update Cat")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        print(Cat.get_all())
        employee_manage_cat()
    elif choice == "4":
        print("Cat owner must exist to create cat")
        print("1: Create Cat Owner")
        print("2: Owner exists - Create Cat")
        cat_choice = input("> ")
        if cat_choice == "1":
            create_owner()
        elif cat_choice == "2":
            print("Cat owner must have valid owner ID")
            print("1: See all Owner information")
            print("2: Owner ID Known - Create Cat")
            owner_id_choice = input("> ")
            if owner_id_choice == "1":
                print(Owner.get_all())
                print("Owner ID ready?")
                print("0: Exit Program")
                print("1: Yes")
                print("2: Return to Main Menu")
                print("3: Return to Employee Portal")
                owner_id_ready = input("> ")
                if owner_id_ready == "0":
                    exit_program()
                if owner_id_ready == "1":
                    create_cat()
                elif owner_id_ready == "2":
                    main_menu()
                elif owner_id_ready == "3":
                    employee_portal()
            elif owner_id_choice == "2":
                create_cat()


def create_reservation():
    print("Please enter valid phone number")
    phone_number = input("> ")
    if phone_number.isnumeric() == True and len(phone_number) == 10:
        phone_number = int(phone_number)
        check_length_of_stay(phone_number)
        return Reservation.find_by_phone(phone_number)
    else:
        print("INVALID: Phone number must be 10 digits with no spaces")
        print("0. Exit Program")
        print("1. Try again")
        create_reservation_choice = input("> ")
        if create_reservation_choice == "0":
            exit_program()
        elif create_reservation_choice == "1":
            create_reservation()


def check_length_of_stay(phone_number):
    print("Please enter valid length of stay")
    length_of_stay = input("> ")
    if length_of_stay.isnumeric() == True and 0 < int(length_of_stay) < 15:
        length_of_stay = int(length_of_stay)
        check_hotel_room_number(phone_number, length_of_stay)
        return length_of_stay
    else:
        print("INVALID: Length of stay must be an integer between 1-14")
        check_length_of_stay(phone_number)


def check_hotel_room_number(phone_number, length_of_stay):
    print("Please enter valid hotel room number")
    hotel_room_number = input("> ")
    if hotel_room_number.isnumeric() == True and 0 < int(hotel_room_number) < 11:
        hotel_room_number = int(hotel_room_number)
        print("Thank you for making a reservation!")
        print("Reservation Details:")
        new_reservation = Reservation.create(
            phone_number, length_of_stay, hotel_room_number
        )
        print(Reservation.find_by_phone(phone_number))
        return new_reservation
    else:
        print("INVALID: Hotel Room Number must be an integer between 1-10")
        check_hotel_room_number(phone_number, length_of_stay)


def create_owner():
    ### must return owner object and/or owner ID
    ### also give option to create cat immediately?
    pass


ACCEPTED_BREEDS = [
    "tabby",
    "calico",
    "shorthair",
    "siamese",
    "maine coon",
    "persian",
    "ragdoll",
    "sphynx",
    "scottish fold",
]


def create_cat():
    print("Please enter valid cat name")
    name = input("> ")
    if isinstance(name, str) and 0 < len(name) <= 30:
        check_cat_breed(name)
    else:
        print("INVALID: Name must be a non-empty string of 30 or fewer characters")
        create_cat()


def check_cat_breed(name):
    print("Please enter valid cat breed")
    breed = input("> ")
    if ACCEPTED_BREEDS.count(breed.lower()) > 0:
        breed = breed.lower()
        check_cat_age(name, breed)
        return breed
    else:
        print("INVALID: Cat breed must be listed in accepted breeds")
        print(f"Accepted breeds:\n {ACCEPTED_BREEDS}")
        check_cat_breed(name)


def check_cat_age(name, breed):
    print("Please enter valid cat age in years")
    age = input("> ")
    if age.isnumeric() and 0 < int(age) <= 30:
        age = int(age)
        check_cat_spice(name, breed, age)
        return age
    else:
        print("INVALID: Age must be positive integer fewer than 31")
        check_cat_age(name, breed)


def check_cat_spice(name, breed, age):
    print("Please enter valid cat spice level")
    spice_level = input("> ")
    if spice_level.isnumeric() and 1 <= int(spice_level) <= 5:
        spice_level = int(spice_level)
        check_cat_owner(name, breed, age, spice_level)
        return spice_level
    else:
        print("INVALID: Cat spice level must be an integer between 1 and 5, inclusive")
        check_cat_spice(name, breed, age)


def check_cat_owner(name, breed, age, spice_level):
    print("See list of all owner IDs? (Y/N)")
    choice_view_owner_ids = input("> ")
    if choice_view_owner_ids == "Y":
        print(Owner.get_all())
    print("Please enter valid owner ID")
    owner_id = input("> ")
    if owner_id.isnumeric() and Owner.find_by_id(int(owner_id)):
        owner_id = int(owner_id)
        print("New Cat Details:")
        new_cat = Cat.create(name, breed, age, spice_level, owner_id)
        print(Cat.find_by_id(new_cat.id))
        time.sleep(2)
        print("What would you like to do next?")
        print("0. Exit Program")
        print("1. Return to Main Menu")
        print("2. Return to Employee Portal")
        print("3. Update cat")
        print("4. Add another cat")
        if input("> ") == "0":
            exit_program()
        elif input("> ") == "1":
            main_menu()
        elif input("> ") == "2":
            employee_portal()
        elif input("> ") == "3":
            print(f"update {new_cat}")
        elif input("> ") == "4":
            employee_manage_cat()
        return new_cat
    else:
        print("INVALID: Owner ID must be an existing owner ID")
        check_cat_owner(name, breed, age, spice_level)
