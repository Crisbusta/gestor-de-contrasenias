import json
import pyperclip
from tkinter import messagebox, END
from random import choice, randint, shuffle

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordManager:
    def __init__(self, email, website, password):
        self.email_entry = email
        self.website_entry = website
        self.password_entry = password

    def generate_password(self):
        password_letters = [choice(LETTERS) for _ in range(randint(8, 12))]
        password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
        password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
        pre_password = password_letters + password_symbols + password_numbers
        shuffle(pre_password)
        password = "".join(pre_password)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save(self):
        website = self.website_entry.get().capitalize()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {website: {
            "email": email,
            "password": password
        }}

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops, algo salió mal", message="Asegurate de no dejar ninguna casilla vacía")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Leyendo la data antigua
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Actualizando la data antigua
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Cargamos la nueva data
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def find_password(self):
        website = self.website_entry.get().capitalize()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Archivo no existe")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n"
                                                                f"Contraseña: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No existen registros de {website}")
