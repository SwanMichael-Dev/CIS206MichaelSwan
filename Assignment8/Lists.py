import csv

customers = []
with open('Northwind.txt', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        customers.append(row)

def display_customers_sorted(customers, sort_by="company"):
   
    if sort_by.lower() == "company":
        customers.sort(key=lambda customer: customer[1])
        print("Company Name | Contact Name | Phone Number")
        print("-----------------------------------------")
        for customer in customers:
            print(f"{customer[1]} | {customer[2]} | {customer[5]}")
    elif sort_by.lower() == "contact":
        customers.sort(key=lambda customer: customer[2])
        print("Contact Name | Company Name | Phone Number")
        print("-----------------------------------------")
        for customer in customers:
            print(f"{customer[2]} | {customer[1]} | {customer[5]}")
    else:
        print("Invalid sort criteria. Please choose 'company' or 'contact'.")

def search_customers_by_field(customers, search_term, search_field="company"):
   
    if search_field.lower() == "company":
        print("Company Name | Contact Name | Phone Number")
        print("-----------------------------------------")
        for customer in customers:
            if search_term.lower() in customer[1].lower():
                print(f"{customer[1]} | {customer[2]} | {customer[5]}")
    elif search_field.lower() == "contact":
        print("Contact Name | Company Name | Phone Number")
        print("-----------------------------------------")
        for customer in customers:
            if search_term.lower() in customer[2].lower():
                print(f"{customer[2]} | {customer[1]} | {customer[5]}")
    else:
        print("Invalid search field. Please choose 'company' or 'contact'.")

def main():
 
    customers = []
    with open('Northwind.txt', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            customers.append(row)

    while True:
        choice = input("Choose an option:\n"
                       "1. Display customers sorted by company name\n"
                       "2. Display customers sorted by contact name\n"
                       "3. Search by company name\n"
                       "4. Search by contact name\n"
                       "5. Exit\n"
                       "Enter your choice: ")

        if choice == '1':
            display_customers_sorted(customers)
        elif choice == '2':
            display_customers_sorted(customers, sort_by="contact")
        elif choice == '3':
            search_term = input("Enter company name or part of a name: ")
            search_customers_by_field(customers, search_term)
        elif choice == '4':
            search_term = input("Enter contact name or part of a name: ")
            search_customers_by_field(customers, search_term, search_field="contact")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
