def average(*scores):
    return sum(scores) / len(scores)

my_scores = [400, 450, 300]
print(average(*my_scores))
#  Nếu không truyền gì thì trả về lỗi chia cho 0 nha bro

def make_student(name, **info):
    print(type(info))
    #  dict
    return {"name": name, **info}

print(make_student("Jack", class_="TA1", listening=300))
# Đặt là class_ thay cho class vì class là syntax cho lớp đối tượng rồi bro