# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_category(menu, new_category, new_items):
    if new_category not in menu:
        menu[new_category] = new_items
        print(f"New menu category, {new_category}, added with items {new_items.keys()}")
    else:
        print("That category already exists!")

def update_price(menu, category, item, new_price):
    try:
        if category in menu:
            try:
                if item in menu[category]:
                    menu[category][item] = new_price
                    print(f"Price of {item} now set to {new_price}.")
            except:
                print("That item does not exist!")
    except:
        print("That category does not exist!")

def remove_item(menu, category, item):
    try:
        if category in menu:
            try:
                if item in menu[category]:
                    menu[category].pop(item)
                    print(f"{item} removed from category {category}")
            except:
                print("That item does not exist!")
    except:
        print("That category does not exist!")

add_category(restaurant_menu, "Beverages", {"Coke": 2.99, "Pepsi": 2.99})
update_price(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")

for menu, item_list in restaurant_menu.items():
    print(menu)
    for item in restaurant_menu[menu].items():
        print(f"    {item}")