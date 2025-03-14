import json
import random

def main_menu():
    print('Welcome KL Trip Planner Application')
    print('1. System adminstrator')
    print('2. Service Provider')
    print('3. Guest')
    print('4. Traveller')
    while True:
        user = input("You Are (Enter number):")
        if user == '1':
            print('='*40)
            admin_login()
            break
        elif user == '2':
            print('=' * 40)
            merchant_login()
            break
        elif user == '3':
            print('=' * 40)
            guestmainpage()
            break
        elif user == '4':
            print('=' * 40)
            login()
            break
        else:
            print("Invalid option. Try again.")

def explore_destination():
    while True:
        print("\nTop Kuala Lumpur Tours")
        print("1. Batu Caves")
        print("2. Petronas Twin Tower")
        print("3. KL Tower")
        keyword = input("Enter a keyword or option (1-3) to explore destinations "
                        "(Enter to see all destination / Type 'Exit' to exit this page): ").strip().lower()
        if keyword == "exit":
            guestmainpage()
            return

        with open("file.json", 'r') as file:
            data = json.load(file)
            destinations = data["Recommendation"]
        if keyword in ["1", "2", "3"]:
            if keyword == "1":
                destination_name = "Batu Caves"
            elif keyword == "2":
                destination_name = "Petronas Twin Tower"
            elif keyword == "3":
                destination_name = "KL Tower"
            else:
                continue
            matching_destinations = [dest for dest in destinations if dest["Name"] == destination_name]
        else:
            matching_destinations = [dest for dest in destinations if keyword.lower() in dest["Name"].lower()]
        if matching_destinations:
            for destination_detail in matching_destinations:
                print(f"\nName: {destination_detail['Name']}")
                print(f"Description: {destination_detail['Description']}")
                print("Attractions:")
                for attraction in destination_detail["Attraction"]:
                    print(f"- {attraction}")
                print("-" * 40)
        else:
            print("No matching destinations found.")

        while True:
            option = input("\nDo you want to see another destination? (Yes / No):").strip().lower()
            if option == "yes":
                explore_destination()
                break
            elif option == "no":
                guestmainpage()
                return
            else:
                print("Invalid input please enter Yes/No")

def view_itineraries():
    with open("file.json", 'r') as file:
        data = json.load(file)
    itineraries = data["Tours"]
    services = data["Services"]

    while True:
        print("\nItineraries and available time of each trip")
        i = 1
        for itinerary in itineraries:
            print(f"{i}. {itinerary['Name']}")
            i += 1
        print(f"{len(itineraries) + 1}. View all itineraries")
        print(f"{len(itineraries) + 2}. Exit")

        option = input(f"Please select an option (1-{len(itineraries) + 2}): ")

        try:
            option = int(option)
            if 1 <= option <= len(itineraries):
                selected_itinerary = itineraries[option - 1]
                print("-" * 40)
                print(f"\nName: {selected_itinerary['Name']}")
                print("\nItineraries:")
                for item in selected_itinerary["Itineraries"]:
                    print(f"- {item}")
                print("\nAvailable Dates:")
                for date in selected_itinerary["Available"]:
                    print(f"- {date}")
                print("\nPrice:")
                for age, price in selected_itinerary["Price"].items():
                    print(f"- {age}: {price}")
                print("\nServices:")
                for service in services:
                    print(f"- {service['Assistance']}: {service['Price']}")
                print("-" * 40)

                while True:
                    signup_option = input(
                        "Do you want to sign up now to view more promotions and information? Yes/No: ").strip().lower()
                    if signup_option == 'yes':
                        sign_up()
                        return
                    elif signup_option == 'no':
                        break
                    else:
                        print("Invalid input. Please enter Yes or No.")

            elif option == len(itineraries) + 1:
                for itinerary in itineraries:
                    print("-" * 40)
                    print(f"\nName: {itinerary['Name']}")
                    print("\nItineraries:")
                    for item in itinerary["Itineraries"]:
                        print(f"- {item}")
                    print("\nAvailable Dates:")
                    for date in itinerary["Available"]:
                        print(f"- {date}")
                    print("\nPrice:")
                    for age, price in itinerary["Price"].items():
                        print(f"- {age}: {price}")
                print("-" * 40)
                print("\nServices:")
                for service in services:
                    print(f"- {service['Assistance']}: {service['Price']}")
                print("-" * 40)

                while True:
                    signup_option = input(
                        "Do you want to sign up now to view more promotions and information? Yes/No: ").strip().lower()
                    if signup_option == 'yes':
                        sign_up()
                        return
                    elif signup_option == 'no':
                        break
                    else:
                        print("Invalid input. Please enter Yes or No.")

            elif option == len(itineraries) + 2:
                guestmainpage()
                return
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def sign_up():
    print("\nSign up for an account in our application to receive more information.")
    while True:
        option = (input("Do you want to sign up now? (Yes/No):")).strip().lower()
        if option == "yes":
            while True:
                username = input("Enter your username:")
                if ' ' in username:
                    print("Username cannot contain any spaces. Please reenter!")
                    print("-" * 40)
                elif not username:
                    print("Username can't be blank. Please reenter!")
                    print("-" * 40)
                elif any(username in line for line in open("users.txt", "r")):
                    print("Username already exists. Please re-enter!")
                    print("-" * 40)
                else:
                    break

            while True:
                password = input("Enter your password: ")
                if ' ' in password:
                    print("Password cannot contain any spaces. Please reenter!")
                    print("-" * 40)
                elif not password:
                    print("Password can't be blank. Please reenter!")
                    print("-" * 40)
                else:
                    break

            while True:
                name = input("Enter your Name (SAME WITH YOUR IC/PASSPORT): ")
                stripped_name = name.strip()
                # Check for leading/trailing spaces and consecutive spaces
                if name != stripped_name or '  ' in stripped_name:
                    print("Name cannot contain leading, trailing, or consecutive spaces. Please re-enter!")
                    print("-" * 40)
                elif any(char.isdigit() for char in name):
                    print("Name cannot contain numbers. Please re-enter!")
                    print("-" * 40)
                elif not stripped_name:
                    print("Name can't be blank. Please re-enter!")
                    print("-" * 40)
                else:
                    break

            while True:
                phone = input("Enter your Phone Number: ")
                if not phone.isdigit():
                    print("Phone number should contain only digits and cannot contain any space. Please re-enter!")
                    print("-" * 40)
                elif not phone:
                    print("Phone number can't be blank. Please reenter!")
                    print("-" * 40)
                else:
                    break

            while True:
                email = input("Enter your Email:")
                if not email:
                    print("email can't be blank. Please reenter!")
                    print("-" * 40)
                elif ' ' in email:
                    print("Email cannot contain any spaces. Please reenter!")
                    print("-" * 40)
                else:
                    break

            new_user={
                'Username':username,
                'Name':stripped_name,
                'Phone':phone,
                'Email':email
            }
            with open("users.txt", "a") as file:
                file.write(f"{username},{password},Traveller\n")
            with open('file.json','r')as file: # create user profile in JSON file
                data = json.load(file)
                individuals = data['Individuals']
                individuals.append(new_user)
            with open ('file.json','w')as file:
                json.dump(data,file,indent=4)
            print("Account created successfully!")
            print("You be a traveller now!")
            while True:
                option = input("Do you want to sign in now? (Yes/No): ").lower().strip()
                if option == 'yes':
                    print("=" * 40)
                    main_menu()
                    return

                elif option == 'no':
                    input("Please type any key to exit this page.")
                    guestmainpage()
                    return
                else:
                    print('Invalid input. Please enter "Yes" or "No".')

        elif option == "no":
            guestmainpage()
            return
        else:
            print('Invalid input. Please enter "Yes" or "No":')
            print("-" * 40)

