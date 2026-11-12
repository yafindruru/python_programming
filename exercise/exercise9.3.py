class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, kota, pekerjaan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.pekerjaan = pekerjaan

    def deskripsikan_pengguna(self):
        print(f"Nama      : {self.nama_depan} {self.nama_belakang}")
        print(f"Umur      : {self.umur} tahun")
        print(f"Kota      : {self.kota}")
        print(f"Pekerjaan : {self.pekerjaan}")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.")


pengguna_satu = Pengguna("Budi", "Santoso", 25, "Surakarta", "Guru")
pengguna_dua = Pengguna("Siti", "Rahayu", 30, "Yogyakarta", "Dokter")
pengguna_tiga = Pengguna("Agus", "Wijaya", 22, "Semarang", "Mahasiswa")

for pengguna in (pengguna_satu, pengguna_dua, pengguna_tiga):
    pengguna.deskripsikan_pengguna()
    pengguna.sapa_pengguna()
    print()