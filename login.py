import tkinter as tk
from tkinter import messagebox
from auth import *
import gui

create_user_table()
create_admin()


def login():
    username = user_entry.get()
    password = pass_entry.get()

    if login_user(username, password):
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        gui.open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")


root = tk.Tk()
root.title("Student Management System")
root.geometry("500x550")
root.configure(bg="#0F172A")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎓 Student Management System",
    font=("Segoe UI", 22, "bold"),
    bg="#0F172A",
    fg="white"
)
title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="Administrator Login",
    font=("Segoe UI", 12),
    bg="#0F172A",
    fg="#94A3B8"
)
subtitle.pack()

tk.Label(
    root,
    text="Username",
    bg="#0F172A",
    fg="white",
    font=("Segoe UI", 11)
).pack(pady=(30,5))

user_entry = tk.Entry(
    root,
    font=("Segoe UI",12),
    width=28
)
user_entry.pack(ipady=6)

tk.Label(
    root,
    text="Password",
    bg="#0F172A",
    fg="white",
    font=("Segoe UI",11)
).pack(pady=(20,5))

pass_entry = tk.Entry(
    root,
    show="*",
    font=("Segoe UI",12),
    width=28
)
pass_entry.pack(ipady=6)

tk.Button(
    root,
    text="LOGIN",
    command=login,
    bg="#2563EB",
    fg="white",
    font=("Segoe UI",12,"bold"),
    width=20,
    height=2,
    cursor="hand2"
    
).pack(pady=40)

tk.Label(
    root,
    text="© 2026 Student Management System",
    bg="#1D1C27",
    fg="gray",
    font=("Segoe UI",9)
).pack(side="bottom", pady=20)

root.mainloop()