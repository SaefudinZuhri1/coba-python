buahBuahan = ["Mangga", "Jeruk", "Kiwi"]
tambahBuah = []

for y in buahBuahan:
	if "i" in y:
		tambahBuah.append(y)

print(tambahBuah)

# Jika menggunakan pemahaman daftar
buahBuahan1 = ["Mangga", "Apel", "Anggur", "Jeruk"]
buahBaru = [x for x in buahBuahan1 if "A" in x]
buahBaru1 = [y for y in buahBuahan1 if y != "Apel"]
kondisiLain = [z for z in buahBuahan1]

print(buahBaru)
print(buahBaru1)
print(kondisiLain)

# Penjelasan jika kondisi if y != "Apel" maka akan memunculkan buah selain apel
# Penjelasan kondisiLain hanyalah opsional
# Sintaks
#newlist = [expression for item in iterable if condition == True]

# Iteration
angka = [x for x in range(25)]
print(angka)

# Contoh iteration dengan syarat
angka1 = [x for x in range(20) if x < 16]
print(angka1)

# Expression 1
# Expression merupakan item yang ada saat iterasi berjalan, tetapi juga hasil yang dapat dimanipulasi sebelum berakhir
namaKota = ["JAKARTA", "BANDUNG", "BEKASI", "TANGERANG", "BOGOR"]
kotaLagi = [y.lower() for y in namaKota]
print(kotaLagi)

# Expression 2
# List dapat diganti dengan apapun
namaKota1 = ["JAKARTA", "BANDUNG", "BEKASI", "TANGERANG", "BOGOR"]
ubahKota = ['Yogyakarta' for z in namaKota1]
print(ubahKota)

# Expression 3
# Bisa berisi kondisi, bukan untuk filter, tapi untuk memanipulasi hasil
namaKota2 = ["JAKARTA", "BANDUNG", "BEKASI", "TANGERANG", "BOGOR"]
ubahKota1 = [x if x != "BANDUNG" else "DEPOK" for x in namaKota2]
print(ubahKota1)











