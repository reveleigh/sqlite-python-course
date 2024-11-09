import sqlite3

def analyse_sales_data():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    while True:
        os_search = input("Enter the OS to search for (or 'exit' to quit): ")
        if os_search.lower() == 'exit':
            break

        cursor.execute() #Add query here
        total_sales = cursor.fetchone()[0]

        if total_sales is not None:
            print(f"There were {total_sales} sales of devices with the {os_search} operating system.")
        else:
            print(f"No sales records found for {os_search}.")

    conn.close()

analyse_sales_data()