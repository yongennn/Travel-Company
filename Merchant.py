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
                    fields = ['Name', 'Available Rooms', 'Price', 'Average Rating']
                    manage_products('Hotel', fields)
                    return
                elif product_choice == "2":
                    fields = ['Name', 'Type', 'Price', 'Open Hours', 'Average Rating']
                    manage_products('Restaurant', fields)
                    return
                elif product_choice == "3":
                    fields = ['Name', 'Open Hours', 'Price' 'Average Rating']
                    manage_products('Attractions', fields)
                    return
                elif product_choice == "4":
                    fields = ['Type', 'Price', 'Working Hours', 'Available Guides']
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