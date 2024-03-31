# Task 1: Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(hotel, room, customer_name):
    try:
        if room in hotel:
            if hotel[room]["status"] == "available":
                hotel[room]["status"] = "booked"
                hotel[room]["customer"] = customer_name
            else:
                print("That room is already booked!")
        else:
            print("That room doesnt exist!")
    except:
        print("Must input a valid room number!")

def check_out(hotel, room):
    if room in hotel:        
        hotel[room]["status"] = "available"
        hotel[room]["customer"] = ""
    else:
        print("That room doesnt exist!")

def view_status(hotel):
    print("This hotel has these rooms:")
    for room in hotel.keys():
        print(f"    {room}:")
        for attribute in hotel[room].items():
            print(f"        {attribute}")


#book_room(hotel_rooms, input("Which room would you like to book? "), input("What is you name? "))
#check_out(hotel_rooms, input("What room are you checking out of? "))
#view_status(hotel_rooms)


# Task 2: E-commerce Product Search Feature

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20},
    "3": {"name": "Shirt", "category": "Clothing", "price": 20},
    "4": {"name": "laptop", "category": "Electronics", "price": 400},
    "5": {"name": "SHIRT", "category": "Clothing", "price": 20},
    "6": {"name": "Pants", "category": "Clothing", "price": 20}
}

def search_product(product_search):
    matching_products = []
    for product in products.values():
        if product["name"].lower() == product_search.lower():
            matching_products.append(product)

    if matching_products:
        for product in matching_products:
            print(product)
    else:
        print("Could not find a match!")

search_product(input("What product are you searching for? "))