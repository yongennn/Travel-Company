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