def guestmainpage():
    with open('file.json','r')as file:
        data = json.load(file)
        promotions = data["Promotion"]
    random_promotion = random.choice(promotions)
    print("\nWelcome KL Trip Planner Application")
    print('======PROMOTION IS HERE !!!========')
    print(f"Promotion: {random_promotion['Title']}")
    print(f"Description: {random_promotion['Description']}")
    print(f"Discount: {random_promotion['Discount']}")
    print(f"Valid Month: {random_promotion['Valid Month']}")
    print('=' * 36)
    print("Function list for guest")
    print('1. Explore destinations, attractions')
    print("2. View recommended itineraries and checking availability")
    print("3. Sign up for an account")
    print("4. Sign In")
    print("5. Exit")
    while True:
        choice = input("Please select an option (1-5): ").strip()
        if choice == '1':
            explore_destination()
        elif choice == '2':
            view_itineraries()
        elif choice == '3':
            sign_up()
        elif choice == '4':
            main_menu()
        elif choice == '5':
            print("Thank you for using the KL Trip Planner. Goodbye!")
            print('=' * 40)
            break
        else:
            print("Invalid choice. Please select a valid option.")

#admin login function
def admin_login():
    print("SYSTEM ADMINISTRATOR")
    username = input("Username:").lower().strip()
    password = input("Password:").lower().strip()
    with open("users.txt", "r") as admin_credential:
        for line in admin_credential:
            record = line.strip().split(",")
            if username == record[0] and password == record[1]:  # check username and password valid in admin
                if record[2] == "admin":
                    print("login success !")
                    print('*' * 40)
                    admin_menu()
                elif record[2] == "traveller":
                    print("This is administrators system.Traveller are strictly not allowed.")
                    main_menu()
                elif record[2] == "merchant":
                    print("This is administrators system. Service Provider are strictly not allowed.")
                    main_menu()
                break
        else:
            print("Invalid username or password.")
            while True:
                ex_admin = input("Wrong Roles selection ? Back to main menu ?(yes/no):")
                if ex_admin == 'yes':
                    main_menu()
                    break
                elif ex_admin == 'no':
                    admin_login()
                    break
                else:
                    print("Invalid Option, Please re-enter.")

# menu function
def admin_menu():
    print("ADMINISTRATION MENU")
    print(" 1:Merchant Management \n 2:Promotion \n 3:Trip recommendation \n 4:Itinerary management\n q:Logout")
    while True:
        opt = input("Choose one function:").strip().lower()  # .strip() and .lower() can read input either in Capital or lower case
        if opt == "1":
            merchant_menu()
            break
        elif opt == "2":
            promotion_menu()
            break
        elif opt == "3":
            recommendation_menu()
            break
        elif opt == '4':
            itineraries_menu()
            break
        elif opt == "q":
            admin_logout()
            break
        else:
            print("Invalid option. Try again.")

# logout function
def admin_logout():
    while True:
        confirm_logout = input("\nLogout?(yes/no):").strip().lower()
        if confirm_logout == "yes":
            print("Thank you !\n\n")
            print('-' * 40)
            guestmainpage()
            break
        elif confirm_logout == "no":
            admin_menu()
            break
        else:
            print("Invalid Option. Try again.")

#merchant
def merchant_menu():
    print("\nMERCHANT MENU")
    print("1:View Merchant \n2:Add Merchant \n3:Block Merchant \n4:Menu")
    while True:
        merchant_opt = input("Enter option:")
        if merchant_opt == "1":
            view_merchant()
            break
        elif merchant_opt == "2":
            add_merchant()
            break
        elif merchant_opt == "3":
            block_merchant()
            break
        elif merchant_opt == "4":
            print('='*40)
            print()
            admin_menu()
            break
        else:
            print("Invalid option.Try again.")

#view merchant
def view_merchant():
    print("\nVIEW MERCHANT")
    with open("users.txt", "r") as merchant:
        for line in merchant:
            record = line.strip().split(",")
            if record[2] == 'merchant':
                print(f"Merchant Username:{record[0]}")
                print(f"Merchant Status:{record[3]}\n")
                found = True
    while True:
        back_to_menu = input("Back to Merchant Menu (yes/no):").strip().lower()
        if back_to_menu == "yes":
            merchant_menu()
            break
        elif back_to_menu == "no":
            view_merchant()
            break
        else:
            print("Invalid option. Try Again.")

