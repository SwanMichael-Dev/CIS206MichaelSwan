import csv

f = open("Northwind.txt", "r")   
customers = []
reader = csv.reader(f)
for row in reader:
    customers.append({"CustomerID": row[0], "CompanyName": row[1], "ContactName": row[2], "ContactTitle": row[3], "Address": row[4], "City": row[5], "Region": row[6], "PostalCode": row[7], "Country": row[8], "Phone": row[9], "Fax": row[10]})

def display_customers_by_company(customers):
    sorted_customers = sorted(customers, key=lambda customer: customer["CompanyName"])
    for customer in sorted_customers:
        print(f"Company Name: {customer['CompanyName']}")
        print(f"Contact Name: {customer['ContactName']}")
        print(f"Phone Number: {customer['Phone']}")

def display_customers_by_contact(customers):
    sorted_customers = sorted(customers, key=lambda customer: customer["ContactName"])
    for customer in sorted_customers:
        print(f"Contact Name: {customer['ContactName']}")
        print(f"Company Name: {customer['CompanyName']}")
        print(f"Phone Number: {customer['Phone']}")

def search_customers(customers, search_term, field):
    matching_customers = []
    for customer in customers:
        if search_term.lower() in customer[field].lower():
            matching_customers.append(customer)
    if matching_customers:
        for customer in matching_customers:
            print(f"Company Name: {customer['CompanyName']}")
            print(f"Contact Name: {customer['ContactName']}")
            print(f"Phone Number: {customer['Phone']}")
    else:
        print("No matching customers found.")

def main():
    while True:
        print("\nCustomer Management System")
        print("1. Display customers by company name")
        print("2. Display customers by contact name")
        print("3. Search for customers by company name")
        print("4. Search for customers by contact name")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_customers_by_company(customers)
        elif choice == '2':
            display_customers_by_contact(customers)
        elif choice == '3':
            search_term = input("Enter company name or part of name: ")
            search_customers(customers, search_term, "CompanyName")
        elif choice == '4':
            search_term = input("Enter contact name or part of name: ")
            search_customers(customers, search_term, "ContactName")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
