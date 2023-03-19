# Menggabungkan dua daftar
# Dapat menggunakan operator + untuk menggabungkan dua list

listHuruf = ["A", "B", "C"]
listAngka = [0, 1, 2, 3]
listGabungan = listHuruf + listAngka
print(listGabungan)

# Cara kedua adalah menambah semua item di list 1 kedalam list 2 satu per satu
# Menggunakan metode append
list1 = ["D", "E", "F", "G"]
list2 = [0, 1, 2, 3]

for z in list2:
	list1.append(z)
print(list1)

# Menggunakan metode extend
list3 = ["A", "I", "U", "E", "O"]
list4 = ["B", "C", "D", "F", "G"]

list3.extend(list4)
print(list3)





