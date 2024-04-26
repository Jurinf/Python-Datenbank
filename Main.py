import tkinter as tk

def run_code1():
    import Eintragen

def run_code2():
    import Auswaehlen

root = tk.Tk()
root.title("Auswahlmenü")
root.geometry("300x150")
root.configure(bg="#2d93d2")

label = tk.Label(root, text="Bitte wählen Sie aus:", bg="#2d93d2")
label.pack()

button1 = tk.Button(root, text="Personen eintragen", command=run_code1, bg="#8ec6eb")
button1.pack()

button2 = tk.Button(root, text="Personen auswählen", command=run_code2, bg="#8ec6eb")
button2.pack()

root.mainloop()
