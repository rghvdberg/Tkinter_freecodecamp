# 17 - Using Databases
# 18 - Building Out The GUI for our Database App
# 19 - Delete A Record From Our Database
# 20 - Update A Record With SQLite

from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x600")
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


def update_record():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Commit Changes
    record_id = select_box.get()
    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address= :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()


# Edit/update record
def edit():
    global editor
    editor = Tk()
    editor.geometry("400x200")
    editor.title("Update Record")

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)
    # Create Text Box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0)
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    save_button_editor = Button(
        editor, text="Save Record", command=update_record)
    save_button_editor.grid(row=6, column=0, columnspan=2,
                            padx=10, pady=10, ipadx=90)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM addresses WHERE oid=" + select_box.get())
    records = c.fetchall()
    # print(record)
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    conn.commit()
    conn.close()


# Delete a record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid="+select_box.get())
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
    query_label.grid(column=0, row=12, columnspan=2)

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

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1)

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
select_label = Label(root, text="Select ID")
select_label.grid(row=9, column=0)

# Create Submit Button
submit_button = Button(root, text="Add record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Create Edit Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Commit Changes
# conn.commit()

# Close Connection
# conn.close()

root.mainloop()
