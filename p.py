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

"""Modul perhitungan upah lembur.

Aturan:
- Perhitungan lembur dimulai pukul 16.30.
- Jam ke-1          : 1.5x upah per jam
- Jam ke-2 s.d. ke-3: 2x upah per jam
- Jam ke-4 ke atas  : 3x upah per jam
- Maksimal jam lembur yang dihitung per hari adalah 4 jam.
"""

JAM_MULAI_LEMBUR = (16, 30)   # pukul 16.30
MAKS_JAM_LEMBUR = 4           # batas jam yang dihitung per hari
HARI_KERJA = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]


def waktu_ke_menit(teks_waktu):
    """Ubah teks waktu 'jam.menit' (misal '18.15' atau '18:15') menjadi menit sejak 00.00."""
    teks_waktu = teks_waktu.strip().replace(":", ".")
    bagian = teks_waktu.split(".")
    jam = int(bagian[0])
    menit = int(bagian[1]) if len(bagian) > 1 and bagian[1] != "" else 0
    if not (0 <= jam <= 23 and 0 <= menit <= 59):
        raise ValueError("Format waktu tidak valid")
    return jam * 60 + menit


def hitung_jam_lembur(waktu_selesai):
    """Hitung jam lembur (bilangan bulat) dari waktu selesai, dihitung mulai 16.30.

    Jam dihitung per jam penuh (dibulatkan ke bawah) dan dibatasi MAKS_JAM_LEMBUR.
    """
    mulai = JAM_MULAI_LEMBUR[0] * 60 + JAM_MULAI_LEMBUR[1]
    selesai = waktu_ke_menit(waktu_selesai)
    selisih_menit = selesai - mulai
    if selisih_menit <= 0:
        return 0
    jam = selisih_menit // 60
    return min(jam, MAKS_JAM_LEMBUR)


def hitung_upah_lembur(jam_lembur, upah_perjam):
    """Hitung upah lembur berdasarkan jumlah jam lembur dan upah per jam."""
    total = 0
    for jam_ke in range(1, jam_lembur + 1):
        if jam_ke == 1:
            total += 1.5 * upah_perjam
        elif jam_ke <= 3:
            total += 2 * upah_perjam
        else:
            total += 3 * upah_perjam
    return int(total)


def format_rupiah(angka):
    """Format angka menjadi 'Rp 70.000'."""
    return "Rp " + f"{angka:,}".replace(",", ".")


if __name__ == "__main__":
    # Pengujian singkat modul (hanya jalan jika file ini dijalankan langsung)
    upah = 20000
    assert hitung_upah_lembur(0, upah) == 0
    assert hitung_upah_lembur(1, upah) == 30000
    assert hitung_upah_lembur(2, upah) == 70000
    assert hitung_upah_lembur(3, upah) == 110000
    assert hitung_jam_lembur("16.30") == 0
    assert hitung_jam_lembur("18.15") == 1
    assert hitung_jam_lembur("19.30") == 3
    assert hitung_jam_lembur("23.00") == 4   # dibatasi maksimal 4 jam
    print("Semua pengujian modul lembur berhasil.")
