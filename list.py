##Bisa diurutkan,bisa diubah/ditambah
mahasiswa = ['yafi','basthan','kentza','haikal']
print ("Daftar Mahasiswa :", mahasiswa)
mahasiswa [3]= 'haef'
print ("Daftar Mahasiswa Baru :")
print (mahasiswa[-1])
print (mahasiswa[-2])
print (mahasiswa[-3])
print(type(mahasiswa))
print(len(mahasiswa))
# Menggunakan Pengulangan While
mahasiswa = ['yafi','basthan','kentza','haikal']
nMahasiswa = len(mahasiswa)
myIndex = 0 # indeks dimulai dengan nilai 0
while myIndex < nMahasiswa:
    print(mahasiswa[myIndex])
    myIndex = myIndex + 1 # increment indeks
    
# Menggunakan pengulangan for <item> in <lists>
mahasiswa = ['yafi','basthan','kentza','haikal']
for item in mahasiswa:
    print(item)

#Menggunakan for <counter> in range (<start>, <end>)
for i in range(1,3):
    print(mahasiswa[i])
    
# Penerapan list comprehension, membuat list mahasiswa yang ada huruf a
mahasiswa = ['yafi','basthan','kentza','haikal']
newmahasiswa = [x for x in mahasiswa if "a" in x]
print(newmahasiswa)

#Mengurutkan data 
mahasiswa = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswa.sort (key=str.lower)
print(mahasiswa)
mahasiswa.sort() #KAPITAL LEBIH DULU
print(mahasiswa)

#Menukar posisi data
mahasiswa = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswa.reverse ()
print(mahasiswa)

#Menggabungkan data pada list
mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
mahasiswa = mahasiswaA+mahasiswaB #menggunakan +
print(mahasiswa)

mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
for x in mahasiswaB :
    mahasiswaA.append(x) #Menggunakan append
print(mahasiswaA)

mahasiswaA = ['yafi', 'Kentza', 'basthan', 'Haikal', 'dimas', 'Ndaru']
mahasiswaB = ['adib', 'sulthan', 'afif']
mahasiswaA.extend(mahasiswaB) #Menggunakan extend
print(mahasiswaA)

listBuah = []
listBuah.append ("Jeruk")
listBuah.append ("Mangga")
listBuah.append ('Apel')
print (listBuah)
# Menambahkan data pada indeks tertentu
listBuah.insert(1, "Belimbing")
listBuah.insert(3, "Alpukat") 
print(listBuah)
# Menambahkan beberapa item sekaligus ke bagian akhir data
listBuah.extend(["Mangga","Pisang"])
print(listBuah)

listC = ["yafi", '168', '85', 'Kudus']
print ("nama :", listC [0])
print ("tinggi badan :", listC [1])
print (dir(list))

#Menghapus elemen
#Yang disebutkan dalam remove
mahasiswa = ['yafi', 'basthan', 'kentza', 'haikal']
mahasiswa.remove('kentza')
print(mahasiswa)

#Berdasar index
mahasiswa = ['yafi', 'basthan', 'kentza', 'haikal']
mahasiswa.pop() #jk index tidak dimasukkan makan elemen terakhir terhapus
mahasiswa.pop(2) #akan terhapus posisi 2
print(mahasiswa)

#Mengosongka data pada list
mahasiswa = ['yafi', 'basthan', 'kentza', 'haikal']
mahasiswa.clear()
print(mahasiswa)

#Mengurutkan berdasar abjad A-Z
mahasiswa = ['yafi', 'basthan', 'kentza', 'haikal']
mahasiswa.sort()
print(mahasiswa)

#Mengurutkan dari Z-A
mahasiswa = ['yafi', 'basthan', 'kentza', 'haikal']
mahasiswa.sort(reverse=True)
print(mahasiswa)

dataMahasiswa = [
    [1, 'yafi', '117'],
    [2, 'basthan', '107'],
    [3, 'kentza', '110']
]
print('Cara Pertama')
print('Daftar Mahasiswa :')
print('NIM\t Nama\t Telp')
for i in range(0,len(data_mahasiswa)):
    print(data_mahasiswa[i][0],'\t', data_mahasiswa[i][1], '\t',data_mahasiswa[i][2])
    i += 1