buahBuahan = ["Mangga", "Jeruk", "Kiwi"]
tambahBuah = []

for y in buahBuahan:
	if "i" in y:
		tambahBuah.append(y)

print(tambahBuah)

# Jika menggunakan pemahaman daftar
buahBuahan1 = ["Mangga", "Apel", "Anggur", "Jeruk"]
buahBaru = [x for x in buahBuahan1 if "A" in x]
buahBaru1 = [y for y in buahBuahan1 if y != "Apel"]
kondisiLain = [z for z in buahBuahan1]

print(buahBaru)
print(buahBaru1)
print(kondisiLain)

# Penjelasan jika kondisi if y != "Apel" maka akan memunculkan buah selain apel
# Penjelasan kondisiLain hanyalah opsional
# Sintaks
#newlist = [expression for item in iterable if condition == True]

