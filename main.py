from tkinter import *
from passmanager import PasswordManager

# ---------------------------- UI SETUP ------------------------------- #

# Inicializamos una ventana
window = Tk()
# Le damos el título de la ventana
window.title("Gestor de contraseñas")
window.config(padx=50, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
background = PhotoImage(file="logo.png")
canvas.create_image(105, 104, image=background)
canvas.grid(column=1, row=0)

website_label = Label(text="Sitio web", fg="white", font=("Courier", 12, "bold"), highlightthickness=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Usuario", fg="white", font=("Courier", 12, "bold"), highlightthickness=0)
email_label.grid(column=0, row=2)

password_label = Label(text="Contraseña", fg="white", font=("Courier", 12, "bold"), highlightthickness=0)
password_label.grid(column=0, row=3)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "crisbustaq@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

password_manager = PasswordManager(email_entry, website_entry, password_entry)

search_button = Button(text="Buscar", command=password_manager.find_password, width=13)
search_button.grid(column=2, row=1)

genpassword_button = Button(text="Generar contraseña", command=password_manager.generate_password)
genpassword_button.grid(column=2, row=3)

add_button = Button(text="Agregar", command=password_manager.save, width=36)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
