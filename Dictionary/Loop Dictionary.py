# Loop Dictionary

# A. Loop Melalui Dictionary
# Kita dapat mengulang melalui dictionary dengan menggunakan for loop
# Saat mengulang melalui dictionary, nilai yang dikembalikan adalah key dictionary, tetapi ada metode yang mengembalikan value nya juga.
# Contoh: Cetak semua name key dalam dictionary, satu per satu
iniKota = {
  "Nama": "Bandung",
  "Provinsi": "Jawa Barat",
  "Tahun": 1982
}
for x in iniKota:
  print(x)
# Contoh: Cetak semua value dalam dictionary, satu per satu
for a in iniKota:
  print(iniKota[a])

# Contoh: Dapat menggunakan method values() untuk mengembalikan value dictionary
for c in iniKota.values():
  print(c)

# Contoh: Menggunakan method keys() untuk mengembalikan key dictionary
for z in iniKota.keys():
  print(z)

# Contoh: Mengulangi key dan value, menggunakan method items()
for z, c in iniKota.items():
  print(z, c)
