# Mengakses Sets Item

# A. Akses Item
# Item tidak dapat diakses dalam satu set dengan mengacu pada indeks atau kunci. Tapi bisa mengulang item set menggunakan for loop, atau mengecek apakah ada nilai tertentu dalam set, dengan menggunakan keyword in.
# Contoh: Ulangi set, dan cetak nilainya:
iniSet = {"Januari", "Februari", "Maret"}
for x in iniSet:
  print(x)

# Contoh: Periksa apakah ada "Jakarta" pada set
kotaSets = {"Bandung", "Papua", "Sragen"}
print("Bandung" in kotaSets)
# Jika ada bernilai True dan jika salah bernilai False

# B. Ubah Item
# Setelah satu set dibuat, kita tidak dapat mengubah itemnya, tetapi bisa menambahkan item baru.
