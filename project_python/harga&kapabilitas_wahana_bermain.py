print("Selamat datang di wahana bermain kami!")
tinggi_badan = int(input("Tinggi badan kamu berapa? "))

#if berfungsi untuk mengecek apakah tinggi badan memenuhi syarat atau tidak
if tinggi_badan >= 150:
    print("Selamat datang di wahana air, Kamu bisa naik wahana ini!")
    print("Kita akan cek umur anda untuk masing-masing harga tiketnya")
    umur = int(input("Berapa umur kamu?"))
    if umur <= 12:
        print("Harga tiketnya 30.000")
    elif umur <= 18:
        print ("Harga tiket kamu 40.000")
    elif umur <= 20:
        print("Harga tiket kamu 50.000")
    else:
        print("Harga tiket kamu 60.000")
    print("Mohon konfirmasi pembayaran")
    

#else berfungsi untuk mengeksekusi perintah jika kondisi if tidak terpenuhi
else:
    print("Maaf, kamu tidak bisa naik wahana ini karena tinggi badanmu kurang dari 150 cm.")
    print("Terima kasih telah mengunjungi wahana ini!")


#Penggunaan :
# < dipakai untuk kurang dari, > dipakai untuk lebih dari, <= dipakai untuk kurang dari sama dengan, >= dipakai untuk lebih dari sama dengan, == dipakai untuk sama dengan, != dipakai untuk tidak sama dengan
#if digunakan kalau ketika input datanya benar
#elif digunakan untuk sebuah variabel yang ada jaraknya, misal (umur 18-20)
#else digunakan ketika datanya tidak masuk ke dalam if (salah)