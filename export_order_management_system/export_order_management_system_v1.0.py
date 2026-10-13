# Honghua Seafood Export Management System V1.0

order_database={
    1001:{
        "client": "Sea Relation, LLC",
        "destination": "USA",
        "product": "Frozen Squid Tubes",
        "weight_kg": 23100.0,
        "price_per_kg": 3.5,
        "total_usd": 80850.0
        },
    1002:{
        "client": "Sea Relation, LLC",
        "destination": "USA",
        "product": "Frozen Squid Tentacles",
        "weight_kg": 15000.0,
        "price_per_kg": 4.0,
        "total_usd": 60000.0
        }
}

print("=== Welcome to Honghua Seafood Export Management System V1.0 ===")
while True:
    print("\n--------------------------------------------")
    print("A. Order Input")
    print("B. Search & Filter")
    print("C. Compliance Check")
    print("D. Financial Analysis")
    print("E. System Exit")

    try:
        OPTION = input("Please select an option...").upper()
    except ValueError:
        print("❌ ERROR: The code MUST be a LETTER!")
        continue

    if OPTION == "A":
        order_id = int(input("Please enter the Order ID: "))
        client = input("Please enter the Client Name: ")
        destination = input("Please enter the Destination Country: ")
        product = input("Please enter the Product Name: ")
        weight_kg = float(input("Please enter the Weight in KG: "))
        price_per_kg = float(input("Please enter the Price per KG in USD: "))
        total_usd = weight_kg * price_per_kg

        order_database[order_id] = {
            "client": client,
            "destination": destination,
            "product": product,
            "weight_kg": weight_kg,
            "price_per_kg": price_per_kg,
            "total_usd": total_usd
        }
        print(f"✅ Order {order_id} has been added successfully!")
        continue

    elif OPTION == "B":
        search_id = int(input("Please enter the Order ID to search: "))
        if search_id in order_database:
            order = order_database[search_id]
            print(f"Order ID: {search_id}")
            print(f"Client: {order['client']}")
            print(f"Destination: {order['destination']}")
            print(f"Product: {order['product']}")
            print(f"Weight (KG): {order['weight_kg']}")
            print(f"Price per KG (USD): {order['price_per_kg']}")
            print(f"Total (USD): {order['total_usd']}")
        else:
            print("❌ Order ID not found!")
        continue

    elif OPTION == "C":
        # Compliance Check logic can be implemented here
        print("Compliance Check feature is under development.")
        continue

    elif OPTION == "D":
        total_revenue = sum(order['total_usd'] for order in order_database.values())
        print(f"Total Revenue from all orders: ${total_revenue:.2f}")
        continue

    elif OPTION == "E":
        print("=== Thank you for using the system! ===")
        break

    else:
        print("❌ ERROR: Invalid option selected. Please try again.")
        continue