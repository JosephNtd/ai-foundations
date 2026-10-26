from collections.abc import Iterator

def average(*scores: int) -> float:
    return sum(scores) / len(scores)

my_scores = [400, 450, 300]
print(average(*my_scores))
# print(average("4500", "300"))

#  Nếu không truyền gì thì trả về lỗi chia cho 0 nha bro

#  có thể dùng Any
def make_student(name: str, **info: str | int) -> dict[str, str | int]:
    print(type(info))
    #  dict
    return {"name": name, **info}

print(make_student("Jack", class_="TA1", listening=300))
# Đặt là class_ thay cho class vì class là syntax cho lớp đối tượng rồi bro

def high_scorers(students: list[dict], threshold: int) -> Iterator[str]:
    for student in students:
        if student["score"] >= threshold:
            yield student["name"]

student_list = [
    {"name": "Jake A", "score": 400},
    {"name": "Flute B", "score": 240},
    {"name": "Bang C", "score": 350}
]

for student in high_scorers(student_list, 300):
    print(student)
