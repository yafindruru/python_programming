from pengguna import Pengguna


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
        self.hak_akses = HakAkses()