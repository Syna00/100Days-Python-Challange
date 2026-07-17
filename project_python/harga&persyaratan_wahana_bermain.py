print("Selamat datang di wahana bermain kami!")
tinggi_badan = int(input("Tinggi badan kamu berapa? "))

#if berfungsi untuk mengecek apakah tinggi badan memenuhi syarat atau tidak
if tinggi_badan >= 150:
    print("Selamat datang di wahana air, Kamu bisa naik wahana ini!")
    print("Kita akan cek umur anda untuk masing-masing harga tiketnya")
    umur = int(input("Berapa umur kamu?"))
    if umur <= 12:
        bill = 30000
        print("Harga tiketnya 30.000")
    elif umur <= 18:
        bill = 40000
        print ("Harga tiket kamu 40.000")
    elif umur <= 20:
        bill = 50000
        print("Harga tiket kamu 50.000")
    elif umur >=21 and umur<=50:
    #bisa disederhanakan menjadi 21 <= age <=55:
        print("Kamu aman untuk naik wahana ini")
        bill = 60000
        print("Harga tiket kamu 60.000")
    wants_photo = (input("Apakah kamu mau difoto ketika naik wahana ini? ketik y untuk ya atau ketik n untuk tidak : "))
    if wants_photo == "y":
        #menambahkan 10.000 untuk biaya mereka
        bill += 10000 
    elif wants_photo == "n":
        print("Baik, kamu tidak akan kami foto ketika naik wahana ini")
    else:
        print("kamu memasukkan input yang salah")
    
    print(f"Biaya yang harus kamu bayar adalah {bill:,}".replace(",",".") )
    print("Mohon konfirmasi pembayaran")

#else berfungsi untuk mengeksekusi perintah jika kondisi if tidak terpenuhi
else:
    print("Maaf, kamu tidak bisa naik wahana ini karena tinggi badanmu kurang dari 150 cm.")
    print("Terima kasih telah mengunjungi wahana ini!")


#Pembelajaran dan keterangan :
# < dipakai untuk kurang dari, > dipakai untuk lebih dari, <= dipakai untuk kurang dari sama dengan, >= dipakai untuk lebih dari sama dengan, == dipakai untuk sama dengan, != dipakai untuk tidak sama dengan
#if digunakan kalau ketika input datanya benar
#elif digunakan untuk sebuah variabel yang ada jaraknya, misal (umur 18-20)
#else digunakan ketika datanya tidak masuk ke dalam if (salah)
