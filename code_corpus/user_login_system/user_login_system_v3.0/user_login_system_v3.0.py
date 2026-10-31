#Portal Login System V3.0
#Author: Ethan Gu
import hashlib
import pwinput
import json
import os

def save_user_database():
    with open("user_database.json", "w") as f:
        json.dump(user_database, f)

def hash_password(password):
    pwd_bytes = password.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd

if __name__ == "__main__":
    # Check if the user database file exists
    if os.path.exists("user_database.json"):
        with open("user_database.json", "r") as f:
            user_database = json.load(f)
    else:
        user_database = {"User": hash_password("123456"), "__admin__": hash_password("admin123")}
        save_user_database()

    print("=== Welcome to the Login System V3.0 ===")
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
        pswd = pwinput.pwinput("Please set your 6-DIGIT PASSWORD:")
        if name == "__admin__":
            print("❌ FAILURE: The username is RESERVED!")
        elif name in user_database:
            print("❌ FAILURE: The username is ALREADY TAKEN!")
        elif len(pswd) != 6:
            print("❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
        else:
            user_database[name] = hash_password(pswd)
            save_user_database()
            print("✅ ACCESS!")
    elif MODE == 2:
        user = input("Please enter your USERNAME:")
        pwd = pwinput.pwinput("Please enter your PASSWORD:")
        pwd = hash_password(pwd)
        if user in user_database and user_database[user] == pwd:
            print("✅ ACCESS!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
    elif MODE == 3:
        user = input("Please enter your USERNAME:")
        pwd = pwinput.pwinput("Please enter your PASSWORD:")
        pwd = hash_password(pwd)
        if user in user_database and user_database[user] == pwd:
            del user_database[user]
            save_user_database()
            print("✅ Account LOG OFF!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
    elif MODE == 4:
        print("=== Thank you for your support! ===")
        break
    elif MODE == 0:
        admin_pwd = pwinput.pwinput("Please enter the ADMINISTRATOR PASSWORD:")
        if hash_password(admin_pwd) == user_database.get("__admin__", hash_password("admin123")):
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
                    pswd = pwinput.pwinput("Please set the 6-DIGIT PASSWORD:")
                    if name == "__admin__":
                        print("❌ FAILURE: The username is RESERVED!")
                    elif name in user_database:
                        print("❌ FAILURE: The username is ALREADY TAKEN!")
                    elif len(pswd) != 6:
                        print("❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
                    else:
                        user_database[name] = hash_password(pswd)
                        save_user_database()
                        print("✅ User ADDED!") 
                elif OPTION == "2":
                    name = input("Please enter the USERNAME to remove:")
                    if name in user_database:
                        del user_database[name]
                        save_user_database()
                        print("✅ User REMOVED!")
                    else:
                        print("❌ FAILURE: The user does NOT EXIST!")
                elif OPTION == "3":
                    new_pwd = pwinput.pwinput("NEW ADMINISTRATOR PASSWORD:")
                    if len(new_pwd) < 6:
                        print("❌ FAILURE: The password must be at least 6 characters long!")
                    else:
                        user_database["__admin__"] = hash_password(new_pwd)
                        save_user_database()
                        print("✅ Administrator password CHANGED!")
                elif OPTION == "4":
                    confirm_reset = input("⚠ SURE to RESET?\n⚠ (Yes/No): ")
                    if confirm_reset.lower() == "yes":
                        user_database.clear()
                        save_user_database()
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