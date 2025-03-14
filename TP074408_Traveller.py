import json
def login():
    print('Welcome!\n')
    while True:
        username = input('Hello ! Please enter your username:').lower()
        password = input('Hello ! Please enter your password:').lower()
        print('\n')
        found_user=False
        with open('users.txt', 'r') as user_information:
            for line in user_information:
                columns = line.strip().split(',')
                user = columns[0]
                pwd = columns[1]
                if user == username and pwd == password and columns[2] == 'Traveller':
                    print('Login Successful!')
                    traveller_menu(username)
                    found_user=True
                    return
        if not found_user:
            print('Invalid username and password. Please try again.')
            ex_opt = input('Do you want to exit?(yes/no):')
            if ex_opt.lower() == 'yes':
                print('See You !')
            elif ex_opt.lower()=='no':
                login()
            else:
                print('Invalid option.')
                login()
                break

def traveller_menu(username):
    print('MAIN MENU\n')
    print(f'Nice to meet you!{username}!\nEnjoy Your Holiday!\n')
    print('1.My Profile')
    print('2.View My Booking')
    print('3.Searching')
    print('4.Logout')
    while True:
        opt = input('Please choose your selection:')
        print('-'*40)
        if opt =='1':
            user_profile(username)
            break
        elif opt =='2':
            booking_menu(username)
            break
        elif opt=='3':
            searching_menu(username)
            break
        elif opt =='4':
            logout(username)
            break
        else:
            print('Invalid Option.Please Try Again.')
            traveller_menu(username)
            break

def user_profile(username):
    print('My PROFILE\n')
    print('1.View Current Profile\n2.Update Current Profile\n3.Add Profile\n4.Delete Profile\n5.Exit ')
    while True:
        profile_opt=input('Please enter :')
        print('-'*40)
        if profile_opt=='1':
            view_profile(username)
            break
        elif profile_opt=='2':
            update_profile(username)
            break
        elif profile_opt=='3':
            add_profile(username)
            break
        elif profile_opt=='4':
            delete_profile(username)
            break
        elif profile_opt=='5':
            traveller_menu(username)
            break
        else:
            print("Invalid Input.Please Try Again.")
            continue



def view_profile(username):
    print('USER PROFILE\n')
    print('1.Group\n2.Individual\n3.Exit')
    while True:
        profile_opt=input('Category:')
        print('-' * 40)
        if profile_opt=='1':
            group_profile(username)
            break
        elif profile_opt=='2':
            individual_profile(username)
            break
        elif profile_opt=='3':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again.')
            continue

def group_profile(username):
    print('GROUP PROFILE\n')
    while True:
        groupid = input(f'Hello {username}! Please enter your group ID:')
        found_group = False
        with open('file.json', 'r') as file:
            data = json.load(file)
            group_profile = data['Groups']
            for gp in group_profile:
                if groupid == gp['Group ID']:
                    found_group = True
                    print('Found Your Profile!')
                    print(f'Group Number:{gp['Group Name']}')
                    print(f'Members: {gp['Number of Pax']}')
                    print(f'Company: {gp['Company']}')
                    print('-'*40)
                    while True:
                        exit_option = input('Do you want Exit?(yes/no):')
                        if exit_option.lower() == 'yes':
                            print('Back to Main Menu...')
                            traveller_menu(username)
                            return
                        elif exit_option.lower() == 'no':
                            break
                        else:
                            print('Invalid Option')
                    break
            else:
                print('Not Found.Please Try Again.')
                continue

def individual_profile(username):
    print('INDIVIDUAL PROFILE\n')
    while True:
        personal_username = input(f'Hello{username}! Please Enter Your Username:')
        found = False
        with open('file.json', 'r') as files:
            data= json.load(files)
            personal_profile = data['Individuals']
            for pro in personal_profile:
                if personal_username == pro['Username']:
                    found_group = True
                    print('Found Your Profile!')
                    print(f'Name:{pro['Name']}')
                    print(f'Phone Number: {pro['Phone Number']}')
                    print(f'Email: {pro['Email']}')
                    print('-'*40)
                    while True:
                        exit_option = input('Do you want Exit?(yes/no):')
                        if exit_option.lower() == 'yes':
                            print('Back to Main Menu...')
                            traveller_menu(username)
                            return
                        elif exit_option.lower() == 'no':
                            break
                        else:
                            print('Invalid Option')
                    break
            else:
                print('Not Found.Please Try Again.')
                continue

