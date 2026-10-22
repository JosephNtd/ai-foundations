from collections import Counter, defaultdict
import sys
students = [
    {"name": "Jack", "class": "TA3", "listening": 400, "reading": 450},
    {"name": "Fun", "class": "TA3", "listening": 250, "reading": 280},
    {"name": "Clown", "class": "TA2", "listening": 330, "reading": 460},
    {"name": "King", "class": "TA2", "listening": 200, "reading": 250},
    {"name": "Queen", "class": "TA1", "listening": 350, "reading": 480},
    {"name": "Justice", "class": "TA2", "listening": 400, "reading": 460}
]
total_score = lambda x: x["listening"] + x["reading"]
gen = (st["name"] for st in students if total_score(st) >= 700)
print(list(gen))
print(list(gen))


# Câu 1a: Lấy 3 học viên đầu
first_3_students = students[:3]
print(*first_3_students, sep="\n")

# Câu 1b: Lấy 3 học viên cuối 
last_3_students = students[-3:]
print(*last_3_students, sep="\n")

# Câu 1c: Lấy học viên ở vị trí chẵn
even_students = students[::2]
print(*even_students, sep="\n")

# Câu 1d: Tách được học viên đầu, nhóm ở giữa và học viên cuối chỉ bằng một dòng
first, *middle, last = students

print(first)
print(*middle, sep="\n")
print(last)

# Câu 1e: Đổi chỗ 2 biến mà không cần biến tạm.
a = 10
b = 20
a, b = b, a
print(a, b)
# # Câu 2a: Sắp xếp học viên theo tổng điểm giảm dần
descending_score = sorted(students, key=lambda x: -(total_score(x)))
print(*descending_score, sep="\n")

# Câu 2a: Sắp xếp học viên theo lớp và tổng điểm giảm dần
descending_class_and_score = sorted(students, key= lambda x: (x["class"], -(total_score(x))))
print(*descending_class_and_score, sep="\n")

# Câu 3a: Lấy danh sách tên học viên có tổng điểm ≥ 600
total_score_above_600 = [st["name"] for st in students if (total_score(st)) >= 600]
print(*total_score_above_600, sep="\n")

# Câu 3b: Tạo dict {tên: tổng}.
dict_name_total = {st["name"]: total_score(st) for st in students}
print(dict_name_total)

# Câu 3c: Tạo tập hợp các lớp. (dùng set để chỉ lấy 1 phần tử không trùng lặp trong list thôi)
class_set = {st["class"] for st in students}
print(class_set)

# Câu 4a: Đếm số học viên mỗi lớp.
counts_4a = Counter(st["class"] for st in students)
print(counts_4a)

# Câu 4b: Tìm lớp đông nhất
most_student = counts_4a.most_common(1)
print(most_student)

# Câu 5: Gom tên học viên theo lớp, ra dạng {lớp: [tên, ...]}
classes = defaultdict(list)

for st in students:
    classes[st["class"]].append(st["name"])

print(dict(classes))

# Câu 6: Xếp học viên vào band điểm (ví dụ 500, 600, 700…), rồi đếm số học viên theo cặp (lớp, band).
counts_6 = Counter((st["class"], total_score(st) // 100 * 100) for st in students)
print(counts_6)

# Câu 7: Viết một hàm generator lần lượt trả ra học viên có tổng điểm ≥ ngưỡng.
def st_exceed_the_threshold(list_students, threshold):
    for student in list_students:
        if total_score(student) >= threshold:
            yield student

cau_7 = list(st_exceed_the_threshold(students, 700))
print(*cau_7, sep="\n")

print(sys.getsizeof([i for i in range(1_000_000)]))
print(sys.getsizeof((i for i in range(1_000_000))))