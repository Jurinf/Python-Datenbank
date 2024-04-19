import psycopg2
import tkinter as tk
from CTkMessagebox import CTkMessagebox

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

    # Tabelle erstellen, wenn sie nicht existiert
    cur.execute("""CREATE TABLE IF NOT EXISTS person2 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR
    );
    """)

    def create_person_gui():
        person_window = tk.Toplevel()
        person_window.title("Person erstellen")
        person_window.geometry("300x150")
        person_window.configure(bg="#2d93d2")

        name_label = tk.Label(person_window, text="Name:", bg="#2d93d2")
        name_label.pack()
        name_entry = tk.Entry(person_window)
        name_entry.pack()

        age_label = tk.Label(person_window, text="Alter:", bg="#2d93d2")
        age_label.pack()
        age_entry = tk.Entry(person_window)
        age_entry.pack()

        gender_label = tk.Label(person_window, text="Geschlecht:", bg="#2d93d2")
        gender_label.pack()
        gender_entry = tk.Entry(person_window)
        gender_entry.pack()

        def save_person():
            name = name_entry.get()
            age = int(age_entry.get())
            gender = gender_entry.get()

            cur.execute("""INSERT INTO person (name, age, gender) VALUES (%s, %s, %s);""", (name, age, gender))
            conn.commit()
            person_window.destroy()
            CTkMessagebox(title="Erfolg", message="Daten gespeichert.", icon="check", option_1="Ok")

        save_button = tk.Button(person_window, text="Speichern", command=save_person, bg="#8ec6eb")
        save_button.pack()

    def create_person():
        root = tk.Tk()
        root.title("Anzahl eingeben")
        root.geometry("300x150")
        root.configure(bg="#2d93d2")

        def submit():
            count = int(entry.get())
            for _ in range(count):
                create_person_gui()

        label = tk.Label(root, text="Anzahl der Personen eingeben:", bg="#2d93d2")
        label.pack()

        entry = tk.Entry(root)
        entry.pack()

        submit_button = tk.Button(root, text="Submit", command=submit, bg="#8ec6eb")
        submit_button.pack()

        root.mainloop()

    create_person()

except Exception as e:
    print(f"Fehler: {e}")

finally:
    # Verbindung schließen
    if conn:
        conn.close()
        print("Verbindung zur Datenbank geschlossen.")