def update_profile(username):
    print('UPDATE PROFILE\n')
    print('1.Group\n2.Individual\n3.Exit')
    while True:
        profile_opt=input('Category:')
        print('-' * 40)
        if profile_opt=='1':
            updategrp_profile(username)
            break
        elif profile_opt=='2':
            updateind_profile(username)
            break
        elif profile_opt=='3':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again.')
            continue

def updategrp_profile(username):
    print('UPDATE GROUP PROFILE\n')
    groupid = input('Enter your group ID to update: ')
    with open('file.json', 'r')as file:
        data = json.load(file)
        group_profile = data['Groups']
        found_group = False
        for gp in group_profile:
            if groupid == gp["Group ID"]:
                found_group = True
                print('Group Found!')
                print('-'*40)
                new_number = input('Enter Your New Group Name:').strip()
                new_members = input('Enter Your New Number of Pax (eg:4 pax):').strip()
                new_contactnumber=input('Enter Your New Contact Number ').strip()
                new_company = input('Enter Your New Group Company:').strip()
                if not new_number or not new_members or not new_contactnumber or not new_company:
                    print("Invalid.")
                    print('-'*40)
                    update_profile(username)
                else:
                    gp['Group Name'] = new_number
                    gp['Number of Pax'] = new_members
                    gp['Contact Number'] = new_contactnumber
                    gp['Company'] = new_company
                    print('Group Profile Update Successful!')
                    with open('file.json', 'w') as file:
                        json.dump(data, file, indent=5)
                break
        if not found_group:
            print('Invalid.\nPlease Try Again.')
            print('-' * 40)
            update_profile(username)
    while True:
        exit_option = input('Do you want Exit?(yes/no):')
        if exit_option.lower() == 'yes':
            print('Back to Main Menu...')
            traveller_menu(username)
            return
        elif exit_option.lower() == 'no':
            update_profile(username)
            break
        else:
            print('Invalid Option')

def updateind_profile(username):
    print('UPDATE INDIVIDUAL PROFILE\n')
    user = input('Enter your Username to update: ')
    with open('file.json', 'r')as file:
        data = json.load(file)
        ind_profile = data['Individuals']
        found_ind = False
        for us in ind_profile:
            if user == us["Username"]:
                found_ind = True
                print('Profile Found!')
                print('-'*40)
                new_name = input('Enter Your New Name:').strip()
                new_phone = input('Enter Your New Phone:').strip()
                new_email = input('Enter Your New Email:').strip()
                if not new_name or not new_phone or not new_email:
                    print("Invalid.")
                    print('-'*40)
                    update_profile(username)
                else:
                    us['Name'] = new_name
                    us['Phone'] = new_phone
                    us['Email'] = new_email
                    print('Individual Profile Update Successful!')
                    with open('file.json', 'w') as file:
                        json.dump(data, file, indent=5)
                    break
        if not found_ind:
            print('Invalid.\nPlease Try Again.')
            print('-' * 40)
            update_profile(username)
    while True:
        exit_option = input('Do you want Exit?(yes/no):')
        if exit_option.lower() == 'yes':
            print('Back to Main Menu...')
            traveller_menu(username)
            return
        elif exit_option.lower() == 'no':
            updateind_profile(username)
            break
        else:
            print('Invalid Option')

def add_profile(username):
    print('USER PROFILE\n')
    print('1.Group\n2.Individual\n3.Exit')
    while True:
        profile_opt=input('Category:')
        print('-' * 40)
        if profile_opt=='1':
            addgrp_profile(username)
            break
        elif profile_opt=='2':
            addindividual_profile(username)
            break
        elif profile_opt=='3':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again.')
            continue

