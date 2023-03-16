# Mengurutkan daftar berdasarkan huruf
# Menggunakan metode sort()
listBuah = ["Jeruk", "Apel", "Mangga", "Nanas"]
listBuah.sort()
print(listBuah)

# Mengurutkan daftar lewat angka
listAngka = [60, 50, 10, 20, 1000]
listAngka.sort()
print(listAngka)

# Mengurutkan daftar secara menurun
# Menggunakan argumen reverse = True
namaKota = ["Jakarta", "Bekasi", "Tangerang", "Bogor", "Tangerang Selatan"]
namaKota.sort(reverse = True)
print(namaKota)

# Mengurutkan angka secara menurun
urutAngka = [200, 100, 67, 83, 10]
urutAngka.sort(reverse = True)
print(urutAngka)


# Menyesuaikan Fungsi Sortir
# Menggunakan argumen keyword key = function

def iniAngka(n):
	return abs(n - 40)

angkaBaru = [200, 20, 80, 55, 38, 44]
angkaBaru.sort(key = iniAngka)
print(iniAngka)

# Penjelasan: fungsi akan mengembalikan nomor yang akan digunkan untuk mengurutkan daftar (nomor terendah lebih dahulu)

# Mengurutkan tidak peka huruf besar  
buahBuahan = ["pisang", "Mangga", "jeruk nipis", "Apel"]
buahBuahan.sort()
print(buahBuahan)

# Penjelasan: secara default, metode sort() peka huruf besar-kecil, sehingga semua huruf kapital diurutkan sebelum huruf kecil











