# Mengakses Item Tuple

# Akses Item Tuple
# Item Tuple dapat diakses dengan nomor index
iniTuple = ("Jawa", "Madura", "Minang")
print(iniTuple[2])

# Pengindeksan Negatif
# Indeks negatif artinya mulai dari akhir. -1 mengacu pada item terakhir, -2 mengacu pada item terakhir kedua, dan seterusnya.
iniTuple1 = ("Jawa", "Sumatra", "Papua")
print(iniTuple1[-2])

# Rentang Indeks
# Dapat menentukan rentang indeks dengan menentukan darimana memulai dan mengakhiri rentang
# Saat rentang ditentukan, nilai yang dihasilkan akan menjadi tuple baru dengan item yang ditentukan
iniTuple2 = ("Mangga", "Jeruk", "Pisang", "kamboja")
print(iniTuple2[2:4])
# Penjelasan
## Pencarian dimulai pada item dengan indeks 2 (termasuk) dan berakhir pada item indeks 4 (tapi tidak termasuk)

# Jika mengabaikan nilai awal, rentang akan dimulai dari item pertama
# Contoh:
## Mengembalikan item dari awal, tetapi tidak termasuk nilai "Guru"
iniTuple3 = ("Profesor", "Dokter", "Raja", "Guru", "Pilot")
print(iniTuple3[:3])

# Contoh:
# Jika mengabaikan nilai akhir, rentang berlanjut ke akhir daftar
iniTuple4 = ("Mangga", "Nanas", "Jeruk", "Apel")
print(iniTuple4[1:])

# Rentang Indeks Negatif
# Jika ingin mencari nilai dari akhir tuple tentukan nilai rentang negatif
iniTuple5 = ("Jambu", "Mangga", "Pisang", "Pir", "Jeruk")
print(iniTuple5[-3:-2])
# Menghasilkan output item dari indeks -3 (termasuk) sampai ke index -2 (tidak termasuk)
