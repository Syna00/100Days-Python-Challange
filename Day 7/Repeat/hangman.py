import random
babak = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''', '''
 +---+
 |   |
     |
     |
     |
     |
=========
''']
nyawa = 6

list_kata = ["harimau", "gajah", "kudanil"]

pilihan_kata = random.choice(list_kata)

tempat = ""
tempat_kata = len(pilihan_kata)
for posisi in range(tempat_kata):
    tempat += ("_")
print(tempat)

game_selesai = False
kata_benar = []
while not game_selesai:
    tebakan = input("Masukkan 1 huruf : ").lower()

    tampilan = ""
    for huruf in pilihan_kata:
        if huruf == tebakan:
            tampilan += huruf
            kata_benar.append(tebakan)
        elif huruf in kata_benar:
            tampilan += huruf
        else:
            tampilan += "_"
    print(tampilan)

    if tebakan not in pilihan_kata:
        nyawa -= 1
        if nyawa == 0:
            game_selesai = True 
            print("Kamu Kalah!")
    if "_" not in tampilan:
        game_selesai = True
        print("Kamu Menang!")

    print(babak[nyawa])