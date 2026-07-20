#misal
masukkan = input("Seberapa besar cintamu pada crush mu? besar? atau engga? \n").lower()
def takaran():
    if masukkan == "engga":
        print("Kamu dalam batas wajar")
    elif masukkan == "besar":
        print("Hati-hati kamu bisa sakit hati")
    else:
        print("Kamu cuma bisa input besar atau engga")
takaran()