import random 

# random_integer = random.randint(1, 2) || #Fungsinya untuk memilih random 2 angka
# print(random_integer)

# random_number_0_to_1 = random.random() || #Fungsinya untuk memilih random 0-1, tapi kalau menggunakan (*X) setelah () akan menghasilkan 1-X
# print(random_number_0_to_1)

# random_float = random.uniform(1,10) || #Fungsinya untuk memilih random 1-X dalam bentuk float
# print(random_float)

    #gimana kalau membuat random dalam bentuk kata?
random_heads_or_tails = random.randint(1, 2)
if random_heads_or_tails == 1:
    print("HeadS")
else:
    print("Tails")