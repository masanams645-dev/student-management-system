"""
validators.py
-------------
Input validation utilities for the Student Management System.
Each function raises a ValueError with a clear message on invalid input,
so callers (CLI, GUI, or file-import routines) can catch and report them
consistently.
"""

import re

EMAIL_REGEX = re.compile(r"^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$")


def validate_name(name: str) -> str:
    name = (name or "").strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    if len(name) > 100:
        raise ValueError("Name is too long (max 100 characters).")
    if not re.match(r"^[A-Za-z\s\.\-']+$", name):
        raise ValueError("Name may only contain letters, spaces, hyphens, and apostrophes.")
    return name


def validate_age(age) -> int:
    try:
        age_int = int(age)
    except (TypeError, ValueError):
        raise ValueError("Age must be a whole number.")
    if not (5 <= age_int <= 100):
        raise ValueError("Age must be between 5 and 100.")
    return age_int


def validate_email(email: str) -> str:
    email = (email or "").strip()
    if not email:
        raise ValueError("Email cannot be empty.")
    if not EMAIL_REGEX.match(email):
        raise ValueError("Email format is invalid.")
    return email


def validate_course(course: str) -> str:
    course = (course or "").strip()
    if not course:
        raise ValueError("Course cannot be empty.")
    if len(course) > 100:
        raise ValueError("Course name is too long (max 100 characters).")
    return course


def validate_grade(grade: str) -> str:
    grade = (grade or "N/A").strip()
    if not grade:
        grade = "N/A"
    if len(grade) > 10:
        raise ValueError("Grade value is too long (max 10 characters).")
    return grade


def validate_student_fields(name, age, email, course, grade="N/A"):
    """Validate all fields at once; returns a tuple of cleaned values."""
    return (
        validate_name(name),
        validate_age(age),
        validate_email(email),
        validate_course(course),
        validate_grade(grade),
    )