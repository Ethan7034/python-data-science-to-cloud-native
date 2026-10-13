#User Portal Login System V1.0
#Author: Ethan Gu

user_database = {"User": "123456"}

print("=== Welcome to the Login System V1.0 ===")

while True:
    print("\n-----------------------------")
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
        continue

    elif MODE == 2:
        user = input("Please enter your USERNAME:")
        pwd = input("Please enter your PASSWORD:")
        
        if user in user_database and user_database[user] == pwd:
            print("✅ ACCESS!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
        continue

    elif MODE == 3:
        user = input("Please enter your USERNAME:")
        pwd = input("Please enter your PASSWORD:")
        
        if user in user_database and user_database[user] == pwd:
            del user_database[user]
            print("✅ Account LOG OFF!")
        else:
            print("❌ FAILURE: INCORRECT username or password!")
        continue

    elif MODE == 4:
        print("👋=== Thank you for your support! ===")
        break

    else:
        print("❌ This service is NOT AVAILABLE yet!")
        continue
