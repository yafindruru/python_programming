orang_1 = {'nama_depan': 'Budi', 'nama_belakang': 'Santoso', 'umur': 30, 'kota': 'Jakarta'}
orang_2 = {'nama_depan': 'Siti', 'nama_belakang': 'Aminah', 'umur': 25, 'kota': 'Bandung'}
orang_3 = {'nama_depan': 'Andi', 'nama_belakang': 'Wijaya', 'umur': 35, 'kota': 'Surabaya'}

orang_orang = [orang_1, orang_2, orang_3]

for orang in orang_orang:
    nama_lengkap = f"{orang['nama_depan']} {orang['nama_belakang']}"
    print(f"\nNama: {nama_lengkap}")
    print(f"Umur: {orang['umur']}")
    print(f"Kota: {orang['kota']}")