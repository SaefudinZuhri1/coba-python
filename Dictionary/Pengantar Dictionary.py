# Python Dictionary
# Sintaks
thisDict = {
  "Nama": "Januarta",
  "Pekerjaan": "Karyawan",
  "Umur": 23
  }

# A. Dictionary
# Dictionary digunakan untuk menyimpan nilai data dalam pasangan key:value.
# Dictionary merupakan kumpulan yang dipesan, dapat diubah, dan tidak mungkin diduplikat.
# Dictionary ditulis dengan kurung kurawal, dan memiliki key dan value
# Contoh: Membuat dan mencetak dictionary
dataDiri = {
  "Nama": "Januarta",
  "Pekerjaan": "Karyawan",
  "Umur": 23
  }
print(dataDiri)

# B. Item Dictionary
# Item dictionary dipesan, diubah, dan tidak memungkinkan untuk diduplikat
# Item dictionary disajikan dengan pasangan key:value, dan dapat dirujuk menggunakan name key
# Contoh: Cetak nilai salah satu key
dataDiri1 = {
  "Nama": "Fauzi",
  "Jabatan": "Sales",
  "Umur": 32
  }
print(dataDiri1["Jabatan"])

# C. Diurutkan atau Tidak Diurutkan
# Dapat dikatakan bahwa dictionary diurutkan, artinya item memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah
# Unordered berarti item tidak memiliki urutan yang ditentukan, kita tidak dapat merujuk item dengan menggunakan indeks

# D. Dapat Diubah
# Dictionary dapat diubah, artinya kita dapat mengubah, menambah, atau menghapus item setelah dibuatnya Dictionary

# E. Duplikat Tidak Diizinkan
# Dictionary tidak boleh memiliki dua item dengan key yang sama
# Contoh: Nilai duplikat akan menimpa nilai yang ada
dataDiri2 = {
  "Nama": "Ilham",
  "Pekerjaan": "Karyawan",
  "Pekerjaan": "HRD",
  "Umur": 23
  }
print(dataDiri2)
# Maka akan memunculkan nilai pada kunci pertama

# F. Panjang Dictionary
# Untuk menentukan berapa banyak item yang dimiliki dictionary, gunakan function len()
# Contoh: Cetak jumlah item dalam dictionary
dataKaryawan = {
  "Nama": "Januarta",
  "Pekerjaan": "Karyawan",
  "Umur": 23
  }
print(len(dataKaryawan))

# G. Item Dictionary - Data Type
# Nilai dalam item kamus dapat berupa tipe data apapun
# Contoh: Tipe data string, int, boolean, dan list
dataKaryawan1 = {
  "Nama": "Januarta",
  "Pekerjaan": "Karyawan",
  "Umur": 23,
  "Pekerja Tetap": True,
  "Jobdesk": ["Mencari supplier", "Membuat dokumen", "Unggah kerjasama"]
  }
print(dataKaryawan1)

# H. type()
# Pada perspektif Python, dictionary didefinisikan sebagai objek dengan tipe data 'dict'
# Output <class 'dict'>
# Contoh: Cek tipe data
dataKaryawan2 = {
  "Nama": "Januarta",
  "Pekerjaan": "Karyawan",
  "Umur": 23
  }
print(type(dataKaryawan2))

# I. Constractur dict()
# Memungkinkan kita menggunakan konstruktor dict() dalam pembuatan dictionary
dataTetap = dict(jadwal = "True", lama_kerja = 10, umur = 19)
print(dataTetap)
