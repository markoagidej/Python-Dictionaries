# Task 1: Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

current_ticket = 3

def open_ticket():
    customer = input("What is the name of the customer?\n")
    issue    = input("What is a description of the issue?\n")

    global current_ticket

    service_tickets[f"Ticket{str(current_ticket).zfill(3)}"] = {
        "Customer": customer,
        "Issue": issue,
        "Status": "open"
    }

    current_ticket += 1


def update_ticket(ticket_number):
    if ticket_number.isnumeric():
        if len(ticket_number) == 3:
            ticket_key = "Ticket" + ticket_number
            if ticket_key in service_tickets:
                if service_tickets[ticket_key]["Status"] == "closed":
                    print(f"{ticket_key} already set to \'closed\'")
                else:
                    service_tickets[ticket_key]["Status"] = "closed"
                    print(f"{ticket_key} set to \'closed\'")
            else:
                print(f"Ticket{ticket_number} does not exist!")
        else:
            print("Input must be three digits long!")
    else:
        print("Enter only numbers!")



def display_tickets(filter):
    if filter:
        filter_list = []
        if filter == "open":
            for ticket_num, details in service_tickets.items():
                if details["Status"] == "open":
                    filter_list.append((ticket_num, details))
        elif filter == "closed":
            for ticket_num, details in service_tickets.items():
                if details["Status"] == "closed":
                    filter_list.append((ticket_num, details))
        else:
            print("Enter a valid filter (open/closed)")

        if filter_list:
            for item in filter_list:
                print(item)
        else:
            print(f"There are no tickets that are {filter}!")
    else:
        for ticket, details in service_tickets.items():
            print(ticket, details)


open_ticket()
#open_ticket()
#open_ticket()
update_ticket(input("Enter ticket number padded with zeros up to three digits (eg. 009): "))
display_tickets(input("Enter a status (open/closed) to filter by, or enter nothing for no filter. "))