import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    cur.execute(
        'INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES (%s, %s);',
        (name, number)
    )

def import_from_csv():
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, number = row
            cur.execute(
                'INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES (%s, %s);',
                (name, number)
            )

def update_contact():
    name = input("Enter the name of the contact to update: ")
    new_number = input("Enter the new phone number: ")
    cur.execute(
        'UPDATE postgres.public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s;',
        (new_number, name)
    )

def export_contacts():
    cur.execute('SELECT * FROM postgres.public.phone_book;')
    records = cur.fetchall()
    output_path = r"C:\Users\ernat\Desktop\mypgsql\Lab#10\phonebook\queredData.txt"

    with open(output_path, "w") as file:
        for row in records:
            file.write(f"Name: {row[1]}\nNumber: {row[2]}\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    cur.execute(
        'DELETE FROM postgres.public.phone_book WHERE "PersonName" = %s;',
        (name,)
    )

def delete_all_contacts():
    cur.execute('DELETE FROM postgres.public.phone_book;')

def main():
    while True:
        print("\nChoose an action:")
        print("1. Add a new contact")
        print("2. Import contacts from CSV")
        print("3. Update an existing contact")
        print("4. Export contacts to file")
        print("5. Delete a contact by name")
        print("6. Delete all contacts")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1–7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_contact()
        elif choice == 2:
            import_from_csv()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            export_contacts()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            delete_all_contacts()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")

        conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
