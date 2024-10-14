import sqlite3

def interact_with_periodic_table():
    conn = sqlite3.connect('periodic_table_1900.db')
    cursor = conn.cursor()

    while True:
        element_symbol = input("Enter the symbol of the element you're interested in (or 'exit' to quit): ").capitalize()
        if element_symbol == 'Exit':
            break

        cursor.execute("SELECT * FROM periodic_table_1900 WHERE element_symbol = ?", (element_symbol,))
        element_data = cursor.fetchone()

        if element_data:
            print("\nElement Details:")
            print("-" * 30)
            print("Atomic Number:", element_data[0])
            print("Element Symbol:", element_data[1])
            print("Element Name:", element_data[2])
            print("Atomic Mass:", element_data[3])
            print("-" * 30)

            action = input("\nDo you want to 'update' or 'delete' this element (or 'back' to go back)? ").lower()
            if action == 'update':
                field_to_update = input("What do you want to update ('name' or 'mass')? ").lower()
                if field_to_update == 'name':
                    new_name = input("Enter the new name: ")
                    cursor.execute("UPDATE periodic_table_1900 SET element_name = ? WHERE element_symbol = ?", (new_name, element_symbol))
                elif field_to_update == 'mass':
                    new_mass = float(input("Enter the new atomic mass: "))
                    cursor.execute("UPDATE periodic_table_1900 SET atomic_mass = ? WHERE element_symbol = ?", (new_mass, element_symbol))
                else:
                    print("Invalid field to update.")
                    continue

                conn.commit()
                print("Element updated successfully!")

                cursor.execute("SELECT * FROM periodic_table_1900 WHERE element_symbol = ?", (element_symbol,))
                updated_data = cursor.fetchone()
                print("\nUpdated Element Details:")
                print("-" * 30)
                print("Atomic Number:", updated_data[0])
                print("Element Symbol:", updated_data[1])
                print("Element Name:", updated_data[2])
                print("Atomic Mass:", updated_data[3])
                print("-" * 30)

            elif action == 'delete':
                confirm = input(f"Are you sure you want to delete {element_data[2]} (y/n)? ").lower()
                if confirm == 'y':
                    cursor.execute("DELETE FROM periodic_table_1900 WHERE element_symbol = ?", (element_symbol,))
                    conn.commit()
                    print("Element deleted successfully!")
                else:
                    print("Deletion cancelled.")

            elif action != 'back':
                print("Invalid action.")

        else:
            print("Element not found.")

    conn.close()

if __name__ == "__main__":
    interact_with_periodic_table()