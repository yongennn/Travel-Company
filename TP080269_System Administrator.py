import json
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
                    main_menu() #function not available here
                elif record[2] == "merchant":
                    print("This is administrators system. Service Provider are strictly not allowed.")
                    main_menu() #function not available here
                break
        else:
            print("Invalid username or password.")
            while True:
                ex_admin = input("Wrong Roles selection ? Back to main menu ?(yes/no):")
                if ex_admin == 'yes':
                    main_menu() #function not available here
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
            logout()
            break
        else:
            print("Invalid option. Try again.")

# logout function
def logout():
    while True:
        confirm_logout = input("\nLogout?(yes/no):").strip().lower()
        if confirm_logout == "yes":
            print("Thank you !\n\n")
            print('-' * 40)
            admin_login()
            break
        elif confirm_logout == "no":
            # guestmainpage()
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
        found = False
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
            print("Itinerary existed.")
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
        json.dump(data, file, indent=3)
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
        print(f'-Children:{price_data['Children']}4')
        print()
    del_des = input("Enter Destination to delete the itinerary:")
    if del_des == "b":
        itineraries_menu()
    else:
        found = False
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
        json.dump(data, files, indent=3)
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
        print(f'-Children:{price_data['Children']}')
        print()
    up_des = input("Enter Destination to Update the Itinerary:")
    if up_des == "b":
        itineraries_menu()
    else:
        found = False
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
        json.dump(data, file, indent=3)
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

admin_login()