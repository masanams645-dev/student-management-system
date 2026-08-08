
"""
db.py
-----
Handles all SQLite persistence for the Student Management System.

The Database class handles:
- Database creation
- Add student
- Read students
- Search students
- Update student
- Delete student
- Count students
"""

import sqlite3
from typing import List, Optional

from models import Student


DB_FILE = "students.db"


class Database:

    def __init__(self, db_path: str = DB_FILE):

        self.db_path = db_path

        self._init_db()

    # =========================================================
    # DATABASE CONNECTION
    # =========================================================

    def _connect(self):

        conn = sqlite3.connect(self.db_path)

        conn.execute(
            "PRAGMA foreign_keys = ON"
        )

        return conn

    # =========================================================
    # INITIALIZE DATABASE
    # =========================================================

    def _init_db(self):

        with self._connect() as conn:

            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    course TEXT NOT NULL,
                    grade TEXT DEFAULT 'N/A'
                )
                """
            )

            conn.commit()

    # =========================================================
    # CREATE - ADD STUDENT
    # =========================================================

    def add_student(
        self,
        name: str,
        age: int,
        email: str,
        course: str,
        grade: str = "N/A"
    ) -> int:

        try:

            with self._connect() as conn:

                cursor = conn.execute(
                    """
                    INSERT INTO students
                    (name, age, email, course, grade)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        name,
                        age,
                        email,
                        course,
                        grade
                    )
                )

                conn.commit()

                return cursor.lastrowid

        except sqlite3.IntegrityError:

            raise ValueError(
                f"A student with email '{email}' already exists."
            )

    # =========================================================
    # READ - GET ALL STUDENTS
    # =========================================================

    def get_all_students(self) -> List[Student]:

        with self._connect() as conn:

            rows = conn.execute(
                """
                SELECT *
                FROM students
                ORDER BY id
                """
            ).fetchall()

        return [
            Student.from_row(row)
            for row in rows
        ]

    # =========================================================
    # READ - GET STUDENT BY ID
    # =========================================================

    def get_student_by_id(
        self,
        student_id: int
    ) -> Optional[Student]:

        with self._connect() as conn:

            row = conn.execute(
                """
                SELECT *
                FROM students
                WHERE id = ?
                """,
                (student_id,)
            ).fetchone()

        if row:

            return Student.from_row(row)

        return None

    # =========================================================
    # SEARCH STUDENTS
    # =========================================================

    def search_students(
        self,
        keyword: str
    ) -> List[Student]:

        like = f"%{keyword}%"

        with self._connect() as conn:

            rows = conn.execute(
                """
                SELECT *
                FROM students
                WHERE name LIKE ?
                   OR email LIKE ?
                   OR course LIKE ?
                   OR CAST(id AS TEXT) = ?
                ORDER BY id
                """,
                (
                    like,
                    like,
                    like,
                    keyword
                )
            ).fetchall()

        return [
            Student.from_row(row)
            for row in rows
        ]

    # =========================================================
    # UPDATE STUDENT
    # =========================================================

    def update_student(
        self,
        student_id: int,
        name: str,
        age: int,
        email: str,
        course: str,
        grade: str
    ) -> bool:

        try:

            with self._connect() as conn:

                cursor = conn.execute(
                    """
                    UPDATE students
                    SET
                        name = ?,
                        age = ?,
                        email = ?,
                        course = ?,
                        grade = ?
                    WHERE id = ?
                    """,
                    (
                        name,
                        age,
                        email,
                        course,
                        grade,
                        student_id
                    )
                )

                conn.commit()

                return cursor.rowcount > 0

        except sqlite3.IntegrityError:

            raise ValueError(
                f"A student with email '{email}' already exists."
            )

    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(
        self,
        student_id: int
    ) -> bool:

        with self._connect() as conn:

            cursor = conn.execute(
                """
                DELETE FROM students
                WHERE id = ?
                """,
                (student_id,)
            )

            conn.commit()

            return cursor.rowcount > 0

    # =========================================================
    # DELETE ALL STUDENTS
    # =========================================================

    def delete_all(self):

        with self._connect() as conn:

            conn.execute(
                "DELETE FROM students"
            )

            conn.commit()

    # =========================================================
    # COUNT STUDENTS
    # =========================================================

    def count(self) -> int:

        with self._connect() as conn:

            result = conn.execute(
                "SELECT COUNT(*) FROM students"
            ).fetchone()

            return result[0]

