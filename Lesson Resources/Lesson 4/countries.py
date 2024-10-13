import tkinter as tk
import sqlite3

def get_population_data():
    """
    Fetches population data from the database based on user input.
    Returns a list of countries with their populations, sorted by population.
    """
    country = country_entry.get()
    year = year_entry.get()

    try:
        conn = sqlite3.connect('world_population.db')
        cursor = conn.cursor()

        # Get the population of the specified country and year
        cursor.execute(f"SELECT `_{year}` FROM world_population WHERE country_name = ?", (country,))
        target_population = cursor.fetchone()[0]

        # Fetch all countries and their populations for the given year
        cursor.execute(f"SELECT country_name, `_{year}` FROM world_population ORDER BY `_{year}` DESC")
        all_countries = cursor.fetchall()

        conn.close()

        return all_countries, target_population

    except Exception as e:
        error_label.config(text=f"Error: {e}")
        return None, None

def display_results():
    """
    Displays the previous 5 and next 5 countries by population in the results area.
    """
    all_countries, target_population = get_population_data()

    if all_countries:
        results = []
        target_index = None

        # Find the index of the target country
        for i, (country, population) in enumerate(all_countries):
            if country == country_entry.get():
                target_index = i
                break

        if target_index is not None:
            # Get the previous 5 and next 5 countries
            start_index = max(0, target_index - 5)
            end_index = min(len(all_countries), target_index + 6)
            results = all_countries[start_index:end_index]

            # Format the results
            output_text = f"Population of {country_entry.get()} in {year_entry.get()}: {target_population}\n\n"
            output_text += "Next 5 Countries:\n"
            for country, population in results[:5]:
                output_text += f"{country}: {population}\n"
            output_text += "\nPrevious 5 Countries:\n"
            for country, population in results[6:]:
                output_text += f"{country}: {population}\n"

            results_text.delete("1.0", tk.END)  # Clear previous results
            results_text.insert(tk.END, output_text)
        else:
            error_label.config(text="Country not found.")

# Create the main window
window = tk.Tk()
window.title("World Population Lookup")

# Country input
country_label = tk.Label(window, text="Country Name:")
country_label.pack()
country_entry = tk.Entry(window)
country_entry.pack()

# Year input
year_label = tk.Label(window, text="Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Button to fetch and display data
fetch_button = tk.Button(window, text="Fetch Data", command=display_results)
fetch_button.pack()

# Error label
error_label = tk.Label(window, text="", fg="red")
error_label.pack()

# Results area
results_text = tk.Text(window)
results_text.pack()

window.mainloop()