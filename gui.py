
"""
gui.py
------
Tkinter GUI front-end for Student Management System

Run:
python gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox

from db import Database
from validators import validate_student_fields


class StudentApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # ---------------- WINDOW ----------------

        self.title("🎓 Student Management System")
        self.geometry("1200x700")
        self.configure(bg="#0F172A")
        self.resizable(False, False)

        # ---------------- DATABASE ----------------

        self.db = Database()
        self.selected_id = None

        # ---------------- UI ----------------

        self.create_header()
        self.create_form()
        self._build_buttons()
        self._build_table()

        self.refresh_table()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self,
            bg="#1E3A8A",
            height=70
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="🎓 STUDENT MANAGEMENT SYSTEM",
            bg="#1E3A8A",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(
            side="left",
            padx=20
        )

        self.total_label = tk.Label(
            header,
            text="Total Students : 0",
            bg="#1E3A8A",
            fg="white",
            font=("Segoe UI", 12, "bold")
        )

        self.total_label.pack(
            side="right",
            padx=20
        )

    # =========================================================
    # FORM
    # =========================================================

    def create_form(self):

        form = tk.Frame(
            self,
            bg="#0F172A"
        )

        form.pack(
            fill="x",
            padx=20,
            pady=20
        )

        labels = [
            "Name",
            "Age",
            "Email",
            "Course",
            "Grade"
        ]

        self.entries = {}

        for i, label in enumerate(labels):

            tk.Label(
                form,
                text=label,
                bg="#0F172A",
                fg="white",
                font=("Segoe UI", 11)
            ).grid(
                row=i,
                column=0,
                pady=8,
                sticky="w"
            )

            entry = tk.Entry(
                form,
                width=40,
                font=("Segoe UI", 11)
            )

            entry.grid(
                row=i,
                column=1,
                padx=15
            )

            self.entries[label.lower()] = entry

    # =========================================================
    # BUTTONS
    # =========================================================

    def _build_buttons(self):

        frame = tk.Frame(
            self,
            bg="#0F172A"
        )

        frame.pack(
            fill="x",
            padx=20
        )

        buttons = [
            ("➕ Add", "#16A34A", self.add_student),
            ("✏ Update", "#2563EB", self.update_student),
            ("🗑 Delete", "#DC2626", self.delete_student),
            ("🧹 Clear", "#F59E0B", self.clear_form)
        ]

        for text, color, command in buttons:

            tk.Button(
                frame,
                text=text,
                bg=color,
                fg="white",
                width=12,
                font=("Segoe UI", 10, "bold"),
                command=command,
                cursor="hand2"
            ).pack(
                side="left",
                padx=5
            )

        # ---------------- SEARCH ----------------

        tk.Label(
            frame,
            text="Search",
            bg="#0F172A",
            fg="white",
            font=("Segoe UI", 10)
        ).pack(
            side="left",
            padx=(40, 5)
        )

        self.search_var = tk.StringVar()

        search = tk.Entry(
            frame,
            textvariable=self.search_var,
            width=25,
            font=("Segoe UI", 10)
        )

        search.pack(
            side="left"
        )

        search.bind(
            "<KeyRelease>",
            lambda event: self.refresh_table()
        )

    # =========================================================
    # TABLE
    # =========================================================

    def _build_table(self):

        style = ttk.Style()

        style.theme_use("clam")

        columns = (
            "ID",
            "Name",
            "Age",
            "Email",
            "Course",
            "Grade"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:

            self.tree.heading(
                col,
                text=col
            )

            self.tree.column(
                col,
                width=170,
                anchor="center"
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_row_select
        )

    # =========================================================
    # REFRESH TABLE
    # =========================================================

    def refresh_table(self):

        # Clear existing rows

        for row in self.tree.get_children():
            self.tree.delete(row)

        keyword = self.search_var.get().strip()

        # Search or load all students

        if keyword:
            students = self.db.search_students(keyword)
        else:
            students = self.db.get_all_students()

        # Update total count

        self.total_label.config(
            text=f"Total Students : {len(students)}"
        )

        # Insert students into table

        for student in students:

            self.tree.insert(
                "",
                "end",
                values=(
                    student.id,
                    student.name,
                    student.age,
                    student.email,
                    student.course,
                    student.grade
                )
            )

    # =========================================================
    # SELECT STUDENT
    # =========================================================

    def on_row_select(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(
            selected,
            "values"
        )

        if not values:
            return

        # Save selected student ID

        self.selected_id = int(values[0])

        keys = [
            "name",
            "age",
            "email",
            "course",
            "grade"
        ]

        # Fill form fields

        for key, value in zip(keys, values[1:]):

            self.entries[key].delete(
                0,
                tk.END
            )

            self.entries[key].insert(
                0,
                value
            )

    # =========================================================
    # CLEAR FORM
    # =========================================================

    def clear_form(self):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )

        self.selected_id = None

        # Remove table selection

        for item in self.tree.selection():
            self.tree.selection_remove(item)

    # =========================================================
    # ADD STUDENT
    # =========================================================

    def add_student(self):

        try:

            data = validate_student_fields(
                self.entries["name"].get(),
                self.entries["age"].get(),
                self.entries["email"].get(),
                self.entries["course"].get(),
                self.entries["grade"].get()
            )

            self.db.add_student(*data)

            messagebox.showinfo(
                "Success",
                "Student Added Successfully"
            )

            self.clear_form()
            self.refresh_table()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # UPDATE STUDENT
    # =========================================================

    def update_student(self):

        # Check whether a student is selected

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a student to update"
            )

            return

        try:

            # Validate updated data

            data = validate_student_fields(
                self.entries["name"].get(),
                self.entries["age"].get(),
                self.entries["email"].get(),
                self.entries["course"].get(),
                self.entries["grade"].get()
            )

            # Update database

            self.db.update_student(
                self.selected_id,
                *data
            )

            messagebox.showinfo(
                "Success",
                "Student Updated Successfully"
            )

            # Clear and reload table

            self.clear_form()
            self.refresh_table()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a student first"
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )

        if not confirm:
            return

        try:

            self.db.delete_student(
                self.selected_id
            )

            messagebox.showinfo(
                "Success",
                "Student Deleted Successfully"
            )

            self.clear_form()
            self.refresh_table()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


# =============================================================
# OPEN DASHBOARD
# =============================================================

def open_dashboard():

    app = StudentApp()

    app.mainloop()


# =============================================================
# RUN APPLICATION
# =============================================================

if __name__ == "__main__":

    open_dashboard()
