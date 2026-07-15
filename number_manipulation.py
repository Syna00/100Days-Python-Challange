height = 1.65 
weight = 84

bmi = weight / (height ** 2)

print(bmi)
print(round(bmi)) #untuk membulatkan angka
print(round(bmi, 2)) #ada parameter kedua untuk menentukan jumlah angka di belakang koma

score = 0

#user scores a point
score += 1
print(score)

#f-strings
print("Your score is: " + str(score))


#f-stings2
score = 0
height = 1.8
is_winning = True

print(f"Your score is: {score}, your height is: {height}, you are winning is: {is_winning}")
#mempersingkat penulisan string dengan menambahkan f di depan tanda kutip dan menambahkan variabel di dalam kurung kurawal {}