def addgrp_profile(username):
    print('ADD  GROUP PROFILE \n')
    print('Pls Entry Your Information:')
    grp_id = input('Group ID:')
    grp_name = input('Group Name: ')
    grp_no= input('Number of Pax:')
    grp_number = input('Contact Number:')
    grp_company= input('Group Company:')
    new_group = {
        'Group ID': grp_id,
        'Group Name': grp_name,
        'Number of Pax': grp_no,
        'Contact Number': grp_number,
        'Company': grp_company
    }
    with open('file.json', 'r') as f:
        data = json.load(f)
    if 'Groups' not in data:
        data['Groups'] = []
    data['Groups'].append(new_group)
    with open('file.json','w') as f:
        json.dump(data, f, indent=4)

    print(f"Successfully created Group Profile: {grp_name}")
    while True:
        exit_opt = input("Press 'b' to return to menu: ")
        if exit_opt.lower() == 'b':
            traveller_menu(username)
            break
        else:
            print("Invalid input. Please press 'b' to return to menu.")


def addindividual_profile(username):
    print('ADD INDIVIDUAL PROFILE\n')
    print('Pls Entry Your Information:')
    ind_username = input ('Username:')
    ind_name = input ('Real Name(Same With Your Passport): ')
    ind_phone = input ('Phone Number:')
    ind_email = input ('Email:')
    new_ind = {
        'Username': ind_username,
        'Real Name': ind_name,
        'Phone Number': ind_phone,
        'Email': ind_email,
    }
    with open('file.json', 'r') as f:
        data = json.load(f)
    if 'Individuals' not in data:
        data['Individuals'] = []
    data['Individuals'].append(new_ind)
    with open('file.json', 'w') as f:
        json.dump(data, f,indent=4)

    print(f"Successfully created Group Profile: {ind_name}")
    while True:
        exit_opt = input("Press 'b' to return to menu: ")
        if exit_opt.lower() == 'b':
            traveller_menu(username)
            break
        else:
            print("Invalid input. Please press 'b' to return to menu.")

def delete_profile(username):
    print('DELETE PROFILE\n')
    print('1.Group\n2.Individual\n3.Exit')
    while True:
        profile_opt=input('Category:')
        print('-' * 40)
        if profile_opt=='1':
            dltgrp_profile(username)
            break
        elif profile_opt=='2':
            dltind_profile(username)
            break
        elif profile_opt=='3':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again.')
            continue

