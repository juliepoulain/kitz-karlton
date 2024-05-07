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
    print("Type 'exit' at any time to exit the program")
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
    elif choice == "exit":
        exit_program()

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
    elif choice == "exit":
        exit_program()

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
    elif choice == "exit":
        exit_program()

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
    elif choice == "exit":
        exit_program()

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
                elif owner_id_ready == "exit":
                    exit_program()
            elif owner_id_choice == "2":
                create_cat()
            elif owner_id_choice == "exit":
                exit_program()
    elif choice == "5":
        update_cat()
    elif choice == "exit":
        exit
    else:
        print("Please enter valid menu option")
        time.sleep(1)
        employee_manage_cat()

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
    elif name == "exit":
        exit_program()
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
    elif breed == "exit":
        exit_program()
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
    elif age == "exit":
        exit_program()
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
    elif spice_level == "exit":
        exit_program()
    else:
        print("INVALID: Cat spice level must be an integer between 1 and 5, inclusive")
        check_cat_spice(name, breed, age)

def check_cat_owner(name, breed, age, spice_level):
    print("See list of all owner IDs? (Y/N)")
    choice_view_owner_ids = input("> ")
    if choice_view_owner_ids.upper() == "Y":
        print(Owner.get_all())
    elif choice_view_owner_ids == "exit":
        exit_program()
    print("Please enter valid owner ID")
    owner_id = input("> ")
    if owner_id.isnumeric() and Owner.find_by_id(int(owner_id)):
        owner_id = int(owner_id)
        print("New Cat Details:")
        new_cat = Cat.create(name, breed, age, spice_level, owner_id)
        print(Cat.find_by_id(new_cat.id))
        time.sleep(1)
        print("What would you like to do next?")
        print("0. Exit Program")
        print("1. Return to Main Menu")
        print("2. Return to Employee Portal")
        print("3. Update cat")
        print("4. Add another cat")
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main_menu()
        elif choice == "2":
            employee_portal()
        elif choice == "3":
            print(f"update {new_cat}")
        elif choice == "4":
            create_cat()
        elif choice == "exit":
            exit_program()
        return new_cat
    elif owner_id == "exit":
        exit_program()
    else:
        print("INVALID: Owner ID must be an existing owner ID")
        check_cat_owner(name, breed, age, spice_level)

def update_cat():
    print(Cat.get_all())
    print("Please enter the ID for the cat you would like to update")
    entered_id = input("> ")
    if (
        entered_id.isnumeric() and Cat.find_by_id(int(entered_id))
    ):
        cat_to_update = Cat.find_by_id(entered_id)
        specify_cat_update(cat_to_update)
    else:
        print("INVALID: Entered ID must exist in database.")
        update_cat()

def specify_cat_update(cat_to_update):
    print(f"Selected Cat:\n {cat_to_update}")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Update Name for selected cat")
    print("4: Update Breed for selected cat")
    print("5: Update Age for selected cat")
    print("6: Update Spice Level for selected cat")
    print("7: Update Owner ID for selected cat")
    print("8: Delete selected cat")
    print("9: Choose a different cat to update")
    choice = input("> ")
    if choice == "0": 
        exit_program()
    elif choice == "1":
        return_main_menu()
    elif choice == "2":
        employee_portal()
    elif choice == "3":
        enter_new_cat_name(cat_to_update)
    elif choice == "4":
        enter_new_cat_breed(cat_to_update)
    elif choice == "5":
        enter_new_cat_age(cat_to_update)
    elif choice == "6":
        enter_new_cat_spice_level(cat_to_update)
    elif choice == "7":
        enter_new_cat_owner_id(cat_to_update)
    elif choice == "8":
        delete_selected_cat(cat_to_update)
    elif choice == "9":
        update_cat()

