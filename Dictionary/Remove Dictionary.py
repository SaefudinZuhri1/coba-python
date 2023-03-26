# Menghapus Item Dictionary

# A. Menghapus Item
# Ada beberapa metode untuk menghapus item dari dictionary
# Contoh: Method pop() menghapus item dengan nama key yang ditentukan
iniKota = {
  "Nama": "Bekasi",
  "Ibukota": "Cikarang",
  "Pembangunan": 2000
}
iniKota.pop("Pembangunan")
print(iniKota)

# Contoh: Method popitem() menghapus item yang dimasukkan terakhir
iniKota.popitem()
print(iniKota)

# Contoh: Keyword del key menghapus item dengan nama kunci yang ditentukan
del iniKota["Nama"]
print(iniKota)

# Contoh: Keyword del dapat menghapus dictionary sepenuhnya
del iniKota
#print(iniKota)
# Akan menghasilkan error

# Contoh: clear() method mengosongkan dictionary
stasiun = {
  "Tipe": "KRL",
  "Jarak": "Jauh",
  "DAOP": 2
}
stasiun.clear()
print(stasiun)
