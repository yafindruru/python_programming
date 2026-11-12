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


restoran = Restoran("Warung Sedap", "Jawa")

# Cetak nilai awal, lalu ubah nilainya langsung dan cetak lagi
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")
restoran.jumlah_dilayani = 12
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")

# Lewat method atur_jumlah_dilayani()
restoran.atur_jumlah_dilayani(20)
print(f"Setelah diatur: {restoran.jumlah_dilayani}")

# Lewat method tambah_jumlah_dilayani(), misal pelanggan dalam satu hari
restoran.tambah_jumlah_dilayani(35)
print(f"Setelah ditambah 35: {restoran.jumlah_dilayani}")