def enter_new_cat_name(cat_to_update):
    print(f"Selected Cat: {cat_to_update}")
    print("Please enter new name")
    new_name = input("> ")
    if 0 < len(new_name) <= 30:
        cat_to_update.name = new_name
        cat_to_update.update()
        print("Cat Name has been updated successfully!")
        print("Updated Cat Details:")
        print(cat_to_update)
        print("Continue to update this cat? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or "y":
            specify_cat_update(cat_to_update)
        else:
            update_cat()
    else:
        print("INVALID: Name must be a non-empty string of 30 or fewer characters")
        time.sleep(1)
        enter_new_cat_name(cat_to_update)

def enter_new_cat_breed(cat_to_update):
    print(f"Selected Cat: {cat_to_update}")
    print("Please enter new breed")
    new_breed = input("> ")
    if ACCEPTED_BREEDS.count(new_breed.lower()) > 0:
        cat_to_update.breed = new_breed.lower()
        cat_to_update.update()
        print("Cat Breed has been updated successfully!")
        print("Updated Cat Details:")
        print(cat_to_update)
        print("Continue to update this cat? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or "y":
            specify_cat_update(cat_to_update)
        else:
            update_cat()
    else:
        print("INVALID: Cat breed must be listed in accepted breeds")
        time.sleep(1)
        print(f"Accepted breeds:\n {ACCEPTED_BREEDS}")
        time.sleep(1)
        enter_new_cat_breed(cat_to_update)

def enter_new_cat_age(cat_to_update):
    print(f"Selected Cat: {cat_to_update}")
    print("Please enter new cat age")
    new_age = input("> ")
    if new_age.isnumeric() and 0 < int(new_age) <= 30:
        cat_to_update.age = int(new_age)
        cat_to_update.update()
        print("Cat Age has been updated successfully!")
        print("Updated Cat Details:")
        print(cat_to_update)
        print("Continue to update this cat? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or "y":
            specify_cat_update(cat_to_update)
        else:
            update_cat()
    else:
        print("INVALID: Age must be positive integer fewer than 31")
        time.sleep(1)
        enter_new_cat_age(cat_to_update)

def enter_new_cat_spice_level(cat_to_update):
    print(f"Selected Cat: {cat_to_update}")
    print("Please enter new cat spice level")
    new_spice_level = input("> ")
    if new_spice_level.isnumeric() and 1 <= int(new_spice_level) <= 5:
        cat_to_update.spice_level = int(new_spice_level)
        cat_to_update.update()
        print("Cat Spice Level has been updated successfully!")
        print("Updated Cat Details:")
        print(cat_to_update)
        print("Continue to update this cat? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or "y":
            specify_cat_update(cat_to_update)
        elif choice == "exit":
            exit_program()
        else:
            update_cat()
    elif new_spice_level == "exit":
        exit_program()
    else:
        print("INVALID: Cat spice level must be an integer between 1 and 5, inclusive")
        time.sleep(1)
        enter_new_cat_spice_level(cat_to_update)

def enter_new_cat_owner_id(cat_to_update):
    print(f"Selected Cat: {cat_to_update}")
    print("See list of all owner IDs? (Y/N)")
    choice_view_owner_ids = input("> ")
    if choice_view_owner_ids.upper() == "Y":
        print(Owner.get_all())
    elif choice_view_owner_ids == "exit":
        exit_program()
    print("Please enter new owner ID")
    new_owner_id = input("> ")
    if new_owner_id.isnumeric() and Owner.find_by_id(int(new_owner_id)):
        cat_to_update.owner_id = int(new_owner_id)
        cat_to_update.update()
        print("Cat Owner ID has been updated successfully!")
        print("Updated Cat Details:")
        print(cat_to_update)
        print("Continue to update this cat? Enter Y or N")
        choice = input("> ")
        if choice == "Y" or "y":
            specify_cat_update(cat_to_update)
        elif choice == "exit":
            exit_program()
        else:
            update_cat()
    elif new_owner_id == "exit":
        exit_program()
    else:
        print("INVALID: Owner ID must be an existing owner ID")
        time.sleep(1)
        enter_new_cat_owner_id(cat_to_update) 

def delete_selected_cat(cat_to_update):
    print("Are you sure you want to delete selected cat? Enter Y or N")
    print(f"Selected Cat Details:\n {cat_to_update}")
    choice = input("> ")
    if choice.upper() == "Y":
        cat_to_update.delete()
        specify_cat_update(cat_to_update)
    elif choice == "exit":
        exit_program()
    else:
        specify_cat_update(cat_to_update)
       
      
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






























































































        
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
        final_res_create(phone_number, length_of_stay, hotel_room_number)
    else:
        print("INVALID: Hotel Room Number must be an integer between 1-10")
        check_hotel_room_number(phone_number, length_of_stay)

def final_res_create(phone_number, length_of_stay, hotel_room_number):
    hotel_room_number = int(hotel_room_number)
    print("Reservation Details:")
    new_reservation = Reservation.create(phone_number, length_of_stay, hotel_room_number)
    print(Reservation.find_by_phone(phone_number))
    print("Returning to menu options...")
    time.sleep(1)
    print("Menu Options:")
    print("0: Exit Program")
    print("1: Return to Main Menu")
    print("2: Return to Employee Portal")
    print("3: Create another reservation")
    print("4: Update this Reservation")
    print("5: Delete this Reservation")
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