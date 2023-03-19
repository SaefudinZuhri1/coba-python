# Salin daftar
## Tidak dapat menyalin daftar dengan mengetik list1 = list 2
# Karena list2 hanya akan menjadi referensi ke list1, dan perubahan yang dilakukan akan secara otomatis dilakukan di list2
### Menggunakan metode list bawaan copy()

copyList = ["Banana", "Pisang", "Mango", "Mangga"]
listSaya = copyList.copy()
print(listSaya)

# Cara lain untuk membuat salinan
copyList1 = ["Jakarta", "Bandung", "Bogor"]
listSaya1 = copyList1.copy()
print(listSaya1)