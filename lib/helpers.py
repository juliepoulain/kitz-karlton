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
        print(Reservation.get_all())
        employee_manage_res()
    elif choice == "4":
        create_reservation()
    elif choice == "5":
        update_reservation()

def employee_manage_owner():
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: See all Owners")
    print("4: Create Owner")
    print("5: Update Owner")
    print("6: View specific Owner")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        print(Owner.get_all())
        employee_manage_owner()
    elif choice == "4":
        create_owner()
    elif choice == "5":
        update_owner()
    elif choice == "6":
        specific_owner()


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
      
      
      
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
























































































































































































































































# julie works here
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
        print("Thank you for making a reservation!")
        hotel_room_number = int(hotel_room_number)
        Reservation.create(phone_number, length_of_stay, hotel_room_number)
        final_res_create(phone_number, length_of_stay, hotel_room_number)
    else:
        print("INVALID: Hotel Room Number must be an integer between 1-10")
        check_hotel_room_number(phone_number, length_of_stay)

def final_res_create(phone_number, length_of_stay, hotel_room_number):
    print("Reservation Details:")
    print(Reservation.find_by_phone(phone_number))
    print("Returning to menu options...")
    time.sleep(1)
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Create another reservation")
    print("4: Update selected Reservation")
    print("5: Delete selected Reservation")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        create_reservation()
    elif choice == "4":
        res_to_update = Reservation.find_by_phone(phone_number)
        specify_reservation_update(res_to_update)
    elif choice == "5":
        res_to_update = Reservation.find_by_phone(phone_number)
        delete_selected_reservation(res_to_update)
    else:
        print("INVALID: entered value must be a number from given menu options")
        final_res_create(phone_number, length_of_stay, hotel_room_number)

def update_reservation():
    print(Reservation.get_all())
    print("Please enter the ID (listed above) for the reservation you would like to update")
    entered_id = input("> ")
    if (
        entered_id.isnumeric() and Reservation.find_by_id(int(entered_id))
    ):
        res_to_update = Reservation.find_by_id(entered_id)
        specify_reservation_update(res_to_update)
    else:
        print("INVALID: ID must be an existing Reservation ID")
        update_reservation()

def specify_reservation_update(res_to_update):
    print(f"Selected Reservation: {res_to_update}")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Update Phone Number for selected reservation")
    print("4: Update Length of Stay for selected reservation")
    print("5: Update Hotel Room Number for selected reservation")
    print("6: Delete selected reservation")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        enter_new_phone(res_to_update)
    elif choice == "4":
        enter_new_length_of_stay(res_to_update)
    elif choice == "5":
        enter_new_hotel_room(res_to_update)
    elif choice == "6":
        delete_selected_reservation(res_to_update)
    else:
        print("INVALID: entered value must be a number from given menu options")
        specify_reservation_update(res_to_update)
        

