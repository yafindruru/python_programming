#latihan fungsi B
# # 1. Tarif Parkir Kendaraan di Bandara
def hitung_parkir_bandara(jenis_kendaraan, lama_parkir_jam):
    tarif_awal = 0
    tarif_per_jam = 0
    
    if jenis_kendaraan.lower() == "motor":
        tarif_awal = 3000
        tarif_per_jam = 1500
    elif jenis_kendaraan.lower() == "mobil":
        tarif_awal = 5000
        tarif_per_jam = 2000
        
    if lama_parkir_jam <= 1:
        return tarif_awal
    else:
        return tarif_awal + ((lama_parkir_jam - 1) * tarif_per_jam)

# 2. Menghitung Penggajian
def hitung_gaji(gaji_pokok, tunjangan, potongan):
    gaji_bersih = (gaji_pokok + tunjangan) - potongan
    return gaji_bersih

# 3. Menghitung BBI (Berat Badan Ideal - Contoh pakai rumus Broca)
def hitung_bbi(tinggi_badan, jenis_kelamin):
    if jenis_kelamin.lower() == "pria":
        bbi = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.10)
    else:
        bbi = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    return bbi

# 4. Tarif Parkir Kendaraan di Stasiun
def hitung_parkir_stasiun(jenis_kendaraan, inap):
    # Logika sama seperti bandara, sesuaikan dengan tarif stasiun
    pass 

# 5. Kebutuhan Cairan Pengganti Dehidrasi
def kebutuhan_cairan(berat_badan, persen_dehidrasi):
    # Contoh rumus: Defisit cairan (Liter) = Berat Badan (kg) x % Dehidrasi
    defisit_cairan = berat_badan * (persen_dehidrasi / 100)
    return defisit_cairan

# 6. Menentukan Tarif Tol Kendaraan
def hitung_tarif_tol(golongan_kendaraan):
    tarif = {
        "Golongan 1": 15000,
        "Golongan 2": 25000,
        "Golongan 3": 35000
    }
    return tarif.get(golongan_kendaraan, "Golongan tidak valid")

#print(f"teks {variabel}")
print("=== HASIL PROGRAM TUGAS ===")

# 1. Print Parkir Bandara (Contoh: Mobil, 3 Jam)
hasil_parkir = hitung_parkir_bandara("mobil", 3)
print(f"1. Tarif Parkir Bandara (Mobil, 3 jam) : Rp {hasil_parkir}")

# 2. Print Penggajian (Contoh: Gaji 5jt, Tunjangan 1jt, Potongan 200rb)
hasil_gaji = hitung_gaji(5000000, 1000000, 200000)
print(f"2. Gaji Bersih Karyawan                : Rp {hasil_gaji}")

# 3. Print BBI (Contoh: Pria, Tinggi 170 cm)
hasil_bbi = hitung_bbi(170, "pria")
print(f"3. Berat Badan Ideal (Pria, 170cm)     : {hasil_bbi} kg")

# 4. Print Parkir Stasiun (Contoh: Motor, 5 Jam)
hasil_stasiun = hitung_parkir_stasiun("motor", 5)
print(f"4. Tarif Parkir Stasiun (Motor, 5 jam) : Rp {hasil_stasiun}")

# 5. Print Kebutuhan Cairan (Contoh: BB 60kg, Dehidrasi 5%)
hasil_BBI = hitung_BBI(60, 5)
print(f"5. Kebutuhan Cairan Pengganti          : {hasil_cairan} Liter")

# 6. Print Tarif Tol (Contoh: Golongan 2)
hasil_tol = hitung_tarif_tol(2)
print(f"6. Tarif Tol (Golongan 2)              : Rp {hasil_tol}")

# ==========================================
# DEFINISI FUNGSI
# ==========================================

# 1. Tarif Parkir Kendaraan di Bandara
def hitung_parkir_bandara(jenis, lama_jam):
    tarif_awal = 5000 if jenis.lower() == "mobil" else 3000
    tarif_berikutnya = 2000 if jenis.lower() == "mobil" else 1500
    
    if lama_jam <= 1:
        return tarif_awal
    else:
        return tarif_awal + ((lama_jam - 1) * tarif_berikutnya)

# 2. Menghitung Penggajian
def hitung_gaji(gaji_pokok, tunjangan, potongan):
    return (gaji_pokok + tunjangan) - potongan

# 3. Menghitung BBI (Berat Badan Ideal)
def hitung_bbi(tinggi, jk):
    if jk.lower() == "pria":
        return (tinggi - 100) - ((tinggi - 100) * 0.10)
    else:
        return (tinggi - 100) - ((tinggi - 100) * 0.15)

# 4. Tarif Parkir Kendaraan di Stasiun (Misal tarif flat + per jam)
def hitung_parkir_stasiun(jenis, lama_jam):
    tarif_awal = 4000 if jenis.lower() == "mobil" else 2000
    tarif_berikutnya = 2000 if jenis.lower() == "mobil" else 1000
    
    if lama_jam <= 1:
        return tarif_awal
    else:
        return tarif_awal + ((lama_jam - 1) * tarif_berikutnya)

# 5. Menentukan kebutuhan cairan pengganti bagi dehidrasi
def hitung_cairan(berat_badan_kg, persen_dehidrasi):
    # Rumus sederhana: Defisit (Liter) = Berat Badan x % Dehidrasi
    return berat_badan_kg * (persen_dehidrasi / 100)

# 6. Menentukan Tarif Tol Kendaraan
def hitung_tarif_tol(golongan):
    tarif = {
        "1": 15000,
        "2": 25000,
        "3": 35000
    }
    return tarif.get(str(golongan), "Golongan tidak terdaftar")


# ==========================================
# PEMANGGILAN FUNGSI & PRINT HASIL
# ==========================================

print("=== HASIL PROGRAM TUGAS ===")

# 1. Print Parkir Bandara (Contoh: Mobil, 3 Jam)
hasil_parkir = hitung_parkir_bandara("mobil", 3)
print(f"1. Tarif Parkir Bandara (Mobil, 3 jam) : Rp {hasil_parkir}")

# 2. Print Penggajian (Contoh: Gaji 5jt, Tunjangan 1jt, Potongan 200rb)
hasil_gaji = hitung_gaji(5000000, 1000000, 200000)
print(f"2. Gaji Bersih Karyawan                : Rp {hasil_gaji}")

# 3. Print BBI (Contoh: Pria, Tinggi 170 cm)
hasil_bbi = hitung_bbi(170, "pria")
print(f"3. Berat Badan Ideal (Pria, 170cm)     : {hasil_bbi} kg")

# 4. Print Parkir Stasiun (Contoh: Motor, 5 Jam)
hasil_stasiun = hitung_parkir_stasiun("motor", 5)
print(f"4. Tarif Parkir Stasiun (Motor, 5 jam) : Rp {hasil_stasiun}")

# 5. Print Kebutuhan Cairan (Contoh: BB 60kg, Dehidrasi 5%)
hasil_cairan = hitung_cairan(60, 5)
print(f"5. Kebutuhan Cairan Pengganti          : {hasil_cairan} Liter")

# 6. Print Tarif Tol (Contoh: Golongan 2)
hasil_tol = hitung_tarif_tol(2)
print(f"6. Tarif Tol (Golongan 2)              : Rp {hasil_tol}")