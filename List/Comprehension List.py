buahBuahan = ["Mangga", "Jeruk", "Kiwi"]
tambahBuah = []

for y in buahBuahan:
	if "i" in y:
		tambahBuah.append(y)

print(tambahBuah)

# Jika menggunakan pemahaman daftar
buahBuahan1 = ["Mangga", "Apel", "Anggur", "Jeruk"]
buahBaru = [x for x in buahBuahan1 if "A" in x]

print(buahBaru)