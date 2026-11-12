class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka. Silakan masuk!")


restoran_satu = Restoran("Warung Sedap", "Jawa")
restoran_dua = Restoran("Pizza Nusantara", "Italia")
restoran_tiga = Restoran("Sushi Sakura", "Jepang")

restoran_satu.deskripsikan_restoran()
restoran_dua.deskripsikan_restoran()
restoran_tiga.deskripsikan_restoran()

class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka. Silakan masuk!")


restoran_satu = Restoran("Warung Sedap", "Jawa")
restoran_dua = Restoran("Pizza Nusantara", "Italia")
restoran_tiga = Restoran("Sushi Sakura", "Jepang")

restoran_satu.deskripsikan_restoran()
restoran_dua.deskripsikan_restoran()
restoran_tiga.deskripsikan_restoran()