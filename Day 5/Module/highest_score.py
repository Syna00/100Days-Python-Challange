students_scores = [80, 70, 79, 60, 90, 40, 55]
total = sum(students_scores)
print(total)

sum = 0
for score in students_scores:
    sum += score
print(sum)

#Menentukan angka terbesar 
#Option 1
print(max(students_scores)) 
#Option 2
max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score
    print(max_score)

