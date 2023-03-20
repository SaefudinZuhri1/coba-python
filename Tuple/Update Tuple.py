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
