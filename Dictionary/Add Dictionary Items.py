# Menambahkan Item Dictionary

# A. Menambahkan Item
# Menambahkan item ke dictionary dengan meggunakan key indeks dan baru dan memberikan value
# Contoh
iniKampus = {
  "Nama": "Universitas Logistik dan Bisnis Internasional",
  "Prodi": "Manajemen Logistik",
  "Tahun": 2022
}
iniKampus["Fakultas"] = "FLTB"
print(iniKampus)

# B. Perbarui Dictionary
# Method update() akan memperbarui dictionary dengan item dari argumen yang diberikan. Jika item tidak ada, item akan ditambahkan
# Argumen dapat berupa dictionary, atau objek yang dapat diubah dengan pasangan key:value
# Contoh: Tambahkan item ke dictionary menggunakan method update()
iniKampus.update({"Lokasi": "Bandung"})
print(iniKampus)
