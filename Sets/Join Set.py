# Join Sets

# A. Menggabungkan Dua Set
# Beberapa cara yang digunakan untuk menggabungkan dua set atau lebih dengan Python
# Bisa menggunakan method union() yang mengembalikan set baru yang berisi semua item dari kedua set, atau update() method yang menyisipkan semua item dari satu set ke set lainnya:
# Contoh: union() method akan menghasilkan set baru dengan semua item dari kedua set
iniSet1 = {"q", "w", "e", "r", "t", "y"}
iniSet2 = {0, 1, 2, 3, 4}

gabunganSet = iniSet1.union(iniSet2)
print(gabunganSet)

# Contoh: Method update() menyisipkan item di kedua set
iniHuruf = {"x", "y", "z"}
iniAngka = {4, 5, 6}
iniHuruf.update(iniAngka)
print(iniHuruf)

# Catatan: Keduanya, union() dan update() akan mengecualikan item duplikat apapun

# B. Menyimpan Duplikat Item
# Menggunakan method intersection_update() hanya akan menyimpan item yang ada di kedua set.
# Contoh: Pertahankan item yang ada di kedua set.
perusahaan = {"Google", "Microsoft", "Louis Vitton"}
produk = {"Google", "Windows", "Pakaian"}

perusahaan.intersection_update(produk)
print(perusahaan)

# Metode intersection() ini akan mengembalikan set baru, yang hanya berisi item yang ada di kedua set.
# Contoh: Menghasilkan nilai set yang berisi item di kedua set.
olshop = {"Shopee", "Lazada", "Tokopedia"}
produk = {"Shopeefood", "LazMall", "Tokopedia"}
produkOlshop = olshop.intersection(produk)
print(produkOlshop)

# C. Simpan semua tapi bukan duplikatnya
# Metode symmetric_difference_update() hanya menyimpan elemen yang tidak ada di kedua set
# Contoh: Simpan item yang tidak ada di kedua set
mediaSosial = {"Facebook", "Instagram", "TikTok"}
produkMedsos = {"Fanpage", "Reels", "TikTok"}

mediaSosial.symmetric_difference_update(produkMedsos)
print(mediaSosial)

# Method symetric_difference() menghasilkan set baru, yang hanya berisi elemen yang tidak ada di kedua set
# Contoh: Mengembalikan set yang berisi semua item dari kedua set, kecuali semua item yang ada di keduanya
produkA = {"Kartu", "Mainan", "Makanan"}
produkB = {"Pakaian", "Hiasan", "Kartu"}

tidakAdaProduk = produkA.symmetric_difference(produkB)
print(tidakAdaProduk)

# Catatan: Nilai True dan 1 dianggap sebagai nilai yang sama dalam kumpulan, dan diperlakukan sebagai duplikat.
# Contoh: True dan 1 dianggap nilai yang sama
produkLagi = {"Gula", "Sendok", "Teh", True}
produkLagi1 = {"Air", 1, "Manisan", 2}

hasilProduk = produkLagi.symmetric_difference(produkLagi1)
print(hasilProduk)
