#Dictionary bisa diurutkan, diubah, dan elemen (key) tidak ada yang duplikat
dict_mhs = {'nim':'117', 
            'nama' : 'Yafi', 
            'telepon': '081111111',
            'tinggi' : 168, 
            'kota' : 'Surakarta'}
dict_mhs
dict_mhs['telepon']='08888'
print(dict_mhs['telepon'])
# Cara pertama 
dict_mhs["kost"] = True
# Cara kedua
dict_mhs.update({"kost": True})
print(type(dict_mhs))
print(dict_mhs)
print(dict_mhs['nama'])
print(dict_mhs['telepon'])
dict_mhs.update({"telepon": "081212"})
print(dict_mhs['telepon'])
# Mengapus satu data
dict_mhs.pop("tinggi")
print(dict_mhs)

# Mengapus seluruh data
dict_mhs.clear()
print(dict_mhs)

# Menghapus varibel dictionary
del(dict_mhs)
#print(dict_mhs)

# Mengakses berdasarkan key 
print(dict_mhs['nama'])

# Mengakses informasi keys yang digunakan
print(dict_mhs.keys())

# Mengakses seluruh data pada dictionary tunggal
print(dict_mhs.values())

# Mengakses panjang data dictionary tunggal
print(len(dict_mhs))

# Mengakses tipe data
print(type(dict_mhs))

# Mengakses key dan value menggunakan iterasi
for key in dict_mhs:
    print(key, dict_mhs[key])
    
for value in dict_mhs.values():
    print(value)
    
for key, value in dict_mhs.items():
    print(key, value)
    
#Memeriksa apakah Key dan Value ada dalam Dictionary
# Cek key dalam dictionary
print('handphone' in dict_mhs)

# Periksa value ada dalam dictionary
print('Andhika' in dict_mhs.values())