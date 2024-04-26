import psycopg2
import tkinter as tk

# Verbindungsinformationen
host = "IP_des_Servers"
dbname = "Datenbank_name"
user = "Datenbank_user"
password = "Datenbank_Password"
port = port_des_Servers

try:
    # Verbindung zur Datenbank herstellen
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
    cur = conn.cursor()

    # Funktion zum Anzeigen der Daten in der GUI basierend auf dem Filter
    def show_filtered_data(filter_by=None, value=None):
        # Erstellen einer Abfrage entsprechend dem Filter
        if filter_by and value:
            query = f"SELECT name, age, gender FROM person WHERE {filter_by} = %s;"
            cur.execute(query, (value,))
        else:
            cur.execute("SELECT name, age, gender FROM person;")
        data = cur.fetchall()

        # GUI erstellen, um Daten anzuzeigen
        root = tk.Tk()
        root.title("Personendaten")
        root.geometry("400x300")
        root.configure(bg="#2d93d2")

        # Funktion zum Anzeigen der Daten in der GUI
        def display_data():
            for person in data:
                person_str = f"Name: {person[0]}, Alter: {person[1]}, Geschlecht: {person[2]}"
                label = tk.Label(root, text=person_str, bg="#2d93d2")
                label.pack()

        # Daten anzeigen
        display_data()

        root.mainloop()

    # Funktion zum Erstellen der Filter-GUI
    def create_filter_gui():
        filter_window = tk.Toplevel()
        filter_window.title("Daten filtern")
        filter_window.geometry("300x150")
        filter_window.configure(bg="#2d93d2")

        # Dropdown-Menü für Filteroptionen
        filter_options = ["name", "age", "gender"]
        filter_var = tk.StringVar(filter_window)
        filter_var.set(filter_options[0])  # Standardwert festlegen

        filter_label = tk.Label(filter_window, text="Filtern nach:", bg="#2d93d2")
        filter_label.pack()
        filter_dropdown = tk.OptionMenu(filter_window, filter_var, *filter_options)
        filter_dropdown.pack()

        # Eingabefeld für den Filterwert
        value_label = tk.Label(filter_window, text="Wert:", bg="#2d93d2")
        value_label.pack()
        value_entry = tk.Entry(filter_window)
        value_entry.pack()

        # Funktion zum Anwenden des Filters und Anzeigen der Daten
        def apply_filter():
            filter_by = filter_var.get()
            value = value_entry.get()
            show_filtered_data(filter_by, value)
            filter_window.destroy()

        # Schaltfläche zum Anwenden des Filters
        apply_button = tk.Button(filter_window, text="Anwenden", command=apply_filter, bg="#8ec6eb")
        apply_button.pack()

    # Funktion zum Erstellen der GUI und Anzeigen der Daten
    def create_main_gui():
        root = tk.Tk()
        root.title("Datenbank GUI")
        root.geometry("300x150")
        root.configure(bg="#2d93d2")

        # Schaltfläche zum Öffnen des Filterfensters
        filter_button = tk.Button(root, text="Filtern", command=create_filter_gui, bg="#8ec6eb")
        filter_button.pack()

        # Schaltfläche zum Anzeigen aller Daten
        show_all_button = tk.Button(root, text="Alle anzeigen", command=show_filtered_data, bg="#8ec6eb")
        show_all_button.pack()

        root.mainloop()

    # GUI erstellen und Hauptprogramm ausführen
    create_main_gui()

except Exception as e:
    print(f"Fehler: {e}")

finally:
    # Verbindung und Cursor schließen
    if cur:
        cur.close()
    if conn:
        conn.close()
        print("Verbindung zur Datenbank geschlossen.")
