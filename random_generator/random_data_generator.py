# Random Data Generator
import random

clients=['Wild Atlantic Trade Inc.','Sea Relation LLC','Lux Ocean LLC','BlueFin Corp.']
products=['Frozen Squid Tubes','Frozen Squid Rings','Frozen Squid Tentacles']
destinations=['Los Angeles','New York','Seattle']

def rdm(a, b):
    for i in range(a, b):
        client=random.choice(clients)
        product=random.choice(products)
        destination=random.choice(destinations)
        quantity=random.randint(1000, 8001)
        price_per_kg=random.uniform(3.0, 5.0)
        total_usd=quantity * price_per_kg

        print(f"{i}: {{'client': '{client}',\n 'product': '{product}',\n 'destination': '{destination}',\n 'weight_kg': {quantity},\n 'price_per_kg': {price_per_kg:.2f}, \n'total_usd': {total_usd:.2f}}}")


a=int(input("Enter the starting index: "))
b=int(input("Enter the ending index: "))
rdm(a, b)