# add merchant function
def add_merchant():
    print("\nADD MERCHANT")
    print("b:Back to Merchant Menu")
    new_merchant_username = input("Enter New Merchant username:")
    newstatus = []
    found = False
    if new_merchant_username.lower() == "b":
        merchant_menu()
    with open("users.txt", "r") as merchant_file:
        merchant = merchant_file.readlines()
    for line in merchant:
        record = line.strip().split(',')
        if new_merchant_username == record[0] and record[2]=='merchant':
            if record[3] == 'inactive':
                record[3] = 'active'
                newstatus.append(','.join(record)+'\n') #changes add updated info to newstatus
                print(f"Merchant {new_merchant_username} reactivated !")
            else:
                print("Merchant existed and is active.")
                newstatus.append(line) #no changes append previous line into newstatus
            found = True
        else:
            newstatus.append(line) #no changes append previous line into newstatus
    if not found:
        new_record = f"{new_merchant_username},kl_trip_merchant,merchant,active\n"
        newstatus.append(new_record) #new record added to newstatus
        print(f"{new_merchant_username} added successfully.")
    with open("users.txt", "w") as merchant:
        merchant.writelines(newstatus)
    while True:
        opt = input("Add another user?(yes/no):").strip().lower()
        if opt == "yes":
            add_merchant()
            break
        elif opt == "no":
            print('-'*40)
            merchant_menu()
            break
        else:
            print("Invalid option. Try Again.")

#block_merchant():
def block_merchant():
    print("\nBLOCK MERCHANT")
    print("b:Back to merchant Menu")
    found = False
    newlines=[]
    with open("users.txt", "r") as merchant:
        lines = merchant.readlines()
        for line in lines:
            record = line.strip().split(",")
            if record[2] == 'merchant':
                print(f"Merchant Username:{record[0]}")
                print(f"Merchant Status:{record[3]}\n")
        block_user_username = input("Enter merchant username to block:").strip().lower()
        for line in lines:
            record = line.strip().split(",")
            if block_user_username == "b":
                print('-' * 40)
                merchant_menu()
                break
            elif block_user_username == record[0]:
                record[3] = 'inactive'  # update merchant status to inactive
                newlines.append(",".join(record) + '\n')
                print(f"Merchant Username:{record[0]}")
                print(f"Merchant Status:{record[3]}")
                print(f'Status of {block_user_username} change to Inactive')
                found = True
            else:
                newlines.append(line)
    if found:
        with open('users.txt','w')as merchant:
            merchant.writelines(newlines)
    else:
        print("Merchant doesn't exist.")
    while True:
        opt = input("Block another user?(yes/no):").strip().lower()
        if opt == "yes":
            block_merchant()
            break
        elif opt == "no":
            merchant_menu()
            break
        else:
            print("Invalid option. Try Again.") # inform users invalid option entered, enter option again.

#promotion menu
def promotion_menu():
    print("\nPROMOTION")
    print("1:View Promotion\n2:Add promotion \n3:Delete promotion \n4:Update Promotion\n5:Menu")
    while True:
        promo_opt = input("Enter your option:")
        if promo_opt == "1":
            view_promotion()
            break
        elif promo_opt == "2":
            add_promotion()
            break
        elif promo_opt == "3":
            delete_promotion()
            break
        elif promo_opt == "4":
            update_promotion()
            break
        elif promo_opt == "5":
            print('=' * 40)
            print()
            admin_menu()
            break
        else:
            print("Invalid Option. Please try again.")

#view promotion
def view_promotion():
    print("\nVIEW PROMOTION")
    with open ('file.json','r') as promotion_file:
            data = json.load(promotion_file)
    promotion = data["Promotion"]
    for promo in promotion:
        print(f"\nPromo Code: {promo['Promo Code']}")
        print(f"Title: {promo['Title']}")
        print(f"Description: {promo['Description']}")
        print(f"Discount: {promo['Discount']}")
        print(f"Valid Month: {promo['Valid Month']}\n")
    while True:
        back_to_menu = input("Back to Promotion Menu (yes/no):").strip().lower()
        if back_to_menu == "yes":
            promotion_menu()
            break
        elif back_to_menu == "no":
            view_promotion()
            break
        else:
            print("Invalid option. Try Again.")

# add promotion
def add_promotion():
    print("\nADD PROMOTION")
    print("b:Back to promotion menu.")
    promo_code = input("Promo Code:").strip().upper()
    if promo_code == "B":
        promotion_menu()
    with open ('file.json','r') as promotion_file:
        data = json.load(promotion_file)
    promotion = data['Promotion']
    for promo in promotion:
        if promo['Promo Code'] == promo_code:
            print("Promotion code existed.")
            break
    else:
        title = input("Promotion Title:")
        description = input("Description:")
        discounts = input("Discount:")
        valid_month = input("Invalid Month:")
        promotion.append({'Promo Code': promo_code, 'Title': title, 'Description': description, 'Discount': discounts,'Valid Month': valid_month})
        with open ('file.json','w') as promotion_file:
            json.dump(data, promotion_file, indent=5)
        print(f'{promo_code} added successful.')
    while True:
        opt = input("Add another promotion?(yes/no):").strip().lower()
        if opt == "yes":
            add_promotion()
            break
        elif opt == "no":
            promotion_menu()
            break
        else:
            print("Invalid option.Try again.")

