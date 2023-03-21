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

