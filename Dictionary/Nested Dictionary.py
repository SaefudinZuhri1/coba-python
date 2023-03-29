# Nested Dictionaries

# A. Nested Dictionary
# Pada dictionary dapat berisi dictionary, disebut sebagai nested dictionary.
# Contoh: Dictionary yang berisi tiga dictionary
dataMahasiswa = {
  "Mahasiswa1" : {
  "Nama" : "Januarta",
  "Angkatan" : 2020
  },
  "Mahasiswa2" : {
  "Nama" : "Daniel",
  "Angkatan" : 2021
  },
  "Mahasiswa3" : {
  "Nama" : "Rafli",
  "Angkatan" : 2022
  }
}

# Jika kita ingin menambahkan tiga dictionary ke dalam dictionary baru
# Contoh: Buat tiga dictionary, lalu buat satu dictionary yang berisi tiga dictionary lainnya
mahasiswa1 = {
  "Nama" : "Danil",
  "Angkatan": 2019
}
mahasiswa2 = {
  "Nama" : "Dwi",
  "Angkatan" : 2021
}
mahasiswa3 = {
  "Nama" : "Alvin",
  "Angkatan" : 2022
}

dataMahasiswa = {
  "mahasiswa1" : mahasiswa1,
  "mahasiswa2" : mahasiswa2,
  "mahasiswa3" : mahasiswa3
}
print(dataMahasiswa)

# B. Akses Item pada Nested Dictionary
# Untuk mengakses item dari nested dictionary, kita gunakan nama dictionary, dimulai dengan dcitionary terluar
# Contoh: Cetak item dictionary
print(dataMahasiswa["mahasiswa2"]["Angkatan"])
