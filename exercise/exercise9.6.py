class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka. Silakan masuk!")


class KiosEsKrim(Restoran):
    def __init__(self, nama_restoran, jenis_masakan):
        super().__init__(nama_restoran, jenis_masakan)
        self.rasa = ["vanila", "cokelat", "stroberi", "alpukat"]

    def tampilkan_rasa(self):
        print(f"Rasa es krim di {self.nama_restoran}:")
        for rasa in self.rasa:
            print(f"- {rasa}")


kios = KiosEsKrim("Es Krim Ceria", "es krim")
kios.deskripsikan_restoran()
kios.tampilkan_rasa()