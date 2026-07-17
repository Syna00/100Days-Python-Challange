print("Welcome to Python Seblak Deliveries!")
size = input("Ukurannya mau yang seberapa? ada ukuran S, M sama L : ")
sayur = input("Pake sayur ga? Y or N: ")
ekstra_keju = input("Mau ekstra keju gak? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 10000
elif size == "M":
    bill += 20000
elif size == "L":
    bill +=25000
else:
    print("Anda salah memasukkan ukuran") 

# todo: work out to how much to add to their bill based on their sayur choice.
if sayur == "Y":
    if size == "S":
        bill += 2000
    elif size == "M":
        bill += 3000
    elif size == "L":
        bill += 5000

# todo: work out to final amount based on wheter if they want extra cheese.
if ekstra_keju == "Y":
    bill += 5000

print (f"Harga yang harus kamu bayar adalah : {bill:,}".replace(",","."))