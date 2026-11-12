#modul
# modul_lembur.py

def hitung_durasi_jam(waktu_selesai):
    """Fungsi untuk menghitung durasi lembur dalam satuan jam penuh"""
    if not waktu_selesai or waktu_selesai == '0':
        return 0
        
    # Mengubah format input (misal "18.15" atau "18:15") menjadi jam dan menit
    waktu_selesai = waktu_selesai.replace(':', '.')
    try:
        jam_selesai, menit_selesai = map(int, waktu_selesai.split('.'))
    except ValueError:
        # Jika user hanya memasukkan angka jam tanpa menit (misal "18")
        jam_selesai = int(waktu_selesai)
        menit_selesai = 0

    # Mengubah semua waktu ke dalam bentuk total menit
    total_menit_selesai = (jam_selesai * 60) + menit_selesai
    total_menit_mulai = (16 * 60) + 30  # Lembur mulai jam 16.30

    selisih_menit = total_menit_selesai - total_menit_mulai

    # Jika selisih negatif (pulang sebelum 16.30), tidak dihitung lembur
    if selisih_menit <= 0:
        return 0

    # Dibulatkan ke bawah ke jam penuh terdekat
    durasi_jam = selisih_menit // 60
    return durasi_jam

def hitung_upah(jam_lembur, upah_per_jam):
    """Fungsi untuk menghitung total upah berdasarkan jam"""
    if jam_lembur <= 0:
        return 0

    # Ketentuan: maksimal yang dihitung adalah 4 jam
    if jam_lembur > 4:
        jam_lembur = 4

    total_upah = 0
    for jam in range(1, jam_lembur + 1):
        if jam == 1:
            total_upah += 1.5 * upah_per_jam
        elif jam == 2 or jam == 3:
            total_upah += 2 * upah_per_jam
        else: # Jam lebih dari 3 (yaitu jam ke-4)
            total_upah += 3 * upah_per_jam

    return int(total_upah)

def format_rupiah(angka):
    """Fungsi pembantu untuk memformat angka menjadi format ribuan dengan titik"""
    return f"{angka:,}".replace(',', '.')