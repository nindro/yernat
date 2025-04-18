import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

def fetch_filtered_records():
    cur.execute("SELECT * FROM get_records_by_pattern('John')")
    records = cur.fetchall()
    for record in records:
        print(record)

def add_new_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    conn.autocommit = True
    cur.execute("CALL insert_data(%s, %s);", (name, number))

def modify_contact():
    name = input("Enter name to update: ")
    new_number = input("Enter new phone number: ")
    conn.autocommit = True
    cur.execute("CALL update_data(%s, %s);", (name, new_number))

def insert_sample_contacts():
    users = [
        ['Stark', '80789013456'],
        ['Admin', '80779903663'],
        ['Sasha', '80779903663p']
    ]
    print("Invalid entries:")
    cur.execute(f"CALL insert_list_of_users(ARRAY{users})")
    cur.execute("SELECT * FROM postgres.public.phone_book_incorrect_data")
    data = cur.fetchall()
    for entry in data:
        print(entry)

def show_paginated_data():
    limit = 3
    offset = 0
    cur.execute('SELECT * FROM paginating(%s, %s)', (limit, offset))
    results = cur.fetchall()
    for index, record in enumerate(results, start=1):
        print(f"{index}. Name: {record[1]}, Number: {record[2]}")

def remove_contact():
    option = input("Delete by:\n1 - Username\n2 - Phone Number\n")
    if option == '1':
        name = input("Enter username: ")
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", ('username', name))
    elif option == '2':
        number = input("Enter phone number: ")
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", ('phone', number))

print("Select an operation:\n"
      "1. View filtered records\n"
      "2. Add contact\n"
      "2.1 Update contact\n"
      "3. Insert multiple contacts\n"
      "4. View paginated records\n"
      "5. Delete contact")

choice = input("Enter your choice: ")

if choice == '1':
    fetch_filtered_records()
elif choice == '2':
    add_new_contact()
elif choice == '2.1':
    modify_contact()
elif choice == '3':
    insert_sample_contacts()
elif choice == '4':
    show_paginated_data()
elif choice == '5':
    remove_contact()

conn.commit()
cur.close()
conn.close()
