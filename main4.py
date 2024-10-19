# # Sedang latihan perulangan FOR
# for i in range(1,20):
#     if i == 6 :
#         break
#     print("Sedang Belajar Python")

# Sedangang belajar perulangan while
'''angka = 1
while angka <= 20:
    print(angka)
    angka += 1'''

# # Percadangan if else
# nilai = 60
# if nilai >= 75:
#     print("Anda lulus ujian.")
# else :
#     print("Anda belum lulus ujian.")


# nilai = 75
# if nilai >= 75:
#     print("Anda lulus ujian.")
# else:
#     print("Anda belum lulus ujian.")

nilai = [77]
for i in nilai:
    if i >= 80:
        status = "Baik Sekali"
    elif i >= 75:
        status = "Baik"
    elif i >= 56:
        status = "Cukup"
    elif i >= 45:
        status = "Kurang"
    elif i:
        status = "Tidak lulus" 

    print(f"Nilai:{i}, status: {status}")