#update promotion
def update_promotion():
    print("\nUPDATE PROMOTION")
    print("b:Back to promotion menu.")
    with open ('file.json','r') as promotion_file:
            data = json.load(promotion_file)
            promotion = data['Promotion']
    for promo in promotion:
        print(f"\nPromo Code: {promo['Promo Code']}")
        print(f"Title: {promo['Title']}")
        print(f"Description: {promo['Description']}")
        print(f"Discount: {promo['Discount']}")
        print(f"Valid Month: {promo['Valid Month']}\n")
    promo_code=input("Enter promo code to update:").upper().strip()
    if promo_code == "B":
        promotion_menu()
    found = False
    for promo in promotion:
        if promo['Promo Code'] == promo_code:
            found = True
            print("Current Promotion Details:")
            print(f"Promo Code: {promo['Promo Code']}")
            print(f"Title: {promo['Title']}")
            print(f"Description: {promo['Description']}")
            print(f"Discount: {promo['Discount']}")
            print(f"Valid Month: {promo['Valid Month']}")
            while True:
                update_part = input("Enter Attribute to Correct:").title().strip()
                if update_part in promo:
                    if update_part == 'Promo Code':
                        update_info = input("Update Information:").upper().strip()
                    else:
                        update_info = input("Update Information:")
                    promo[update_part] = update_info
                    print("Current Promotion Details:")
                    print(f"Promo Code: {promo['Promo Code']}")
                    print(f"Title: {promo['Title']}")
                    print(f"Description: {promo['Description']}")
                    print(f"Discount: {promo['Discount']}")
                    print(f"Valid Month: {promo['Valid Month']}")
                    break
                else:
                    print("Invalid attribute.")
    if not found:
        print('Promotion not found.')
    with open('file.json', 'w') as promotion_file:
        json.dump(data, promotion_file, indent=5)
    while True:
        opt = input("Update another promotion? (yes/no):").strip().lower()
        if opt == "yes":
            update_promotion()
            break
        elif opt == "no":
            promotion_menu()
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

#delete promotion
def delete_promotion():
    print("\nDELETE PROMOTION")
    print("b:Back to promotion menu.")
    with open ('file.json','r') as promotion_file:
        data = json.load(promotion_file)
        promotion = data['Promotion']
    found = False
    for promo in promotion:
        print(f"Promo Code: {promo['Promo Code']}")
        print(f"Title: {promo['Title']}")
        print(f"Description: {promo['Description']}")
        print(f"Discount: {promo['Discount']}")
        print(f"Valid Month: {promo['Valid Month']}\n")
    del_promocode = input("Enter promo code to delete:").strip().upper()
    for promo in promotion:
        if del_promocode == "B":
            promotion_menu()
        elif promo['Promo Code'] == del_promocode:
            found = True
            print("Current Promotion Details:")
            print(f"Promo Code: {promo['Promo Code']}")
            print(f"Title: {promo['Title']}")
            print(f"Description: {promo['Description']}")
            print(f"Discount: {promo['Discount']}")
            print(f"Valid Month: {promo['Valid Month']}")
            while True:
                opt_del = input("Confirm to delete?(yes/no):").strip().lower()
                if opt_del == "yes":
                    promotion.remove(promo)
                    print(f"{del_promocode} deleted !")
                    break
                elif opt_del == "no":
                    print("Deletion cancelled.")
                    break
                else:
                    print("Invalid option. Try again.")
                break
    if not found:
        print("Promotion doesn't exist.")
    with open('file.json', 'w') as promotion_file:
        json.dump(data, promotion_file,indent=5)
    while True:
        del_opt = input("Delete another promotion ?(yes/no):").strip().lower()
        if del_opt == "yes":
            delete_promotion()
            break
        elif del_opt == "no":
            promotion_menu()
            break
        else:
            print("Invalid option. Try Again.")

 #trip recommendation menu
def recommendation_menu():
    print("\nTRIP RECOMMENDATION")
    print("1:View recommendation\n2:Provide Trip Recommendation \n3:Delete Recommendation \n4:Menu")
    while True:
        rec_opt = input("Enter your option:")
        if rec_opt == "1":
            view_trip_recommendation()
            break
        elif rec_opt == "2":
            provide_trip_recommendation()
            break
        elif rec_opt == "3":
            delete_recommendation()
            break
        elif rec_opt == "4":
            print('=' * 40)
            print()
            admin_menu()
            break
        else:
            print("Invalid Option. Choose again.")

# view trip recommendation
def view_trip_recommendation():
    print("\nVIEW TRIP RECOMMENDATION")
    with open ('file.json','r')as reco_file:
        data = json.load(reco_file)
        recommendation = data['Recommendation']
    for reco in recommendation:
        print(f"Destination: {reco['Name']}")
        print(f"Description: {reco['Description']}")
        print(f"Attraction:")
        for attr in reco["Attraction"]:
            print(f"- {attr}")
        print()
    while True:
        back_to_menu = input("Back to Trip Recommendation Menu (yes/no):")
        if back_to_menu == "yes":
            recommendation_menu()
            break
        elif back_to_menu =="no":
            view_trip_recommendation()
            break
        else:
            print("Invalid option. Try Again.")

# provide trip recommendation
def provide_trip_recommendation():
    print("\nPROVIDE TRIP RECOMMENDATION")
    print("b:back to recommendation menu")
    reco_des = input("Destination:").title()
    if reco_des.lower() =="b":
        recommendation_menu()
    with open ('file.json','r')as reco_file:
        data = json.load(reco_file)
        recommendation = data['Recommendation']
    for reco in recommendation:
        if reco['Name'].lower() == reco_des.lower():
            print("Recommendation existed.")
            break
    else:
        description = input("Description:")
        attractions = []
        count = 1
        while True:
            attraction = input(f'Attraction {count} (Type Enter if finish):')
            if attraction =='': #type enter to quit
                break
            attractions.append(attraction)
            count += 1
        recommendation.append({'Name':reco_des,'Description':description,'Attraction':attractions})
        print(f'{reco_des} added successfully.')
        with open ('file.json','w')as reco_file:
            json.dump(data,reco_file,indent=3)
    while True:
        opt = input("Add another recommendation?(yes/no):").strip().lower()
        if opt == "yes":
            provide_trip_recommendation()
            break
        elif opt == "no":
            recommendation_menu()
            break
        else:
            print("Invalid option. Try Again.")

