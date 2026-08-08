import sqlite3
import hashlib


def create_user_table():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def create_admin():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (
                "admin",
                hash_password("admin123")
            )
        )

        conn.commit()

    except:
        pass

    conn.close()



def login_user(username,password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (
            username,
            hash_password(password)
        )
    )

    user = cursor.fetchone()

    conn.close()


    if user:
        return True
    else:
        return False