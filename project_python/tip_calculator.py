print("Selamat datang di Tip Calculator!")
harga = float(input("Masukkan harga makanan: Rp. "))
persentase_tip = int(input("Masukkan persentase tip "))
jumlah_orang = int(input("Masukkan jumlah orang: "))
persenan_tip = persentase_tip / 100
total_tip = harga + harga * persenan_tip
tip_per_orang = total_tip / jumlah_orang
tip_final = round(tip_per_orang, 2)
print(f"Setiap orang harus membayar: Rp. {tip_final}")