#delete recommendation
def delete_recommendation():
    print("\nDELETE RECOMMENDATION")
    print("b:back to recommendation menu")
    found = False
    with open('file.json', 'r') as reco_file:
        data = json.load(reco_file)
        recommendation = data['Recommendation']
    for reco in recommendation:
        print(f"Destination: {reco['Name']}")
        print(f"Description: {reco['Description']}")
        print(f"Attraction:")
        for attr in reco["Attraction"]:
            print(f"- {attr}")
        print()
    del_reco_des = input("Enter Destination to delete:")
    if del_reco_des =="b":
        recommendation_menu()
    else:
        for reco in recommendation:
            if reco['Name'].lower() == del_reco_des.lower():
                found = True
                print(f"Destination: {reco['Name']}")
                print(f"Description: {reco['Description']}")
                print(f"Attraction:")
                for attr in reco["Attraction"]:
                    print(f"- {attr}")
                while True:
                    confirm = input("Confirm to delete(yes/no):").strip().lower()
                    if confirm == "yes":
                        recommendation.remove(reco)
                        print(f"{del_reco_des} deleted.")
                        break
                    elif confirm == "no":
                        print("Deletion cancelled.")
                        break
                    else:
                        print("Invalid Option. Try again")
    if not found:
        print("Recommendation code not found.")
    with open ('file.json','w')as reco_file:
        json.dump(data,reco_file,indent=3)
    while True:
        opt = input("Delete another recommendation ?(yes/no):").strip().lower()
        if opt == "yes":
            delete_recommendation()
            break
        elif opt == "no":
            recommendation_menu()
            break
        else:
            print("Invalid option. Try Again.")

# itinaries
def itineraries_menu():
    print("\nITINERARY MANAGEMENT MENU")
    print("1:View Itinerary\n2:Add Itinerary \n3:Update Itinerary \n4:Delete Itinerary \n5:Menu")
    while True:
        opt = input("Enter your option:")
        if opt == "1":
            view_itinerary()
            break
        elif opt == "2":
            add_itinerary()
            break
        elif opt == "3":
            update_itinerary()
            break
        elif opt == "4":
            delete_itinerary()
            break
        elif opt == "5":
            print('=' * 40)
            print()
            admin_menu()
            break
        else:
            print("Invalid Option. Please try again.")

def view_itinerary():
    print("\nVIEW ITINERARY")
    with open('file.json', 'r') as files:
        data = json.load(files)
        itinerary = data['Tours']
    for itn in itinerary:
        print(f"Trip: {itn['Name']}")
        print("Itineraries:")
        for itin in itn['Itineraries']:
            print(f'-{itin}')
        print(f"Available:")
        for ava in itn["Available"]:
            print(f"- {ava}")
        print(f"Price:")
        price_data = itn['Price']
        print(f'-Adult:{price_data['Adult']}')
        print(f'-Children:{price_data['Children']}')
        print()
    while True:
        back_to_menu = input("Back to Itineraries Menu (yes/no):")
        if back_to_menu == "yes":
            itineraries_menu()
            break
        elif back_to_menu == "no":
            view_itinerary()
            break
        else:
            print("Invalid option. Try Again.")

#add itinerary
def add_itinerary():
    print("\nADD ITINERARY")
    print("b:back to itinerary menu")
    des = input("Trip:").title()
    if des.lower() == "b":
        itineraries_menu()
    with open('file.json', 'r') as itn_file:
        data = json.load(itn_file)
        itinerary = data['Tours']
    for itn in itinerary:
        if itn['Name'].lower() == des.lower():
            print("Recommendation existed.")
            break
    else:
        print('Itineraries:')
        itineraries = []
        count = 1
        while True:
            itin = input(f'- Schedule {count} (Type Enter if finish):')
            if count == 1 and itin == '':
                print('Itinerary Cannot be blanked.')
            elif count > 1 and itin == '':  # type enter to quit
                break
            else:
                itineraries.append(itin)
                count += 1
        print("Available Slot:")
        availability = []
        count = 1
        while True:
            available = input(f'- Time Slot {count} (Type Enter if finish):')
            if count == 1 and available == '':
                print('Cannot be blanked, Please enter available time slot.')
            elif available == '':
                break
            else:
                availability.append(available)
                count += 1
        print('Price(eg:RM100):')
        adult = input("-Adult:")
        children = input("-Children:")
        new_itinerary = {
            'Name': des,
            'Itineraries': itineraries,
            'Available': availability,
            'Price': {
                'Adult': adult,
                'Children': children
            }
        }
        itinerary.append(new_itinerary)
        print(f'Itinerary of {des} added successfully.')
    with open('file.json', 'w') as file:
        json.dump(data, file, indent=4)
    while True:
        opt = input("Add another itinerary?(yes/no):").strip().lower()
        if opt == "yes":
            add_itinerary()
            break
        elif opt == "no":
            itineraries_menu()
            break
        else:
            print("Invalid option. Try Again.")

