class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0

    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka. Silakan masuk!")

    def atur_jumlah_dilayani(self, jumlah):
        self.jumlah_dilayani = jumlah

    def tambah_jumlah_dilayani(self, tambahan):
        self.jumlah_dilayani += tambahan