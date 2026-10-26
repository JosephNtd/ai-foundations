from dataclasses import dataclass
from collections.abc import Iterator

@dataclass(frozen=True)
class Student:
    name: str
    class_name: str
    listening: int
    reading: int

    def total(self) -> int:
        return self.listening + self.reading

student_list = [
    Student("Jake A", "Class A", 400, 300),
    Student("Flute B", "Class B", 200, 300),
    Student("Bang C", "Class C", 999, 450),
]

def high_scorers(students: list[Student], threshold: int) -> Iterator[str]:
    for st in students:
        if st.total() >= threshold:
            yield st.name

for student in high_scorers(student_list, 600):
    print(student)