#delete_itinerary
def delete_itinerary():
    print("\nDELETE ITINERARY")
    print("b:back to Itinerary menu")
    with open('file.json', 'r') as itn_file:
        data = json.load(itn_file)
        itinerary = data['Tours']
    for itn in itinerary:
        print(f"Trip: {itn['Name']}")
        print("Description:")
        for itin in itn['Itineraries']:
            print(f'-{itin}')
        print(f"Available:")
        for ava in itn["Available"]:
            print(f"- {ava}")
        print(f"Price:")
        price_data = itn['Price']
        print(f'-Adult:{price_data['Adult']}')
        print(f'-Children:{price_data['Children']}/n')
        print()
    del_des = input("Enter Trip Title to delete the itinerary:")
    found = False
    if del_des == "b":
        itineraries_menu()
    else:
        for itn in itinerary:
            if itn['Name'].lower() == del_des.lower():
                found = True
                print(f"Trip: {itn['Name']}")
                print("Description:")
                for itin in itn['Itineraries']:
                    print(f'-{itin}')
                print(f"Available:")
                for ava in itn["Available"]:
                    print(f"- {ava}")
                print(f"Price:")
                price_data = itn['Price']
                print(f'-Adult:{price_data['Adult']}')
                print(f'-Children:{price_data['Children']}')
                print()
                while True:
                    confirm = input("Confirm to delete(yes/no):").strip().lower()
                    if confirm == "yes":
                        itinerary.remove(itn)
                        print(f"{del_des} deleted.")
                        break
                    elif confirm == "no":
                        print("Deletion cancelled.")
                        break
                    else:
                        print("Invalid Option. Try again")
    if not found:
        print("Itinerary not found.")
    with open('file.json', 'w') as files:
        json.dump(data, files, indent=4)
    while True:
        opt = input("Delete another itinerary ?(yes/no):").strip().lower()
        if opt == "yes":
            delete_itinerary()
            break
        elif opt == "no":
            itineraries_menu()
            break
        else:
            print("Invalid option. Try Again.")

#update itinerary
def update_itinerary():
    print("\nUPDATE ITINERARY")
    print("b:back to Itinerary menu")
    found = False
    with open('file.json', 'r') as itn_file:
        data = json.load(itn_file)
        itinerary = data['Tours']
    for itn in itinerary: # show all itinerary
        print(f"Trip: {itn['Name']}")
        print("Description:")
        for itin in itn['Itineraries']:
            print(f'-{itin}')
        print(f"Available:")
        for ava in itn["Available"]:
            print(f"- {ava}")
        print(f"Price:")
        price_data = itn['Price']
        print(f'-Adult:{price_data['Adult']}')
        print(f'-Children:{price_data['Children']}')
        print()
    up_des = input("Enter Trip Title to Update the Itinerary:")
    if up_des == "b": #wrong function selected
        itineraries_menu()
    else: #update a itinerary
        newupdate = []
        for itn in itinerary:
            if itn['Name'].lower() == up_des.lower():
                found = True
                print(f"1. Trip: {itn['Name']}")
                print("2. Itinerary:")
                for itin in itn['Itineraries']:
                    print(f'-{itin}')
                print(f"3. Available:")
                for ava in itn["Available"]:
                    print(f"- {ava}")
                print(f"4. Price:")
                price_data = itn['Price']
                print(f'-Adult:{price_data['Adult']}')
                print(f'-Children:{price_data['Children']}')
                print()
                while True:
                    update_part = input("Enter number to Correct:")
                    if update_part == '1':
                        update_info = input("Update Information:").title()
                        itn['Name'] = update_info
                        break
                    elif update_part == '2':
                        count = 1
                        while True:
                            itin = input(f'- Update Schedule {count} (Type Enter if finish):')
                            if count == 1 and itin == '':
                                print('Itinerary Cannot be blanked.')
                            elif count > 1 and itin == '':  # type enter to quit
                                break
                            else:
                                newupdate.append(itin)
                                count += 1
                        itn['Itineraries'] = newupdate
                        break
                    elif update_part == '3':
                        count = 1
                        while True:
                            available = input(f'- Time Slot {count} (Type Enter if finish):')
                            if count == 1 and available == '':
                                print('Cannot be blanked, Please enter available time slot.')
                            elif available == '':
                                break
                            else:
                                newupdate.append(available)
                                count += 1
                        itn['Available'] = newupdate
                        break
                    elif update_part == "4":
                        print('Price(eg:RM100):')
                        adult = input("-Adult:")
                        children = input("-Children:")
                        price_update = {
                            "Adult": adult,
                            "Children": children
                        }
                        itn["Price"] = price_update
                        break
                    else:
                        print("Invalid attribute.")
                print("Itinerary Updated Successfully")
    if not found:
        print("Itinerary not found.")
    with open('file.json', 'w') as file:
        json.dump(data, file, indent=4)
    while True:
        opt = input("Update another Itinerary ?(yes/no):").strip().lower()
        if opt == "yes":
            update_itinerary()
            break
        elif opt == "no":
            itineraries_menu()
            break
        else:
            print("Invalid option. Try Again.")

#traveller
def login():
    print('Welcome!\n')
    while True:
        username = input('Hello ! Please enter your username:').lower()
        password = input('Hello ! Please enter your password:').lower()
        print('\n')
        found_user = False
        with open('users.txt', 'r') as user_information:
            for line in user_information:
                columns = line.strip().split(',')
                user = columns[0]
                pwd = columns[1]
                if user == username and pwd == password and columns[2] == 'Traveller':
                    print('Login Successful!')
                    traveller_menu(username)
                    found_user = True
                    return
        if not found_user:
            print('Invalid username and password. Please try again.')
            ex_opt = input('Do you want to exit?(yes/no):')
            if ex_opt.lower() == 'yes':
                print('See You !')
            elif ex_opt.lower() == 'no':
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
        print('-' * 40)
        if opt == '1':
            user_profile(username)
            break
        elif opt == '2':
            booking_menu(username)
            break
        elif opt == '3':
            searching_menu(username)
            break
        elif opt == '4':
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
        profile_opt = input('Please enter :')
        print('-' * 40)
        if profile_opt == '1':
            view_profile(username)
            break
        elif profile_opt == '2':
            update_profile(username)
            break
        elif profile_opt == '3':
            add_profile(username)
            break
        elif profile_opt == '4':
            delete_profile(username)
            break
        elif profile_opt == '5':
            traveller_menu(username)
            break
        else:
            print("Invalid Input.Please Try Again.")
            continue


