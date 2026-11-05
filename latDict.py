# Program Pengolahan Nilai Mahasiswa dengan Dictionary & Input Pengguna

data_mahasiswa = {}

print("=== PROGRAM INPUT DATA NILAI MAHASISWA ===")
jumlah_data = int(input("Masukkan jumlah mahasiswa yang ingin diinput: "))

for i in range(jumlah_data):
    print(f"\n--- Data Mahasiswa ke-{i+1} ---")
    nama = input("Masukkan Nama Mahasiswa : ")
    
    # Input nilai dengan validasi sederhana/konversi tipe data
    tugas = float(input("Masukkan Nilai Tugas    : "))
    uts = float(input("Masukkan Nilai UTS      : "))
    uas = float(input("Masukkan Nilai UAS      : "))
    
    # Menghitung nilai akhir (Bobot: Tugas 30%, UTS 35%, UAS 35%)
    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
    
    # Menyimpan data ke dalam nested dictionary
    data_mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }

# Menampilkan seluruh data yang telah dimasukkan
print("\n" + "="*45)
print(f"{'Nama':<15} | {'Tugas':<6} | {'UTS':<6} | {'UAS':<6} | {'Akhir':<6}")
print("="*45)

for nama, info in data_mahasiswa.items():
    print(f"{nama:<15} | {info['tugas']:<6.1f} | {info['uts']:<6.1f} | {info['uas']:<6.1f} | {info['nilai_akhir']:<6.2f}")

print("="*45)