def enter_new_phone(res_to_update):
    print(f"Selected Reservation: {res_to_update}")
    print("Please enter new phone number")
    new_phone = input("> ")
    if (
        new_phone.isnumeric() == True
        and len(new_phone) == 10
    ):
        res_to_update.phone_number = int(new_phone)
        res_to_update.update()
        print("Phone Number has been updated successfully!")
        print("Updated Reservation Details:")
        print(res_to_update)
        print("Continue to update this reservation? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_reservation_update(res_to_update)
        else:
            update_reservation()
    else: 
        print("INVALID: Phone number must be 10 digits with no spaces")
        enter_new_phone(res_to_update)

def enter_new_length_of_stay(res_to_update):
    print(f"Selected Reservation: {res_to_update}")
    print("Please enter new length of stay for selected reservation")
    new_length = input("> ")
    if (
        new_length.isnumeric() == True
        and 0 < int(new_length) < 15
    ):
        res_to_update.length_of_stay = int(new_length)
        res_to_update.update()
        print("Length of Stay has been updated successfully!")
        print("Updated Reservation Details:")
        print(res_to_update)
        print("Continue to update this reservation? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_reservation_update(res_to_update)
        else:
            update_reservation()
    else: 
        print("INVALID: Length of stay must be an integer between 1-14")
        enter_new_length_of_stay(res_to_update)

def enter_new_hotel_room(res_to_update):
    print(f"Selected Reservation: {res_to_update}")
    print("Please enter new hotel room for selected reservation")
    new_room = input("> ")
    if (
        new_room.isnumeric() == True
        and 0 < int(new_room) < 11
    ):
        res_to_update.hotel_room_number = int(new_room)
        res_to_update.update()
        print("Hotel Room Number has been updated successfully!")
        print("Updated Reservation Details:")
        print(res_to_update)
        print("Continue to update this reservation? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_reservation_update(res_to_update)
        else:
            update_reservation()
    else: 
        print("INVALID: Hotel Room must be an integer between 1-10")
        enter_new_hotel_room(res_to_update)

def delete_selected_reservation(res_to_update):
    print(f"Selected Reservation: {res_to_update}")
    print("Are you sure you want to delete this reservation? Enter Y or N")
    choice = input("> ")
    if choice == "Y" or choice == "y":
        res_to_update.delete()
        print("Reservation deleted successfully!")
        print("Returning to manage reservations...")
        time.sleep(1)
        employee_manage_res()
    else:
        specify_reservation_update(res_to_update)

def create_owner():
    print("Please enter owner's name")
    entered_name = input("> ")
    if (
        isinstance(entered_name, str) 
        and 0 < len(entered_name) <= 20
    ):
        check_owner_phone_number(entered_name)
    else:
        print("INVALID: Name must be a valid string between 1-20 characters")
        create_owner()

def check_owner_phone_number(entered_name):
    print("Please enter owner's phone number")
    entered_phone = input("> ")
    if (
        entered_phone.isnumeric() == True
        and len(entered_phone) == 10
    ):
        entered_phone = int(entered_phone)
        check_owner_address(entered_name, entered_phone)
    else:
        print("INVALID: Phone number must be 10 digits with no spaces")
        check_owner_phone_number(entered_name)

def check_owner_address(entered_name, entered_phone):
    print("Please enter owner's address")
    entered_address = input("> ")
    if (
        isinstance(entered_address, str)
        and 0 < len(entered_address)
    ):
        Owner.create(entered_name, entered_phone, entered_address)
        print("Thank you for creating a new owner!")
        final_owner_create(entered_name, entered_phone, entered_address)
    else:
        print("INVALID: Address must be a string")
        check_owner_address(entered_name, entered_phone)

def final_owner_create(entered_name, entered_phone, entered_address):
    print("Owner Details:")
    print(Owner.find_by_phone(entered_phone))
    print("Returning to menu options...")
    time.sleep(1)
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Create another owner")
    print("4: Update selected owner")
    print("5: Delete selected owner")
    print("6: Create a cat for selected owner")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        create_owner()
    elif choice == "4":
        owner_to_update = Owner.find_by_phone(entered_phone)
        specify_owner_update(owner_to_update)
    elif choice == "5":
        owner_to_update = Owner.find_by_phone(entered_phone)
        delete_selected_owner(owner_to_update)
    elif choice == "6":
        cat_owner = Owner.find_by_phone(entered_phone)
        create_cat(cat_owner.id)
    else:
        print("INVALID: entered value must be a number from given menu options")
        final_owner_create(entered_name, entered_phone, entered_address)
        
def update_owner():
    print(Owner.get_all())
    print("Please enter the ID (listed above) for the owner you would like to update")
    entered_id = input("> ")
    if (
        entered_id.isnumeric() and Owner.find_by_id(int(entered_id))
    ):
        owner_to_update = Owner.find_by_id(entered_id)
        specify_owner_update(owner_to_update)
    else:
        print("INVALID: ID must be an existing Owner ID")
        update_owner()

def specify_owner_update(owner_to_update):
    print(f"Selected Owner: {owner_to_update}")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Update Name for selected owner")
    print("4: Update Phone Number for selected owner")
    print("5: Update Address for selected owner")
    print("6: Delete selected reservation")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        enter_new_owner_name(owner_to_update)
    elif choice == "4":
        enter_new_owner_phone(owner_to_update)
    elif choice == "5":
        enter_new_owner_address(owner_to_update)
    elif choice == "6":
        delete_selected_owner(owner_to_update)
    else:
        print("INVALID: entered value must be a number from given menu options")
        specify_owner_update(owner_to_update)

def enter_new_owner_name(owner_to_update):
    print(f"Selected Owner: {owner_to_update}")
    print("Please enter new owner name")
    new_name = input("> ")
    if (
        isinstance(new_name, str) 
        and 0 < len(new_name) <= 20
    ):
        owner_to_update.name = new_name
        owner_to_update.update()
        print("Owner Name has been updated successfully!")
        print("Updated Reservation Details:")
        print(owner_to_update)
        print("Continue to update this owner information? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_owner_update(owner_to_update)
        else:
            employee_manage_owner()
    else: 
        print("INVALID: Phone number must be 10 digits with no spaces")
        enter_new_owner_name(owner_to_update)

def enter_new_owner_phone(owner_to_update):
    print(f"Selected Owner: {owner_to_update}")
    print("Please enter new phone number")
    new_phone = input("> ")
    if (
        new_phone.isnumeric() == True
        and len(new_phone) == 10
    ):
        owner_to_update.phone_number = int(new_phone)
        owner_to_update.update()
        print("Phone Number has been updated successfully!")
        print("Updated Reservation Details:")
        print(owner_to_update)
        print("Continue to update this owner? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_owner_update(owner_to_update)
        else:
            employee_manage_owner()
    else: 
        print("INVALID: Phone number must be 10 digits with no spaces")
        enter_new_owner_phone(owner_to_update)

def enter_new_owner_address(owner_to_update):
    print(f"Selected Owner: {owner_to_update}")
    print("Please enter new address for selected owner")
    new_address = input("> ")
    if (
        isinstance(new_address, str)
        and 0 < len(new_address)
    ):
        owner_to_update.address = new_address
        owner_to_update.update()
        print("Address has been updated successfully!")
        print("Updated Owner Details:")
        print(owner_to_update)
        print("Continue to update this owner? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            specify_owner_update(owner_to_update)
        else:
            employee_manage_owner()
    else: 
        print("INVALID: Address must be string")
        enter_new_owner_address(owner_to_update)

def delete_selected_owner(owner_to_update):
    print(f"Selected Owner: {owner_to_update}")
    print("Are you sure you want to delete this owner? Enter Y or N")
    choice = input("> ")
    if choice == "Y" or choice == "y":
        owner_to_update.delete()
        print("Owner deleted successfully!")
        print("Returning to manage owners...")
        time.sleep(1)
        employee_manage_owner()
    else:
        specify_owner_update(owner_to_update)


def specific_owner():
    print(Owner.get_all())
    print("Please enter the ID (listed above) for the owner you would like to view")
    entered_id = input("> ")
    if (
        entered_id.isnumeric() and Owner.find_by_id(int(entered_id))
    ):
        print(Owner.find_by_id(entered_id))
        view_owner = Owner.find_by_id(entered_id)
        print("See this owner's cats? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or choice == "y":
            print(view_owner.get_cats())
            employee_manage_owner()
        else:
            employee_manage_owner()
    else:
        print("INVALID: ID must be an existing Owner ID")
        specific_owner()