def view_profile(username):
    print('USER PROFILE\n')
    print('1.Group\n2.Individual\n3.Exit')
    while True:
        profile_opt = input('Category:')
        print('-' * 40)
        if profile_opt == '1':
            group_profile(username)
            break
        elif profile_opt == '2':
            individual_profile(username)
            break
        elif profile_opt == '3':
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
                    print('-' * 40)
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
            data = json.load(files)
            personal_profile = data['Individuals']
            for pro in personal_profile:
                if personal_username == pro['Username']:
                    found_group = True
                    print('Found Your Profile!')
                    print(f'Name:{pro['Name']}')
                    print(f'Phone Number: {pro['Phone Number']}')
                    print(f'Email: {pro['Email']}')
                    print('-' * 40)
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
        profile_opt = input('Category:')
        print('-' * 40)
        if profile_opt == '1':
            updategrp_profile(username)
            break
        elif profile_opt == '2':
            updateind_profile(username)
            break
        elif profile_opt == '3':
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again.')
            continue


def updategrp_profile(username):
    print('UPDATE GROUP PROFILE\n')
    groupid = input('Enter your group ID to update: ')
    with open('file.json', 'r') as file:
        data = json.load(file)
        group_profile = data['Groups']
        found_group = False
        for gp in group_profile:
            if groupid == gp["Group ID"]:
                found_group = True
                print('Group Found!')
                print('-' * 40)
                new_number = input('Enter Your New Group Name:').strip()
                new_members = input('Enter Your New Number of Pax (eg:4 pax):').strip()
                new_contactnumber = input('Enter Your New Contact Number ').strip()
                new_company = input('Enter Your New Group Company:').strip()
                if not new_number or not new_members or not new_contactnumber or not new_company:
                    print("Invalid.")
                    print('-' * 40)
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
    with open('file.json', 'r') as file:
        data = json.load(file)
        ind_profile = data['Individuals']
        found_ind = False
        for us in ind_profile:
            if user == us["Username"]:
                found_ind = True
                print('Profile Found!')
                print('-' * 40)
                new_name = input('Enter Your New Name:').strip()
                new_phone = input('Enter Your New Phone:').strip()
                new_email = input('Enter Your New Email:').strip()
                if not new_name or not new_phone or not new_email:
                    print("Invalid.")
                    print('-' * 40)
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
        profile_opt = input('Category:')
        print('-' * 40)
        if profile_opt == '1':
            addgrp_profile(username)
            break
        elif profile_opt == '2':
            addindividual_profile(username)
            break
        elif profile_opt == '3':
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
    grp_no = input('Number of Pax:')
    grp_number = input('Contact Number:')
    grp_company = input('Group Company:')
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
    with open('file.json', 'w') as f:
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
    ind_username = input('Username:')
    ind_name = input('Real Name(Same With Your Passport): ')
    ind_phone = input('Phone Number:')
    ind_email = input('Email:')
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
        json.dump(data, f, indent=4)

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
        profile_opt = input('Category:')
        print('-' * 40)
        if profile_opt == '1':
            dltgrp_profile(username)
            break
        elif profile_opt == '2':
            dltind_profile(username)
            break
        elif profile_opt == '3':
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
        confirm_delete = input(
            f"Are you sure you want to delete group profile with ID '{grpid}'? (yes/no): ").strip().lower()
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
        confirm_delete = input(
            f"Are you sure you want to delete Individual profile with Username '{indname}'? (yes/no): ").strip().lower()
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
        booking_opt = input('Welcome to Booking Menu!Please choose yours option:')
        print('-' * 40)
        if booking_opt == '1':
            show_booking(username)
            break
        elif booking_opt == '2':
            cancel_booking(username)
            break
        elif booking_opt == '3':
            add_booking(username)
            break
        elif booking_opt == '4':
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
        print('-' * 40)
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
                    print('-' * 40)
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
        print('-' * 40)
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
        print('-' * 40)
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
            print('-' * 40)
            login()
            return
        elif logout_option.lower() == 'no':
            print('Turn to Main Menu...')
            print('-' * 40)
            traveller_menu(username)
            break
        else:
            print('Invalid Input.Please Try Again...')

#merchant
def merchant_main_menu():
    print("\nThis is the Main Menu")
    choice = input("Login as merchant? y/n: ")
    if choice == "y":
        merchant_login()


def merchant_login():
    print("\nSERVICE PROVIDER")
    while True:
        username = input("Username: ")
        password = input("Password: ")

        with open("users.txt", 'r') as merchant_info:
            accounts = [line.strip().split(",") for line in merchant_info]

            account_found = False  # check to see if account exists
            for account in accounts:
                if username == account[0] and password == account[1]:
                    account_found = True
                    account_type = account[2].strip()

                    if account_type == "merchant":
                        merchant_status = account[3].strip()

                        if password == "kl_trip_merchant" and merchant_status == "active":
                            print("\nWelcome to KL Trip Planner Application! Please change your password.")
                            new_pass = input("Enter new password: ")
                            account[1] = new_pass

                            # writes the updated password back to the file
                            with open("users.txt", 'w') as all_users:
                                for acc in accounts:
                                    all_users.write(",".join(acc) + "\n")
                            service_provider_menu()

                            return

                        elif merchant_status == "active":
                            print("\nLogin Successful! Welcome.")
                            service_provider_menu()

                            return

                        elif merchant_status == "inactive":
                            print("\nYour account has been blocked. Please contact administration for assistance.")
                            main_menu()

                            return

                    else:
                        print("\nThis is the login page for service providers only. "
                              "Please go to the correct login page.")
                        main_menu()
                        return

            if not account_found:
                print("\nInvalid username or password. Please try again.")


def merchant_logout():
    while True:
        logout = input("\nDo you wish to log out? yes/no: ").strip().lower()

        if logout == "yes":
            print("\nSuccessfully logged out!")
            main_menu()

            return

        elif logout == "no":
            service_provider_menu()

            return

        else:
            print("\nInvalid option. Please try again.")


