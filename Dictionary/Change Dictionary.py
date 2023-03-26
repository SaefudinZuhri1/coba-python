# Ubah Item Dictionary

# A. Ubah Nilai
# Kita dapat mengubah nilai item tertentu dengan mengacu pada name key
# Contoh: Ubah key
iniMobil = {
  "Nama": "Toyota",
  "Merk": "Avanza",
  "Model": "AVP",
  "Tahun": 2010
}
iniMobil["Model"] = "Sedan"
print(iniMobil)

# B. Perbarui Dictionary
# Method update() akan memperbarui dictionary dengan item dari argumen yang diberikan.
# Argumen harus berupa dictionary, atau objek yang dapat diubah dengan pasangan key:value
# Contoh: Memperbarui key:value menggunakan method update()
iniMobil.update({"Nama": "Suzuki"})
print(iniMobil)
