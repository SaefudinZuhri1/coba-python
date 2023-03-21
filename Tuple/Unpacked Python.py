# Upnacked Tuple
## A. Membongkar Tuple
# Saat membuat tuple, biasanya diberikan nilai. Disebut dengan "mengemas" tuple
buah = ("Mangga", "Manggis", "Sirsak")
print(buah)

# Namun, pada Python, diperbolehkan mengekstrak nilai kembali ke dalam variabel. Disebut dengan "Membongkar"
buah1 = ("Jeruk", "Melon", "Semangka")
(kuning, hijau, merah) = buah1
print(kuning)
print(hijau)
print(merah)
# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam tuple, jika tidak, maka harus menggunakan tanda bintang untuk mengumpulkan nilai yang tersisa sebagai list.

# B. Menggunakan Asterisk *
# Jika jumlah variabel kurang dari jumlah nilai, bisa menggunakan *namaVariabel dan nilai akan diberikan ke variabel sebagai list.
# Contoh:
buah2 = ("Jeruk", "Manggis", "Mangga", "Jambu")
(ungu, biru, *putih) = buah2
print(ungu)
print(biru)
print(putih)

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir, Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa sesuai dengan jumlah variabel yang tersisa
# Contoh:
kota = ("Jakarta", "Bogor", "Tangerang", "Depok", "Bekasi")
(jakarta, *tangerang, bekasi) = kota
print(jakarta)
print(tangerang)
print(bekasi)
