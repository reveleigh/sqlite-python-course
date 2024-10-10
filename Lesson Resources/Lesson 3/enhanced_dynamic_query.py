import sqlite3

def search_cars():
    conn = sqlite3.connect('car_showroom.db')
    cursor = conn.cursor()

    colour = input("Enter car colour (or leave blank to skip): ").title()
    make = input("Enter car make (or leave blank to skip): ").title()
    min_price = input("Enter minimum price (or leave blank to skip): ")
    max_price = input("Enter maximum price (or leave blank to skip): ")
    min_year = input("Enter minimum model year (or leave blank to skip): ")
    max_year = input("Enter maximum model year (or leave blank to skip): ")

    query = "SELECT * FROM inventory WHERE 1=1" # Start with a true condition to simplify adding AND clauses
    params = []

    if colour:
        query += " AND colour = ?"
        params.append(colour)
    if make:
        query += " AND make = ?"
        params.append(make)
    if min_price:
        query += " AND price >= ?"
        params.append(int(min_price))
    if max_price:
        query += " AND price <= ?"
        params.append(int(max_price))
    if min_year:
        query += " AND model_year >= ?"
        params.append(int(min_year))
    if max_year:
        query += " AND model_year <= ?"
        params.append(int(max_year))

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()

        if results:
            print("\nMatching cars:")
            print("-" * 78)  # Print a separator line
            # Print the header row with column names centered within their respective widths
            print("|{:^10}|{:^15}|{:^15}|{:^10}|{:^10}|{:^10}|".format("ID", "Make", "Model", "Year", "Colour", "Price"))
            # Print a separator line to visually separate the header from the data rows
            print("-" * 78)
            for row in results:
                print("|{:^10}|{:^15}|{:^15}|{:^10}|{:^10}|{:^10}|".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            print("-" * 78)  # Print a separator line
        else:
            print("No cars match your criteria.")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and year.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    search_cars()