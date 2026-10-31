#Portal Login System V2.0
#Author: Ethan Gu

user_database = {"User": "123456"}

print("=== Welcome to the Login System V2.0 ===")
while True:
    print("\n-----------------------------")
    print("0. ADMINISTRATOR")
    print("1. Sign UP")
    print("2. Sign IN")
    print("3. Log OFF")
    print("4. System EXIT")
    try:
        MODE = int(input("Please enter the Service code..."))
    except ValueError:
        print("❌ ERROR: The code MUST be a NUMBER!")
        continue

    if MODE == 1:
        name = input("Please set your USERNAME:")
        pswd = input("Please set your 6-DIGIT PASSWORD:")
        if name in user_database:
            print("❌ FAILURE: The user ALREADY EXISTS!")
        elif len(pswd) != 6:
            print("❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
        else:
            user_database[name] = pswd
            print("✅ ACCESS!")
    elif MODE == 2:
        user = input("Please enter your USERNAME:")
        pwd = input("Please enter your PASSWORD:")
        
        if user in user_database and user_database[user] == pwd:
            print("✅ ACCESS!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
    elif MODE == 3:
        user = input("Please enter your USERNAME:")
        pwd = input("Please enter your PASSWORD:")
        if user in user_database and user_database[user] == pwd:
            del user_database[user]
            print("✅ Account LOG OFF!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
    elif MODE == 4:
        print("=== Thank you for your support! ===")
        break
    elif MODE == 0:
        admin_pwd = input("Please enter the ADMINISTRATOR PASSWORD:")
        if admin_pwd == "admin123":
            print(" === ✅ ACCESS! Welcome, ADMINISTRATOR! === ")
            while True:
                print("\nCurrent User Database:", user_database)
                print("\n--- ADMINISTRATOR OPTIONS ---")
                print("1. Add User")
                print("2. Remove User")
                print("3. Change Administrator Password")
                print("4. Reset System") 
                print("5. Return to Main Menu")

                OPTION = input("Option code:")    
                if OPTION == "1":
                    name = input("Please set the USERNAME to add:")
                    pswd = input("Please set the 6-DIGIT PASSWORD:")
                    if name in user_database:
                        print("❌ FAILURE: The user ALREADY EXISTS!")
                        continue
                    elif len(pswd) != 6:
                        print("❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
                        continue
                    else:
                        user_database[name] = pswd
                        print("✅ User ADDED!") 
                elif OPTION == "2":
                    name = input("Please enter the USERNAME to remove:")
                    if name in user_database:
                        del user_database[name]
                        print("✅ User REMOVED!")
                    else:
                        print("❌ FAILURE: The user does NOT EXIST!")
                elif OPTION == "3":
                    new_pwd = input("NEW ADMINISTRATOR PASSWORD:")
                    if len(new_pwd) < 6:
                        print("❌ FAILURE: The password must be at least 6 characters long!")
                    else:
                        admin_pwd = new_pwd
                        print("✅ Administrator password CHANGED!")
                elif OPTION == "4":
                    confirm_reset = input("⚠ SURE to RESET?\n⚠ (Yes/No): ")
                    if confirm_reset.lower() == "yes":
                        user_database.clear()
                        print("✅ System RESET! All users have been deleted.")
                        break
                    else:
                        print("❌ System RESET CANCELLED.")
                elif OPTION == "5":
                    print("◀◀◀Returning to Main Menu...")  
                    break
                else:
                    print("❌ FAILURE: INVALID OPTION!")
    else:
        print("❌ This service is NOT AVAILABLE yet!")