# Set Python
# Sintaks: mysets = {"value1", "value2", "value3"}

# A. Set
# Set digunakna untuk menyimpan beberapa item dalam satu variabel.
# Set adalah salah satu dari 4 tipe data bwaan di Python yang gunanya untuk menyimpan kumpulan data. 3 tipe data lainnya adalah List, Tuple, dan Dictionary, semua mempunyai kualitas dan penggunaan yang berbeda.

# Set adalah kumpulan yang unordered, unchangeable*, dan unindexed.
# Catatan: Set item tidak dapat diubah, tetapi dapat menghapus item dan menambahkan item baru.

# Contoh: Buat Set
iniSet = {"Apel", "Mangga", "Jeruk"}
print(iniSet)
# Catatan: Set tidak diurutkan, jadi tidak dapat dipastikan urutan yang akan muncul

# B. Tetapkan Item
# Set item tidak diurutkan, tidak dapat diubah, dan tidak mengizinkan duplikat

# C. Tidak dipesan
# Unordered artinya item dalam satu set tidak memiliki urutan yang ditentukan.
# Set item dapat muncul dalam urutan yang berbeda setiap kali menggunakannya, dan tidak dapat dirujuk dengan indeks atau kunci.

# D. Tidak dapat diubah
# Item set tidak dapat diubah, artinya tidak dapat mengubah item setelah set dibuat.
## Setelah set dibuat, kita tidak bisa merubah itemnya, tetapi dapat menghapus dan menambahkan item baru.

# E. Duplikat Tidak Diizinkan
# Set tidak boleh memiliki dua item dengan nilai yang sama.
# Contoh: Nilai duplikat akan diabaikan
kota = {"Jakarta", "Dumay", "Jambi", "Jakarta"}
print(kota)

## Catatan: Nilai True dan 1 dianggap sebagai nilai yang sama dalam kumpulan, dan diperlakukan sebagai duplikat.
# Contoh: True dan 1 dianggap nilai yang sama
iniSet1 = {"Mangga", "Jeruk", "Monas", True, 1, 3}
print(iniSet1)

# F. Dapatkan Panjang Set
# Untuk menentukan berapa banyak item yang dimiliki suatu set, gunakan function len()
# Contoh: Dapatkan jumlah item dalam satu set
panjangSet = {"Markisa", "Melon", "Mangga"}
print(len(panjangSet))

# G. Tetapkan Item –
# Set item dapat berupa tipe data apapun
# Contoh: Tipe data string, boolean, float, integer
tipeString = {"ABA", "APA", "AJA"}
tipeNumber = {1, 2, 8, 0.2, 1.9}
tipeBool = {True, False, True, True}

print(tipeString)
print(tipeNumber)
print(tipeBool)

# Satu set dapat berisi tipe data yang berbeda
# Contoh: Satu set berisi string, float, int, boolean
gabunganSet = {"ABJAD", 20, True, 0.2, "male"}
print(gabunganSet)

# H. type()
# Dari prespektif Python, set didefinisikan sebagai objek dengan tipe data 'set'
# Sintaks <class 'set'>
# Contoh: Apa tipe data ini?
tebakTipeData = {"Benar", "Salah", 08.2}
print(type(tebakTipeData))

# I. Konstruktor Set()
# DImungkinkan juga untuk menggunakan konstruktor set() untuk membuat set
# Contoh: Menggunakan konstruktor set() untuk membuat set
setBuatan = set(("Tomat", "Wortel", "Kol")) # Digabung dengan dua tanda kurung
print(setBuatan)

# Saat memilih tipe koleksi, akan sangat berguna untuk memahami properti dari tipe data tersebut. Memilih jenis yang tepat untuk kumpulan data tertentu dapat berarti retensi makna, dan dapat berarti peningkatan efisiensi atau keamanan.





