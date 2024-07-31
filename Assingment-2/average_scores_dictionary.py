student={"Student A":78, "Student B":96 }
print(student)

avg = sum(student.values()) / len(student)
print(avg)

new_student={}

for i in (student):
    if(student[i]>avg):
        new_student[i]=student[i]

print(new_student)