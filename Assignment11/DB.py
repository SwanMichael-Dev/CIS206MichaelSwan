import sqlite3

conn = sqlite3.connect('Northwind1.db.sql')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor]
print("Available tables:")
for i, table in enumerate(tables):
    print(f"{i+1}. {table}")
choice = int(input("Enter the number of the table to view: ")) - 1
if 0 <= choice < len(tables):
    table_name = tables[choice]
    cursor.execute(f"SELECT * FROM {table_name}")
    column_names = [description[0] for description in cursor.description]
    print(f"Table: {table_name}")
    print("-" * 80)
    print(" | ".join(column_names))
    print("-" * 80)
    for i, row in enumerate(cursor.fetchall()):
        print(f"{i+1} | " + " | ".join(str(value) for value in row))
else:
    print("Invalid table selection.")

while True:
    action = input("Choose an action (I)nsert, (U)pdate, (D)elete, or (Q)uit: ").upper()
    if action == 'Q':
        break

    if action not in ('I', 'U', 'D'):
        print("Invalid action. Please choose I, U, D, or Q.")
        continue

    table_name = input("Enter the table name (Customers, Employees, Products): ").title()
    if table_name not in ('Customers', 'Employees', 'Products'):
        print("Invalid table name. Please choose from Customers, Employees, or Products.")
        continue

    if action == 'I':
        # Get field values from the user
        field_values = []
        for column_name in column_names:
            value = input(f"Enter value for {column_name}: ")
            field_values.append(value)

        # Insert the new record
        insert_query = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(['?'] * len(column_names))})"
        cursor.execute(insert_query, field_values)
        conn.commit()
        print(f"Record inserted into {table_name} table.")

    elif action == 'U':
        # Display records for selection
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        for i, row in enumerate(records):
            print(f"{i+1} | " + " | ".join(str(value) for value in row))

        # Get row number and field name for update
        row_choice = int(input("Enter the number of the row to update: ")) - 1
        if 0 <= row_choice < len(records):
            record_to_update = records[row_choice]
            print("Available fields to update:")
            for i, column_name in enumerate(column_names):
                print(f"{i+1}. {column_name}")
            field_choice = int(input("Enter the number of the field to update: ")) - 1
            if 0 <= field_choice < len(column_names):
                field_to_update = column_names[field_choice]
                new_value = input(f"Enter the new value for {field_to_update}: ")

                # Update the record
                update_query = f"UPDATE {table_name} SET {field_to_update} = ? WHERE ROWID = ?"
                cursor.execute(update_query, (new_value, record_to_update[0]))
                conn.commit()
                print(f"Record updated in {table_name} table.")
            else:
                print("Invalid field selection.")
        else:
            print("Invalid row selection.")

    elif action == 'D':
        # Display records for selection
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        for i, row in enumerate(records):
            print(f"{i+1} | " + " | ".join(str(value) for value in row))

        # Get row number for deletion
        row_choice = int(input("Enter the number of the row to delete: ")) - 1
        if 0 <= row_choice < len(records):
            record_to_delete = records[row_choice]

            # Delete the record
            delete_query = f"DELETE FROM {table_name} WHERE ROWID = ?"
            cursor.execute(delete_query, (record_to_delete[0],))
            conn.commit()
            print(f"Record deleted from {table_name} table.")
        else:
            print("Invalid row selection.")

conn.close()
