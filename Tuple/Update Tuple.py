# Update Tuple
# Tuple tidak dapat diubah, artinya tidak dapat diubah, ditambah, atau dihapus itemnya setelah tupel dibuat. Namun terdapat beberapa solusi:

## A. Ubah Nilai Tuple
# Setelah tuple dibuat, kita tidak dapat mengubah nilainya. Tuple tidak dapat diubah. Tapi ada solusinya. Kita dapat mengonversi tuple menjadi list, megubah list, dan mengubah kembali dari list menjadi tuple
# Contoh: Ubah tuple menjadi list untuk dapat mengubahnya:
x = ("Jambu", "Jeruk", "Markisa")
y = list(x)
y[2] = "Apel"
x = tuple(y)
print(x)

## B. Tambahkan Item
# Karena tuple tidak dapat diubah, mereka tidak memiliki metode bawaan append(), tetapi ada cara lain untuk menambahkan item ke tuple
# 1. Ubah menjadi daftar: seperti solusi untuk mengubah tuple, diubah menjadi list, menambahkan item, dan mengubah kembali menjadi tuple
# Contoh:
iniTuple = ("Jakarta", "Monas", "TMII")
iniList = list(iniTuple)
iniList.append("Kota Tua")
iniTuple = tuple(iniList)
print(iniTuple)

# 2. Tambahkan Tuple ke Tuple. Diizinkan untuk menambahkan tuple ke tuple baru dengan item tersebut, dan tambahkan ke tuple yang sudah ada
# Contoh:
iniTuple1 = ("Manajemen", "Hubungan Internasional", "Akuntansi")
tambahTuple = ("Manajemen Logistik",)
iniTuple1 += tambahTuple

print(iniTuple1)
# Catatan: Saat membuat tuple hanya satu item, sertakan juga koma setelah item, jika tidak maka akan teridentifikasi sebagai tuple.

# C. Hapus Item
# Catatan: Tidak dapat menghapus item dalam tuple
# Terdapat solusi jika ingin menghapus item. Caranya sama dengan ketika kita menambahkan atau mengganti item pada tuple.
# Contoh
# Mengubah tuple menjadi list, dan ubah kembali menjadi tuple
iniTuple2 = ("Januari", "Februari", "Maret", "April")
ubahTuple = list(iniTuple2)
ubahTuple.remove("Januari")
iniTuple2 = tuple(ubahTuple)
print(iniTuple2)

# Atau dapat juga menghapus semua item dalam tuple
# Gunakan keyword del untuk menghapusnya
iniTuple3 = ("Januari", "Februari", "Maret", "April", "Mei")
del iniTuple3
print(iniTuple3)
# Hasilnya akan error
