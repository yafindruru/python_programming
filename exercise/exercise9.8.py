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


class HakAkses:
    def __init__(self):
        self.hak_akses = [
            "dapat menambah postingan",
            "dapat menghapus postingan",
            "dapat memblokir pengguna",
        ]

    def tampilkan_hak_akses(self):
        print("Hak akses yang dimiliki:")
        for hak in self.hak_akses:
            print(f"- {hak}")


class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, kota, pekerjaan):
        super().__init__(nama_depan, nama_belakang, umur, kota, pekerjaan)
        self.hak_akses = HakAkses()   # objek HakAkses sebagai atribut


admin = Admin("Dewi", "Lestari", 35, "Jakarta", "Administrator Sistem")
admin.hak_akses.tampilkan_hak_akses()