# Tuple digunakan untuk menyimpan banyak item dalam satu list
# Tuple adalah tipe data python yang digunakan untuk menyimpan kumpulan data
# Tuple merupakan koleksi yang dipesan dan tidak dapan diubah
# Tuple ditulis dengan tanda kurung bulat
tupleContoh = ("Jambi", "Aceh", "Medan")
print(tupleContoh)


# Sintaks untuk membuat tuple
iniTuple = ("Jawa", "Madura", "Lampung")
print(iniTuple)

# Item Tuple
# Tidak dapat dipesan, tidak dapat diubah, dan memungkinkan untuk diduplikat
# Item tuple diindeks, item pertama bernilai [0], item kedua [1], dan seterusnya

# Dipesan
# Tuple tidak dapat diubah, artinya tidak dapat diubah, menambah, menghapus item setelah tuple dibuat.

# Izinkan duplikat
# Karena tuple menggunakan indeks, maka dapat memiliki item dengan value yang sama
iniTuple1 = ("Jawa", "Madura", "Makasar", "Surabaya", "Jawa")
print(iniTuple1)

# Panjang Tuple
# Menentukan berapa banyak item, gunakan function len()
iniTuple2 = ("Jakarta", "Semarang", "Karawang", "Cikampek")
print(len(iniTuple2))

# Membuat Tuple dengan Satu Item
# Membuat tuple dengan hanya satu item, menambahkan koma setelah item, jika tidak, python tidak akan mengenali sebagai tuple
# Contoh satu item tuple
iniTuple3 = ("Jakarta",)
print(len(iniTuple3))
# Contoh bukan tuple
iniTuple3 = ("Jakarta")
print(len(iniTuple3))



