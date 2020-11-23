import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor - mowi bases co chcemy zrobić
x = conn.cursor()

x.execute(""" UPDATE customers SET first_name = 'Jakub'
            WHERE rowid = 1 
            """)

conn.commit()

x.execute("SELECT rowid, * FROM customers")

items = x.fetchall()

print("Command executed succesfully...")
# Commit our command - musimy zakomunikować komunikacje :)

for item in items:
    print(item)
# Close our connection - dobra praktyka
# conn.close()
