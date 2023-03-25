# Python - Loop Tuple

# A. Loop Melalui Tuple
# Kita dapat mengulang item tuple menggunakan for loop
# Iterasi melalui item dan cetak nilainya. Contoh:
tupleContoh = ("Jus", "Sari Buah", "Nutrisari")
for z in tupleContoh:
  print(z)

# B. Loop Melalui Nomor Indeks
# Kita dapat mengulang item tuple dengan mengacu pada nomor indeksnya. Gunakan fungsi range() and len() untuk membuat iterable yang sesuai
# Cetak semua item dengan mengacu pada nomor indeksnya. Contoh:
buahBuahan = ("Apel", "Mangga", "Pisang")
for x in range(len(buahBuahan)):
  print(buahBuahan[x])

# C. Menggunakan While Loop
# Kita dapat mengulang item tuple dengan menggunakan while loop. Gunakan function len() untuk menentukan panjang tuple, lalu mulai dari 0 dan lewati item tuple dengan mengacu pada indeksnya.
# Selalu tambah indeks sebesar 1 setelah setiap iterasi (i = i + 1)
# Contoh:
kota = ("Bandung", "Cimahi", "Padalarang", "Purwakarta")
x = 0
while x < len(kota):
  print(kota[x])
  x = x + 1
# Mencetak semua item, gunakan while loop untuk melewati semua nomor indeks.
