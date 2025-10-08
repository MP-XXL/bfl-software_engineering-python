"""
TASK: Create a StudentGradeManager class.

Requirements:
1. Store students and their grades (student → list of grades).
2. Add student with empty grade list.
3. Add grade for specific student (0-100 range).
4. Calculate average grade for a student.
5. Get student with highest average.
6. Add validation for grades (0-100 range).

Example Usage:
    manager = StudentGradeManager()
    manager.add_student("Alice")
    manager.add_grade("Alice", 85)
    manager.add_grade("Alice", 92)
    print(manager.get_average("Alice"))  # 88.5
"""

# Custom Errors - IMPLEMENT THESE
class StudentExistsAlreadyError(Exception):
    pass

class StudentDoesNotExistsError(Exception):
    pass

class NameMustBeStringError(Exception):
    pass

class InvalidScoreError(Exception):
    pass

class ScoreOutOfRangeError(Exception):
    pass

class StudentGradeManager:
    def __init__(self):
        # TODO: Initialize your data structure here
        pass
    
    def add_student(self, name: str) -> bool:
        """
        Add a new student with empty grade list.
        Returns True if successful, raises appropriate errors otherwise.
        """
        # TODO: Implement this method
        pass
    
    def add_grade(self, name: str, score: float) -> bool:
        """
        Add grade for a student.
        Returns True if successful, raises appropriate errors otherwise.
        """
        # TODO: Implement this method
        pass
    
    def get_average(self, name: str) -> float:
        """
        Calculate average grade for a student.
        Returns average or 0.0 if no grades exist.
        Raises appropriate errors if student not found.
        """
        # TODO: Implement this method
        pass
    
    def get_student_with_highest_average(self) -> str:
        """
        Find student with highest average grade.
        Returns student name or None if no students have grades.
        """
        # TODO: Implement this method
        pass
    
    def get_all_grades(self, name: str) -> list:
        """
        Get all grades for a student.
        Returns list of grades or empty list if student not found.
        """
        # TODO: Implement this method
        pass
    
    def get_all_students(self) -> list:
        """
        Get all student names.
        Returns list of student names.
        """
        # TODO: Implement this method
        pass