def dltgrp_profile(username):
    print('DELETE GROUP PROFILE\n')
    with open('file.json', 'r') as file:
        data = json.load(file)

    grpid = input('Please Enter Your Group ID: ').strip().lower()
    found_grpid = False
    group_profiles = data.get('Groups', [])
    updated_group_profiles = []

    for group in group_profiles:
        if group.get('Group ID').lower() == grpid:
            found_grpid = True
            print("Group profile to delete:")
            print(f"Group ID: {group.get('Group ID')}")
            print(f"Group Name: {group.get('Group Name')}")
            print(f"Number of Pax: {group.get('Number of Pax')}")
            print(f"Contact Number: {group.get('Contact Number')}")
            print(f"Company: {group.get('Company')}")
            print()
        else:
            updated_group_profiles.append(group)

    if found_grpid:
        confirm_delete = input(f"Are you sure you want to delete group profile with ID '{grpid}'? (yes/no): ").strip().lower()
        if confirm_delete == 'yes':
            data['Groups'] = updated_group_profiles
            with open('file.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Group profile with ID '{grpid}' deleted successfully.")
        else:
            print(f"Delete operation for group with ID '{grpid}' canceled.")
    else:
        print(f"Group with ID '{grpid}' not found.")

    while True:
        exit_opt = input("Press 'b' to return to menu: ")
        if exit_opt.lower() == 'b':
            traveller_menu(username)
            break
        else:
            print("Invalid input. Please press 'b' to return to menu.")


def dltind_profile(username):
    print('DELETE INDIVIDUAL PROFILE\n')
    with open('file.json', 'r') as file:
        data = json.load(file)

    indname = input('Please Enter  Username: ').strip().lower()
    found_indid = False
    ind_profiles = data.get('Individuals', [])
    updated_ind_profiles = []

    for ind in ind_profiles:
        if ind.get('Username').lower() == indname:
            found_indid = True
            print("Individual profile to delete:")
            print(f"Username: {ind.get('Username')}")
            print(f"Name: {ind.get('Name')}")
            print(f"Phone: {ind.get('Phone')}")
            print(f"Email: {ind.get('Email')}")
            print()
        else:
            updated_ind_profiles.append(ind)

    if found_indid:
        confirm_delete = input(f"Are you sure you want to delete Individual profile with Username '{indname}'? (yes/no): ").strip().lower()
        if confirm_delete == 'yes':
            data['Individuals'] = updated_ind_profiles
            with open('file.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Individual profile with Username '{indname}' deleted successfully.")
        else:
            print(f"Delete operation for individual Profile with Username '{indname}' canceled.")
    else:
        print(f"Individuals Profile with Username '{indname}' not found.")

    while True:
        exit_opt = input("Press 'b' to return to menu: ")
        if exit_opt.lower() == 'b':
            traveller_menu(username)
            break
        else:
            print("Invalid input. Please press 'b' to return to menu.")

def booking_menu(username):
    print('BOOKING MENU\n')
    print('1.View My Current Booking.\n2.Cancel Booking.\n3.Add Booking.\n4.Exit.')
    while True:
        booking_opt=input('Welcome to Booking Menu!Please choose yours option:')
        print('-'*40)
        if booking_opt=='1':
            show_booking(username)
            break
        elif booking_opt=='2':
            cancel_booking(username)
            break
        elif booking_opt=='3':
            add_booking(username)
            break
        elif booking_opt=='4':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please choose your option.')
            continue

def show_booking(username):
    print('SHOW BOOKING PAGE\n')
    bkname = input('Hello! Please enter the Booker Name to find their booking: ')
    found_booking = False
    with open('bookingstate.json', 'r') as file:
        data = json.load(file)
        if 'Travel Packages' in data:
            for booking in data['Travel Packages']:
                if bkname == booking.get('Booker name'):
                    found_booking = True
                    print('Found Your Booking!')
                    print(f"Plan: {booking['Plan']}")
                    print(f"Duration: {booking['Duration']}")
                    print(f"Date: {booking['Date']}")
                    print(f"Price: {booking['Price']}")
                    print('-' * 40)

                    if 'Services' in data:
                        for service in data['Services']:
                            if bkname == service.get('Booker name'):
                                print('Found Your Booking in Services!')
                                print(f"Assistance: {service['Assistance']}")
                                print(f"Price: {service['Price']}")
                                print('-' * 40)
                    break
        if not found_booking:
            print('Booking not found. ')
    while True:
        exit_option = input('Do you want Exit?(yes/no):')
        if exit_option.lower() == 'yes':
            print('Back to Main Menu...')
            traveller_menu(username)
            return
        elif exit_option.lower() == 'no':
            show_booking(username)
            break
        else:
            print('Invalid Option')

def cancel_booking(username):
    print('CANCEL BOOKING\n')
    booker_name = input('Please Enter Booker Name: ').strip().lower()
    found_any_booking = False
    found_bookings = []

    with open('bookingstate.json', 'r') as file:
        booking_state = json.load(file)

    travel_package_index = 1
    service_index = 1

    for category, items in booking_state.items():
        for index, item in enumerate(items):
            if item.get('Booker name').lower() == booker_name:
                if category == 'Travel Packages':
                    print(
                        f"{travel_package_index}. Travel Package: {item.get('Plan')} - Destination: {item.get('Destination')} - Date: {item.get('Date')}")
                    travel_package_index += 1
                elif category == 'Services':
                    print(f"{service_index}. Service: {item.get('Assistance')} - Price: {item.get('Price')}")
                    service_index += 1
                print('\n')
                found_bookings.append((category, index))  # Store category and index only
                found_any_booking = True

    if not found_any_booking:
        print(f'No bookings found for {booker_name}.')
        print('-'*40)
        booking_menu(username)
        return

    while True:
        try:
            cancel_id = input(
                f'Enter the Plan/Assistance of the booking you want to cancel (e.g., "Hotel"): ').strip().lower()
            found = False
            for category, index in found_bookings:
                item = booking_state[category][index]
                if 'Plan' in item and item['Plan'].lower() == cancel_id:
                    del booking_state[category][index]
                    print('Booking cancelled successfully.')
                    found = True
                    break
                elif 'Assistance' in item and item['Assistance'].lower() == cancel_id:
                    del booking_state[category][index]
                    print('Booking cancelled successfully.')
                    print('-'*40)
                    booking_menu(username)
                    found = True
                    break

            if found:
                break
            else:
                print('Invalid Plan/Assistance. Please enter a valid one.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    with open('bookingstate.json', 'w') as file:
        json.dump(booking_state, file, indent=4)

    print('-' * 40)


def add_booking(username):
    print('ADD BOOKING\n')
    booker_name = input('Please Enter Booker Name: ').strip().lower()
    booking_type = input('Enter Booking Type (e.g., Travel Package, Service): ').strip()

    if booking_type.lower() == 'travel package':
        plan = input('Enter travel package plan: ').strip()
        destination = input('Enter destination: ').strip()
        date = input('Enter date (e.g., 6 September-13 September 2024): ').strip()
        price = input('Enter price: ').strip()
        booking_details = {
            'Booker name': booker_name,
            'Plan': plan,
            'Destination': destination,
            'Date': date,
            'Price': price
        }
    elif booking_type.lower() == 'service':
        assistance = input('Enter type of assistance (e.g., Translation, Hotel): ').strip()
        price = input('Enter price: ').strip()
        booking_details = {
            'Booker name': booker_name,
            'Assistance': assistance,
            'Price': price
        }
    else:
        print(f"Invalid booking type '{booking_type}'. Please enter either 'Travel Package' or 'Service'.")
        return

    with open('bookingstate.json', 'r') as file:
        booking_state = json.load(file)

    if booking_type.lower() == 'travel package':
        if 'Travel Packages' not in booking_state:
            booking_state['Travel Packages'] = []
        booking_state['Travel Packages'].append(booking_details)
    elif booking_type.lower() == 'service':
        if 'Services' not in booking_state:
            booking_state['Services'] = []
        booking_state['Services'].append(booking_details)

    with open('bookingstate.json', 'w') as file:
        json.dump(booking_state, file, indent=4)

    print("Booking added successfully.")
    print('-' * 40)

def searching_menu(username):
    print('SEARCHING PAGE\n')
    while True:
        keyword = input('Please Enter Your Keyword: ').strip().lower()
        if keyword:
            break
        else:
            print('Invalid input. Please enter a valid keyword.')
    while True:
        with open('file.json', 'r') as file:
            data = json.load(file)
            matching_tours = [tour for tour in data['Tours'] if keyword.lower() in tour['Name'].lower()]
            matching_promotions = [promotion for promotion in data['Promotion'] if
                                   keyword.lower() in promotion['Title'].lower() or keyword.lower() in promotion[
                                       'Description'].lower()]
            matching_services = [service for service in data['Services'] if
                                 keyword.lower() in service['Assistance'].lower()]
            if not (matching_tours or matching_promotions or matching_services):
                print('No matching results found. Please try again with a different keyword.\n')
                break

            display_results(matching_tours, matching_promotions, matching_services)
            break
    while True:
        exit_option = input('Do you want Exit?(yes/no):')
        if exit_option.lower() == 'yes':
            print('Back to Main Menu...')
            traveller_menu(username)
            return
        elif exit_option.lower() == 'no':
            searching_menu(username)
            break
        else:
            print('Invalid Option')

def display_results(tours, promotions, services):
    if tours:
        print("Matching tours:")
        for tour in tours:
            print(f"Tour Name: {tour['Name']}")
            print(f"Itineraries: {tour['Itineraries']}")
            print(f'Available: {tour['Available']}')
            print(f'Price: {tour['Price']}')
            print()
    else:
        print("No matching tour found.\n")


    if promotions:
        print('Matching promotions:')
        print('-'*40)
        for promotion in promotions:
            print(f'Promo Code: {promotion['Promo Code']}')
            print(f'Title: {promotion['Title']}')
            print(f'Description: {promotion['Description']}')
            print(f'Discount: {promotion['Discount']}')
            print(f'Valid Month: {promotion['Valid Month']}')
            print()
    else:
        print('No matching promotions found.\n')

    if services:
        print('Matching services:')
        print('-'*40)
        for service in services:
            print(f'Assistance: {service["Assistance"]}')
            print(f'Price: {service["Price"]}')
            print()
    else:
        print('No matching services found.')

    if not (tours or promotions or services):
        print('No Matching found./n')




def logout(username):
    print('Logout....\n')
    while True:
        logout_option = input('Are You Sure to Logout?(yes/no):')
        if logout_option.lower() == 'yes':
            print('Have a Nice Day!See You!')
            print('-'*40)
            login()
            return
        elif logout_option.lower() == 'no':
            print('Turn to Main Menu...')
            print('-'*40)
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again...')


login()

 