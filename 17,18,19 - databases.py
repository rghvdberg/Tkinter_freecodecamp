# 17 - Using Databases
# 18 - Building Out The GUI for our Database App
# 19 - Delete A Record From Our Database

from tkinter import *
import sqlite3

root = Tk()
root.geometry("800x600")
root.title("Using Databases")

# Create a database or connect to one
#conn = sqlite3.connect('address_book.db')

# Create cursor
#c = conn.cursor()

# # Create table
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode text
#     )""")

# Delete a record


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())
    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Commit Changes
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    conn.commit()
    # Close Connection
    conn.close()
    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + " "
        print_records += "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(column=0, row=11, columnspan=2)

    conn.commit()
    # Close Connection
    conn.close()
    # Clear Text Boxes


 # Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=38)
delete_box.grid(row=9, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_label = Label(root, text="Delete ID")
delete_label.grid(row=9, column=0)

# Create Submit Button
submit_button = Button(root, text="Add record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Commit Changes
#conn.commit()

# Close Connection
#conn.close()

root.mainloop()
