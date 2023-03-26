# Mengakses Item Dictionary

# A. Mengakses Item
# Kita dapat mengakses item dictionary dengan mengacu pada key name, di dalam tanda kurung siku
# Contoh: Dapatkan key value
iniBrand = {
  "Jenis": "Smartphone",
  "Brand": "Apple",
  "Version": 14,
  "Tahun": 2022
}

z = iniBrand["Brand"]
z1 = iniBrand.get("Version")
print(z)
print(z1)

# Terdapat method bernama get() yang akan memberi hasil yang sama

# B. Dapatkan Kunci
# keys() method akan mengembalikan daftar semua key dalam dictionary
# Contoh: Dapatkan daftar kunci
x = iniBrand.keys()
print(x)

# Daftar key adalah tampilan dictionary, artinya setiap perubahan yang dilakukan pada kamus akan tercermin dalam daftar kunci
# Contoh: Tambahkan item baru ke dictionary asli, dan lihat bahwa daftar kunci juga diperbarui

kota = {
  "Nama": "Bogor",
  "Provinsi": "Jawa Barat",
  "Wilayah": 3
}

a = kota.keys()
print(a) # Sebelum terdapat perubahan

kota["Kabupaten"] = "Bogor"

print(a) # Setelah terdapat perubahan

# C. Dapatkan Nilai
# values() method akan mengembalikan daftar semua nilai dalam kamus
u = kota.values()
print(u)
# Daftar nilai adalah tampilan dictionary, artinya setiap perubahan yang dilakukan pada dictionary akan tercermin dalam daftar nilai
# Contoh: Buat perubahana di dictionary asli, dan lihat bahwa daftar nilai juga diperbarui
a = kota.values()

kota["Tahun"] = 1990
print(a)

# Dapatkan Item
# items() method akan mengembalikan setiap item dalam dictionary, sebagai tuple dalam daftar
# Contoh: Dapatkan list key:value pair
a = kota.items()
print(a)

# D. Periksa apakah Kunci Ada
# Contoh: Periksa apakah ada di dictionary:
if "Kabupaten" in kota:
  print("Ya, 'Kabupaten' Bogor adalah bagian dari dictionary")
