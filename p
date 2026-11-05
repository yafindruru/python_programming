dict_mhs = {'nim':'117', 
            'nama' : 'Yafi', 
            'telepon': '081111111',
            'tinggi' : 168, 
            'kota' : 'Surakarta'}
dict_mhs
dict_mhs['telepon']='08888'
print(dict_mhs['telepon'])
dict_mhs.clear()
print (dict_mhs)

mahasiswa = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswa.sort (key=str.lower)
print(mahasiswa)
mahasiswa.sort()
print(mahasiswa)

mahasiswa = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswa.reverse ()
print(mahasiswa)

mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
mahasiswa = mahasiswaA+mahasiswaB
print(mahasiswa)

mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
for x in mahasiswaB :
    mahasiswaA.append(x)
print(mahasiswaA)
mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
mahasiswaB.extend(mahasiswaA)
print(mahasiswaB)

print(mahasiswaA)
mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
mahasiswaA.extend(mahasiswaB)
print(mahasiswaA)

dataMahasiswa = [
    [1, 'yafi', '117'],
    [2, 'basthan', '107'],
    [3, 'kentza', '110']
]
print('Cara Pertama')
print('Daftar Mahasiswa :')
print('NIM\t Nama\t Telp')
for i in range(0,len(dataMahasiswa)):
    print(dataMahasiswa[i][0],'\t', dataMahasiswa[i][1], '\t',dataMahasiswa[i][2])
    i += 1
    
def luasSegitiga(alas, tinggi):
    luas = 0.5*alas*tinggi
    return luas

#Pemanggilan function
luas_Sgt = luasSegitiga(20, 15)
print(luas_Sgt)
print(f"Luas Segitiga : (luas_Sgt)")
