# Menambahkan Sets

# A. Tambahkan Item
# Setelah satu set dibuat, kita tidak dapat mengubah itemnya, tetapi dapat menambahkan item baru.
# Untuk menambahkan satu item ke set, gunakan methode add().
# Contoh: Tambahkan item ke set, menggunakan methode add()
bulanSets = {"Juli", "Agustus", "September"}
bulanSets.add("Juni")
print(bulanSets)

# B. Tambahkan Set
# Untuk menambahkan item dari set lain ke set saat ini, gunakan method() update.
# Contoh: Tambahkan elemen dari satu set ke set lain
bulaLalu = {"Januari", "Februari", "Maret"}
bulanSekarang = {"April", "Mei", "Juni"}

bulaLalu.update(bulanSekarang)

print(bulaLalu)

# C. Tambahkan Setiap Iterable
# Objek dalam method update() tidak harus satu set, bisa berupa objek yang dapat diubah (tuple, list, dictionary, dll)
# Contoh: Tambahkan elemen daftar ke set:
setKota = {"Jakarta", "Bogor", "Tasik", "Garut"}
listKota = ["Cimahi", "Padalarang"]

setKota.update(listKota)
print(setKota)
# Akan menghasilkan gabungan list dan set namun dalam bentuk set.







