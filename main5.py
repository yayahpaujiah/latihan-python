# #Belajar Fungsi

# #mengisi nilai parameter
# def sapa(nama,):
#     print("Halo,", nama, "!")
# # Format string tanpa jarak spasi
#     print(f"Halo, {nama}!")
# #Menampilkan hasil fungsi

# #mengisi nilai fungsi dengan tipe data string yaitu yayah
# sapa("Yayah")
# # Output: Halo, Yayah!

# def tambah (a, b, c):
#     hasil = (a + b) / c
#     return hasil

# jumlah = tambah(3, 5, 2)
# print("Hasilnya adalah:", jumlah) 
# # Output: 8:4=2

# # Membuat list
# buah = ["apel", "pisang", "mangga"]

# # Mengakses elemen
# print(buah[0]) # Output: apel

# # Mengubah elemen
# buah[1] = "jeruk"
# print(buah) 

buah = ["apel", "pisang", "mangga"]

# Menambah dua buah
buah += ["manggis","anggur"]

# Menghapus "mangga"
buah.remove("mangga")

print(buah) # Output: ['apel','jeruk','manggis','anggur']

# daftar nama buah
buah = ["apel", "pisang", "mangga"]

# mengakses elemen pada buah pada daftar list
buah[1] = "jeruk"

# menambah list baru dengan index tertentu
buah.insert(0,"anggur")

# menambah buah
buah.append("Manggis")

# menghapus buah
buah.remove("mangga")
print(buah)

# Struktur Data Tuple
angka1 = (1,2,3)
angka2 = (4,5,6)
angka3 = (angka1 + angka2)


print(angka3)