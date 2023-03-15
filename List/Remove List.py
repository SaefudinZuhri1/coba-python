# Menghapus item tertentu
listBaruLagi = ["UPI", "UNJ", "UNY"]
listBaruLagi.remove("UNY")
print(listBaruLagi)

# Menghapus index tertentu
list11 = ["Jakarta", "Yogyakarta", "Jawa"]
list11.pop(1)
print(list11)

# Jika metode pop tidak ditentukan maka akan menghapus item terakhir
# Menghapus index tertentu
list12 = ["Jakarta", "Yogyakarta", "Jawa"]
list12.pop()
print(list12)

# Menggunakan keyword del untuk menghapus item
list13 = ["Jawa Barat", "Jawa Tengah", "Jawa Timur"]
del list13[0]
print(list13)
