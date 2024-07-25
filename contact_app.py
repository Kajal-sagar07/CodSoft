import tkinter as tk
from tkinter import messagebox

phone_book = []

def add_contact():
    global phone_book
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Name is required.")
        return

    try:
        number = int(number)
    except ValueError:
        messagebox.showerror("Error", "Number must be a valid integer.")
        return

    phone_book.append([name, number, email])
    messagebox.showinfo("Phonebook", "Contact added successfully.")
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def update_contact():
    global phone_book
    try:
        index = int(index_entry.get())
        if index < 1 or index > len(phone_book):
            messagebox.showerror("Error", f"Invalid index. Index should be between 1 and {len(phone_book)}.")
            return
    except ValueError:
        messagebox.showerror("Error", "Index must be a valid integer.")
        return

    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Name is required.")
        return

    try:
        number = int(number)
    except ValueError:
        messagebox.showerror("Error", "Number must be a valid integer.")
        return

    phone_book[index - 1] = [name, number, email]
    messagebox.showinfo("Phonebook", "Contact updated successfully.")
    clear_entries()

def delete_contact():
    global phone_book
    try:
        index = int(index_entry.get())
        if index < 1 or index > len(phone_book):
            messagebox.showerror("Error", f"Invalid index. Index should be between 1 and {len(phone_book)}.")
            return
    except ValueError:
        messagebox.showerror("Error", "Index must be a valid integer.")
        return

    del phone_book[index - 1]
    messagebox.showinfo("Phonebook", "Contact deleted successfully.")
    clear_entries()

def display_all():
    global phone_book
    if not phone_book:
        messagebox.showinfo("Phonebook", "List is empty.")
    else:
        display_text = ""
        for index, contact in enumerate(phone_book, start=1):
            display_text += f"Contact {index}: Name: {contact[0]}, Number: {contact[1]}, Email: {contact[2]}\n"
        messagebox.showinfo("Phonebook", display_text)

def view_contact():
    global phone_book
    try:
        index = int(index_entry.get())
        if index < 1 or index > len(phone_book):
            messagebox.showerror("Error", f"Invalid index. Index should be between 1 and {len(phone_book)}.")
            return
    except ValueError:
        messagebox.showerror("Error", "Index must be a valid integer.")
        return

    contact = phone_book[index - 1]
    display_text = f"Name: {contact[0]}\nNumber: {contact[1]}\nEmail: {contact[2]}"
    messagebox.showinfo("Contact Details", display_text)

def search_contact():
    global phone_book
    search_name = name_entry.get().strip()

    if not search_name:
        messagebox.showerror("Error", "Please enter a name to search.")
        return

    found = False
    for contact in phone_book:
        if contact[0].lower() == search_name.lower():
            display_text = f"Name: {contact[0]}\nNumber: {contact[1]}\nEmail: {contact[2]}"
            messagebox.showinfo("Contact Details", display_text)
            found = True
            break

    if not found:
        messagebox.showinfo("Search Result", f"No contact found with name '{search_name}'.")

def EXIT():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Smartphone Directory")
root.geometry("370x450")  # Set initial size of the window (width x height)
root.resizable(0, 0)  # Disable resizing
root.configure(bg = "#FAEBD8")  # Set background color

# Custom label for title with a different font
title_label = tk.Label(root, text="Smartphone Directory", font=("", 20, "bold"))
title_label.grid(row=0, column=2, columnspan=2, padx=10, pady=(10, 20))

# Labels and Entry widgets for Name, Number, Email, Index
name_label = tk.Label(root, text="Name:", width=10, anchor='w')
name_label.grid(row=1, column=2, padx=10, pady=10)

name_entry = tk.Entry(root)
name_entry.grid(row=1, column=3, padx=10, pady=10)

number_label = tk.Label(root, text="Number:", width=10, anchor='w')
number_label.grid(row=2, column=2, padx=10, pady=10)

number_entry = tk.Entry(root)
number_entry.grid(row=2, column=3, padx=10, pady=10)

email_label = tk.Label(root, text="Email:", width=10, anchor='w')
email_label.grid(row=3, column=2, padx=10, pady=10)

email_entry = tk.Entry(root)
email_entry.grid(row=3, column=3, padx=10, pady=10)

index_label = tk.Label(root, text="Index (1-based):", width=20, anchor='w')
index_label.grid(row=4, column=2, padx=10, pady=10)

index_entry = tk.Entry(root)
index_entry.grid(row=4, column=3, padx=10, pady=10)

# Buttons for various operations
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white")
add_button.grid(row=5, column=2, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact, bg="blue", fg="white")
update_button.grid(row=5, column=3, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white")
delete_button.grid(row=6, column=2, padx=10, pady=10)

display_button = tk.Button(root, text="Display All Contacts", command=display_all, bg="purple", fg="white")
display_button.grid(row=6, column=3, padx=10, pady=10)

view_button = tk.Button(root, text="View Contact", command=view_contact, bg="orange", fg="white")
view_button.grid(row=7, column=3, columnspan=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact, bg="yellow", fg="black")
search_button.grid(row=7, column=2, columnspan=2, padx=0, pady=10)

exit_button = tk.Button(root, text="EXIT", command=EXIT, bg="dark red", fg="white")
exit_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()