def manage_products(product_type, fields):
    with open('products.txt', 'r') as products:
        all_products = [line.strip().split(",") for line in products]

    def view_products():
        print("Fields: ", "  ".join(fields))
        for idx, itm in enumerate(product_list):
            print(f"{idx + 1}. {', '.join(itm[1:])}")

    # creates a new list to store only the relevant products/services
    product_list = []
    for product in all_products:
        if product[0].strip().lower() == product_type.strip().lower():
            product_list.append(product)

    while True:
        print(f"\nMANAGE {product_type.upper()}")
        print(f"1. Add {product_type} \n2. Delete {product_type} "
              f"\n3. Update Listing \n4. View {product_type}s \n5. Confirm Changes \n6. Back")
        choice = input("\nChoose an option: ").strip().lower()

        if choice == "1":
            new_product = [product_type]
            print("\nPlease enter the following details: ")

            for field in fields:
                new_value = input(f"{field}: ").strip()
                new_product.append(new_value)
            product_list.append(new_product)

            print(f"\n{product_type.capitalize()} added successfully.")

        elif choice == "2":
            # check to see if list is empty
            if not product_list:
                print(f"\nNo {product_type}s to delete.")
                continue

            view_products()

            del_index = int(input(f"\nEnter the number of the {product_type} you wish to delete: ").strip())

            if 0 < del_index <= len(product_list):
                del_index = del_index - 1
                deleted_product = product_list.pop(del_index)

                print(f"\n{product_type.capitalize()} '{deleted_product[1]}' deleted successfully.")

            else:
                print("\nInvalid selection. Please try again.")

        elif choice == "3":
            if not product_list:
                print(f"\nNo {product_type}s to update.")
                continue

            view_products()

            update_index = int(input(f"\nEnter the number of the {product_type} you wish to update: ").strip())

            if 0 < update_index <= len(product_list):
                update_index = update_index - 1  # Convert to 0-based index
                updated_product = [product_type]
                print("\nPlease enter the following details: ")

                for field in fields:
                    updated_value = input(f"{field}: ").strip()
                    updated_product.append(updated_value)
                product_list[update_index] = updated_product

                print(f"\n{product_type.capitalize()} updated successfully.")

            else:
                print("\nInvalid selection. Please try again.")

        elif choice == "4":
            view_products()

        elif choice == "5":
            with open('products.txt', 'w') as products:
                for product in all_products:
                    if product[0].strip().lower() != product_type:
                        products.write(",".join(product) + "\n")
                    else:
                        for item in product_list:
                            products.write(",".join(item) + "\n")

            print("\nChanges saved successfully.")

        elif choice == "6":
            service_provider_menu()

        else:
            print("\nInvalid input. Please try again.")


def service_provider_menu():
    print("\nSERVICE PROVIDER MENU")
    print("1. Manage Products and Services \n2. Manage Bookings \n3. Logout")

    while True:
        choice = input("\nChoose an option: ").strip().lower()

        if choice == "1":
            print("\nPRODUCTS AND SERVICES")
            print("1. Hotels \n2. Restaurants \n3. Attractions \n4. Tour Operators \n5. Back")

            # to adjust the manage_products() function based on the type of product/service
            while True:
                product_choice = input("\nChoose an option: ").strip().lower()
                if product_choice == "1":
                    fields = ['Name', 'Price', 'Average Rating']
                    manage_products('Hotel', fields)
                    return
                elif product_choice == "2":
                    fields = ['Name', 'Type', 'Price', 'Open Hours', 'Average Rating']
                    manage_products('Restaurant', fields)
                    return
                elif product_choice == "3":
                    fields = ['Name', 'Open Hours', 'Price']
                    manage_products('Attractions', fields)
                    return
                elif product_choice == "4":
                    fields = ['Type', 'Price']
                    manage_products('Tour Operator', fields)
                    return
                elif product_choice == "5":
                    service_provider_menu()
                    return
                else:
                    print("Invalid option. Please try again.")

        elif choice == "2":
            manage_bookings()
            return

        elif choice == "3":
            merchant_logout()
            return
        else:
            print("Invalid option. Please try again.")


def manage_bookings():
    with open("bookings.txt", "r") as total_bookings:
        all_bookings = [line.strip().split(",") for line in total_bookings]

    # helper functions to reduce code redundancy
    def write_bookings(bookings):
        with open("bookings.txt", "w") as write_bookings:
            for booking in bookings:
                write_bookings.write(",".join(booking) + "\n")

    def view_bookings():
        for idx, booking in enumerate(all_bookings):
            print(f"{idx + 1}. {', '.join(booking)}")

    while True:
        with open("bookings.txt", "r") as bookings_file:
            all_bookings = [line.strip().split(",") for line in bookings_file]

        print("\nMANAGE BOOKINGS")
        print("1. View Bookings \n2. Confirm Booking \n3. Cancel Booking \n4. Back")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            if not all_bookings:
                print("\nThere are no bookings to view.")
                continue
            view_bookings()

        elif choice == "2":

            view_bookings()

            if not all_bookings:
                print("\nThere are no bookings to be confirmed.")
                continue

            booking_idx = int(input("\nEnter the index of the booking to confirm: ").strip())

            if 0 < booking_idx <= len(all_bookings):
                booking_idx = booking_idx - 1
                if "Confirmed" not in all_bookings[booking_idx]:
                    all_bookings[booking_idx].append("Confirmed")
                    write_bookings(all_bookings)
                    print("\nBooking is now confirmed.")
                else:
                    print("\nBooking is already confirmed.")

            else:
                print("\nInvalid index. Please try again.")

        elif choice == "3":
            view_bookings()

            booking_idx = int(input("\nEnter the index of the booking to cancel: ").strip())

            if not all_bookings:
                print("\nThere are no bookings to be cancelled.")
                continue

            if 0 < booking_idx <= len(all_bookings):
                booking_idx = booking_idx - 1
                del all_bookings[booking_idx]
                write_bookings(all_bookings)
                print("\nBooking has been cancelled.")
            else:
                print("\nInvalid index. Please try again.")

        elif choice == "4":
            service_provider_menu()
            return

        else:
            print("Invalid input. Please try again.")

guestmainpage()