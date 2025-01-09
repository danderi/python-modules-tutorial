# This file contains our data structures
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    """Student data structure"""
    id: int
    name: str
    courses: List[str]

    def __post_init__(self):
        if self.courses is None:
            self.courses = []

@dataclass
class Course:
    """Course data structure"""
    code: str
    name: str
    students: List[int]

    def __post_init__(self):
        if self.students is None:
            self.students = []