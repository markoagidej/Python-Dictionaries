# Task 1: Sales Data Cloning and Modification

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

new_weekly_sales = copy.deepcopy(weekly_sales)

new_weekly_sales["Week 2"]["Electronics"] = 18000

def print_dict(sales_dict, dict_name):
    print(dict_name)
    for key, value in sales_dict.items():
        print(f"    {key}, {value}")

print_dict(weekly_sales, "weekly_sales")
print_dict(new_weekly_sales, "new_weekly_sales")