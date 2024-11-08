import sqlite3

def display_table_data():
    # Connect to the database
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # Retrieve the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]

    # Print the list of tables
    print("Available tables:")
    for i, table in enumerate(tables, 1):
        print(f"{i}. {table}")

    # Ask the user to select a table by index
    try:
        table_index = int(input("Enter the number of the table you want to display: ")) - 1
        if table_index < 0 or table_index >= len(tables):
            print("Invalid table number selected.")
            conn.close()
            return

        selected_table = tables[table_index]

        # Retrieve and print all data from the selected table
        cursor.execute(f"SELECT * FROM {selected_table}")
        rows = cursor.fetchall()
        print(f"\nData from table '{selected_table}':")
        for row in rows:
            print(row)

    except ValueError:
        print("Please enter a valid number.")
    finally:
        # Close the database connection
        conn.close()

# Example usage:
display_table_data()