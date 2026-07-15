#--data_type--

#1).Subscripting
print("hello"[0])
# menentukan peletakan angka, nomor di dalam [] akan menjadi index(posisi), index dimulai dari 0

#2).String
print("123" + "456")
# penjumlahan string akan menggabungkan kedua string menjadi satu

#3).Integer=whole number
print(123 + 456)
# penjumlahan integer akan menghasilkan penjumlahan matematika biasa

#4).Float=decimal number
print(1.23 + 4.56)
# penjumlahan float akan menghasilkan penjumlahan matematika biasa

#5).Larger integer
print(123_112_312_323)
# penulisan angka besar dapat menggunakan underscore (_) untuk memisahkan digit agar lebih mudah dibaca

#6).floating = floating point number
print(3.14159)
# penulisan angka desimal dapat menggunakan titik (.) untuk memisahkan bagian integer dan bagian desimal

#7).Boolean
print(True)
print(False)
# boolean adalah tipe data yang hanya memiliki dua nilai, yaitu True (benar) dan False (salah).



#--Type error, type checking, type conversion--
name_of_the_user = input("What is your name? ")
lenght_of_name = len(name_of_the_user)

print(type(name_of_the_user)) #str
print(type(lenght_of_name)) #int

print("number of letters in your name is: " + str(lenght_of_name))
#di dalam print ini, kita tidak boleh menggabungkan string dengan integer, maka kita harus mengubah integer menjadi string menggunakan str() agar bisa digabungkan dengan string.