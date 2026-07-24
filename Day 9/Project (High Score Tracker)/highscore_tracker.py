from art import logo
print(logo)


def cari_score_tertinggi(score_dictionary):
    pemenang = ""
    score_tertinggi = 0

    for pemain in score_dictionary:
        score = score_dictionary[pemain]
        if score > score_tertinggi:
            score_tertinggi = score
            pemenang = pemain
    print(f"Jadi pemenangnya adalah {pemenang} dengan skor {score_tertinggi}")
    
penyimpan_nama = {}
lanjut = True
while lanjut :
    name = input("Siapa nama kamu? ")
    score = int(input("Masukkan skor kamu : "))
    penyimpan_nama[name] = score
    lanjut_gak = input("Apakah masih ada yang mau input? ketika 'ya' atau 'tidak' : ").lower()
    if lanjut_gak == "ya":
        lanjut = True
        print("\n" * 10)
    elif lanjut_gak == "tidak":
        lanjut = False
        cari_score_tertinggi(penyimpan_nama)