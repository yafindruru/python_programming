import math
a = 9
ak = math.sqrt(a)
print(ak)
pk = pow (a, 3)
print(pk)

def luasSegitiga(alas, tinggi):
    luas = 0.5*alas*tinggi
    return luas

#Pemanggilan function
luas_Sgt = luasSegitiga(20, 15)
print(luas_Sgt)
print(f"Luas Segitiga : (luas_Sgt)")
print(f"Luas Segitiga : (luasSegitiga(100, 320))")

#Contoh fungsi tidak memiliki nilai balik
def cetakBiodata(nm, hp, email):
    print ("Data Pengguna Program")
    print("="*25)
    print("Nama /t/t :", nm)
    print("Handphone /t :", hp)
    print("Email /t/t :", email)

nama = "Mila"
handphone = "-"
email = "mila@gmail.com"

cetakBiodata(nama,handphone,email)

# fungsi statistik nilai kelas
def hitung_statistik_nilai(listNilai):
    total = 0
    for nilai in listNilai:
        total = total + nilai
    rataan = total / len(listNilai)
    # rataan = sum(listNilai)/len(listNilai) # ALternatif cara
    variansi = sum((x-rataan)**2 for x in listNilai) / len(listNilai)
    stddev = variansi ** 0.5
    return total, rataan, stddev

nilai_kelasA = [78, 89, 88, 97]

totalNIlai, rataanNilai, stdevNilai = hitung_statistik_nilai(nilai_kelasA)
print("Total Nilai Kelas : ", totalNIlai)
print("Rata-rata Nilai Kelas : ", rataanNilai)
print("Standar Deviasi Nilai Kelas : ", stdevNilai)

# fungsi statistik nilai kelas
#import statisticss as stat
def hitung_statistik_nilai(listNilai):
    total = 0
    for nilai in listNilai:
        total = total + nilai
    rataan = total / len(listNilai)
    # rataan = sum(listNilai)/len(listNilai) # ALternatif cara
    #rataan = stat.mean(listNilai) #Alternatif cara
    variansi = sum((x-rataan)**2 for x in listNilai) / len(listNilai)
    stddev = variansi ** 0.5 #stddev = math.sqrt(variansi)
    #standardeviasi = stat.stddev(listNilai)
    return total, rataan, stddev

nilai_kelasA = [78, 89, 88, 97]

nilaistat = hitung_statistik_nilai(nilai_kelasA)
totalNIlai, rataanNilai, stdevNilai = hitung_statistik_nilai(nilai_kelasA)
#nilaiStat = hitung_statistik_nilai(nilai_krlasA)
print("Total Nilai Kelas : ", totalNIlai)
print("Rata-rata Nilai Kelas : ", rataanNilai)
print("Standar Deviasi Nilai Kelas : ", stdevNilai)