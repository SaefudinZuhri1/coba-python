# Hapus Item Set

# A. Hapus Item
# Untuk menghapus item dalam satu set, gunakan remove() atau method discard()
# Contoh: Hapus menggunakan metod remove()
namaBuah = {"Jeruk", "Pisang", "Mangga"}
namaBuah.remove("Jeruk")
print(namaBuah)
# Catatan: Jika item yang ingin dihapus tersebut tidak ada, maka remove() akan error.

# Contoh: Hapus item menggunakan method discard():
updateNamaBuah = {"Kelapa", "Lemon", "Kiwi"}
updateNamaBuah.discard("Lemon")
print(updateNamaBuah)
# Catatan: Jika item yang ingin dihapus tidak ada, discard() tidak akan menghasilkan error.

# Bisa menggunakan method pop() untuk menghapus item, tetapi metode ini akan menghapus item secara acak, sehingga kita tidak dapat memastikan item apa yang dihapus.
# Nilai output dari method pop() ini adalah item yang dihapus
# Contoh: Hapus item menggunakan metode pop()
namaKota = {"Jakarta", "Bogor", "Bandung"}
z = namaKota.pop()
print(z)
print(namaKota)

# Catatan: Set tidak diurutkan, jadi saat menggunakan metode pop(), kita tidak tahu item mana yang dihapus.
# Contoh: clear() method mengosongkan set:
namaKota1 = {"Jambi", "Garut", "Semarang"}
namaKota1.clear()
print(namaKota1)

# Contoh: metode del akan menghapus set sepenuhnya
namaBuah1 = {"Jambu", "Nangka", "Nanas"}
del namaBuah1
print(namaBuah1)
# Akan menghasilkan error
