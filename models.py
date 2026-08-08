"""
models.py
---------
Defines the Student data model used across the Student Management System.
"""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Student:
    """Represents a single student record."""
    id: Optional[int]
    name: str
    age: int
    email: str
    course: str
    grade: str = "N/A"

    def to_dict(self) -> dict:
        """Convert the student record to a plain dictionary."""
        return asdict(self)

    @staticmethod
    def from_row(row) -> "Student":
        """Build a Student instance from a SQLite row (or tuple)."""
        return Student(
            id=row[0],
            name=row[1],
            age=row[2],
            email=row[3],
            course=row[4],
            grade=row[5],
        )

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.name} | Age: {self.age} | "
            f"Email: {self.email} | Course: {self.course} | Grade: {self.grade}"
        )