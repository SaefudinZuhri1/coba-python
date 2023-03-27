# Copy Dictionary

# A. Salin Kamus
# Kita tidak dapat menyalin dictionary hanya dengan mengetik dict2 = dict 1, karena dict 2 hanya akan menjadi referensi ke dict 1, dan perubahan yang dimuat di dalam dict1 juga akan otomatis dibuat di dict2.
# Ada cara untuk membuat salinan, salah satunya adalah dengan menggunakan metode dictionary bawaan, yaitu copy()
# Contoh: Buat salinan dictionary dengan method copy()
minuman = {
  "Nama": "Teh Pucuk",
  "Iklan": "Ulat",
  "Tahun": 2010
}
minumanTeh = minuman.copy()
print(minumanTeh)

# Cara yang lain untuk membuat salinan adalah dengan menggunakan function bawaan dict()
# Contoh: Buat salinan dictionary dengan function dict()
iklanTeh = dict(minuman)
print(iklanTeh)
