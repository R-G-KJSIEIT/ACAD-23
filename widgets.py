import tkinter as tk

root = tk.Tk()
root.title("Login")

username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")

username_label.grid(row=0, column=0, sticky="W")
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0, sticky="W")
password_entry.grid(row=1, column=1)

def show_text():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

submit_button = tk.Button(root, text="Submit", command=show_text)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
