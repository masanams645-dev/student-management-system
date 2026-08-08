# 🎓 Student Management System

A desktop-based **Student Management System** developed using **Python and Tkinter**. The application provides a simple and user-friendly interface to manage student records with administrator login, validation, search, and CRUD operations.

## 🚀 Features

* 🔐 **Admin Login**
* ➕ Add new students
* ✏️ Update student details
* 🗑️ Delete student records
* 🔍 Search students
* 📋 View all student records
* 👥 Display total number of students
* ✅ Input validation
* 🔒 Password hashing using SHA-256
* 🖥️ User-friendly Tkinter GUI
* 💾 SQLite database integration
* 📊 Structured student data management
* ⚡ Real-time table refresh after operations

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **SQLite** – Database management
* **Dataclasses** – Student data model
* **Hashlib** – Password hashing
* **Regular Expressions** – Input validation

## 📁 Project Structure

```text
Student-Management-System/
│
├── main.py
├── auth.py
├── gui.py
├── db.py
├── models.py
├── validators.py
├── users.db
└── README.md
```

## 📌 File Description

| File            | Description                                      |
| --------------- | ------------------------------------------------ |
| `main.py`       | Handles the administrator login interface        |
| `auth.py`       | Manages user authentication and password hashing |
| `gui.py`        | Provides the main Student Management dashboard   |
| `db.py`         | Handles SQLite database operations               |
| `models.py`     | Defines the Student data model                   |
| `validators.py` | Validates student input fields                   |
| `users.db`      | Stores administrator authentication data         |

## 🔄 Application Workflow

```text
             ┌───────────────┐
             │    main.py    │
             │  Admin Login  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    auth.py    │
             │ Authentication│
             └───────┬───────┘
                     │
              Login Successful
                     │
                     ▼
             ┌───────────────┐
             │    gui.py     │
             │   Dashboard   │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │     db.py     │
             │ CRUD Operations│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    SQLite     │
             │   Database    │
             └───────────────┘
```

## 🔐 Authentication

The system includes an administrator login system.

Default credentials:

```text
Username: admin
Password: admin123
```

> ⚠️ These credentials are for development/demo purposes only. Change them before using the application in a real environment.

Passwords are hashed using Python's `hashlib` before being stored.

## 📋 Student Information

The application manages the following student details:

* Student ID
* Name
* Age
* Email
* Course
* Grade

## ✅ Input Validation

The application validates:

* Name format
* Age range
* Email format
* Course name
* Grade value
* Empty fields

Invalid input generates a clear error message for the user.

## 💻 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

No external database package is required because the project uses Python's built-in SQLite support.

## 🎯 CRUD Operations

The system supports the four basic database operations:

```text
Create  → Add Student
Read    → View/Search Students
Update  → Edit Student
Delete  → Remove Student
```

## 🌟 Project Highlights

This project demonstrates practical knowledge of:

* Python programming
* Object-oriented programming
* GUI development
* Database management
* CRUD operations
* Authentication
* Password hashing
* Input validation
* Modular project structure
* Exception handling

## 📈 Future Enhancements

Possible future improvements:

* 📊 Student performance analytics
* 📑 Export student records to CSV/PDF
* 👨‍🎓 Student profile pages
* 📧 Email notifications
* 🌐 REST API integration
* 🗄️ MongoDB integration
* 👥 Multiple user roles
* 🌙 Dark/Light mode
* 📱 Responsive web version

## 👨‍💻 Author

**Masanam**

Computer Science Engineering Student

---

⭐ If you find this project useful, consider giving the repository a star!
