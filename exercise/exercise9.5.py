class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, kota, pekerjaan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.pekerjaan = pekerjaan
        self.percobaan_masuk = 0

    def deskripsikan_pengguna(self):
        print(f"Nama      : {self.nama_depan} {self.nama_belakang}")
        print(f"Umur      : {self.umur} tahun")
        print(f"Kota      : {self.kota}")
        print(f"Pekerjaan : {self.pekerjaan}")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.")

    def tambah_percobaan_masuk(self):
        self.percobaan_masuk += 1

    def reset_percobaan_masuk(self):
        self.percobaan_masuk = 0


pengguna = Pengguna("Budi", "Santoso", 25, "Surakarta", "Guru")

pengguna.tambah_percobaan_masuk()
pengguna.tambah_percobaan_masuk()
pengguna.tambah_percobaan_masuk()
print(f"Percobaan masuk: {pengguna.percobaan_masuk}")

pengguna.reset_percobaan_masuk()
print(f"Percobaan masuk setelah reset: {pengguna.percobaan_masuk}")