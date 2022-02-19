import sqlite3

#create table monthly if not exists with name, occurence and price

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS monthly (name TEXT, occurence INTEGER, price REAL)")
    conn.commit()
    conn.close()

#a function to add new row to the table

def insert(name, occurence, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO monthly VALUES (?, ?, ?)", (name, occurence, price))
    conn.commit()
    conn.close()

# a function to delete a row from the table with a certain name

def delete(name):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM monthly WHERE name=?", (name,))
    conn.commit()
    conn.close()

#a function to update a row in the table with a certain name

def update(name, occurence, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE monthly SET occurence=?, price=? WHERE name=?", (occurence, price, name))
    conn.commit()
    conn.close()

#a function to view all rows in the table
def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT name, occurence, price FROM monthly")
    rows = cur.fetchall()
    conn.close()
    return rows

#function to get the sum of occurence multiplied by price

def sum_of_occurence():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT SUM(occurence * price) FROM monthly")
    rows = cur.fetchall()
    conn.close()
    return rows

# a function to create a graph of the rows in the table using matplotlib based on name and price multiplied by occurence

def graph():
    import matplotlib.pyplot as plt
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT name ,(occurence * price) as monthly_price FROM monthly")
    rows = cur.fetchall()
    x = []
    y = []
    for row in rows:
        x.append(row[0])
        y.append(row[1])
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
    plt.title('Expenses')
    plt.xlabel('Occurence')
    plt.ylabel('Price')
    plt.show()
    conn.close()

# a loop for the user to interact with the program

while True:
    print("""
    1. Create a new table
    2. Insert a new row
    3. Delete a row
    4. Update a row
    5. View all rows
    6. Sum of occurence
    7. Graph
    8. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        create_table()
    elif choice == '2':
        name = input("Enter the name of the item: ")
        occurence = int(input("Enter the occurence: "))
        price = float(input("Enter the price: "))
        insert(name, occurence, price)
    elif choice == '3':
        name = input("Enter the name of the item: ")
        delete(name)
    elif choice == '4':
        name = input("Enter the name of the item: ")
        occurence = int(input("Enter the occurence: "))
        price = float(input("Enter the price: "))
        update(name, occurence, price)
    elif choice == '5':
        print(view())
    elif choice == '6':
        print(sum_of_occurence())
    elif choice == '7':
        graph()
    elif choice == '8':
        break
    else:
        print("Invalid choice")