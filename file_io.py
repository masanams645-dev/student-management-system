"""
file_io.py
----------
CSV / JSON export and import support for the Student Management System.
"""

import csv
import json
from typing import List, Tuple
from models import Student
from validators import validate_student_fields

FIELDNAMES = ["id", "name", "age", "email", "course", "grade"]


# ---------- EXPORT ----------
def export_to_csv(students: List[Student], filepath: str):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())


def export_to_json(students: List[Student], filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, indent=2)


# ---------- IMPORT ----------
def import_from_csv(filepath: str, db) -> Tuple[int, List[str]]:
    """Import students from a CSV file into the given Database instance.
    Returns (num_imported, list_of_error_messages)."""
    added, errors = 0, []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # row 1 is header
            try:
                name, age, email, course, grade = validate_student_fields(
                    row.get("name"), row.get("age"), row.get("email"),
                    row.get("course"), row.get("grade", "N/A")
                )
                db.add_student(name, age, email, course, grade)
                added += 1
            except ValueError as e:
                errors.append(f"Row {i}: {e}")
    return added, errors


def import_from_json(filepath: str, db) -> Tuple[int, List[str]]:
    added, errors = 0, []
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    for i, row in enumerate(data, start=1):
        try:
            name, age, email, course, grade = validate_student_fields(
                row.get("name"), row.get("age"), row.get("email"),
                row.get("course"), row.get("grade", "N/A")
            )
            db.add_student(name, age, email, course, grade)
            added += 1
        except ValueError as e:
            errors.append(f"Record {i}: {e}")
    return added, errors