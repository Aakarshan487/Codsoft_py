import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("650x400")
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Contact Management System", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.listbox_frame = tk.Frame(main_frame)
        self.listbox_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.listbox_frame, height=15, width=50, yscrollcommand=self.scrollbar.set, font=("Helvetica", 12))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

        self.buttons_frame = tk.Frame(main_frame)
        self.buttons_frame.pack(side=tk.RIGHT, padx=10)

        button_font = ("Helvetica", 12)
        button_width = 12
        button_height = 2

        self.add_button = tk.Button(self.buttons_frame, text="Add Contact", command=self.add_contact, font=button_font, width=button_width, height=button_height, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.buttons_frame, text="View Contacts", command=self.view_contacts, font=button_font, width=button_width, height=button_height, bg="#2196F3", fg="white")
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.buttons_frame, text="Search Contact", command=self.search_contact, font=button_font, width=button_width, height=button_height, bg="#FFC107", fg="white")
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.buttons_frame, text="Update Contact", command=self.update_contact, font=button_font, width=button_width, height=button_height, bg="#FF5722", fg="white")
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Contact", command=self.delete_contact, font=button_font, width=button_width, height=button_height, bg="#F44336", fg="white")
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        if name and phone and email and address:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please provide all the details.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self):
        query = simpledialog.askstring("Input", "Enter name or phone to search:")
        if query:
            results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]
            if results:
                self.listbox.delete(0, tk.END)
                for contact in results:
                    self.listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}")
            else:
                messagebox.showinfo("No Results", "No contacts found.")
        else:
            messagebox.showwarning("Input Error", "Please provide a search query.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to update:")
        if name:
            for contact in self.contacts:
                if contact['name'] == name:
                    new_phone = simpledialog.askstring("Input", "Enter new phone (leave blank if no change):")
                    new_email = simpledialog.askstring("Input", "Enter new email (leave blank if no change):")
                    new_address = simpledialog.askstring("Input", "Enter new address (leave blank if no change):")

                    if new_phone:
                        contact['phone'] = new_phone
                    if new_email:
                        contact['email'] = new_email
                    if new_address:
                        contact['address'] = new_address

                    messagebox.showinfo("Success", "Contact updated successfully.")
                    return

            messagebox.showinfo("No Results", "Contact not found.")
        else:
            messagebox.showwarning("Input Error", "Please provide a name.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to delete:")
        if name:
            self.contacts = [contact for contact in self.contacts if contact['name'] != name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Input Error", "Please provide a name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementSystem(root)
    root.mainloop()