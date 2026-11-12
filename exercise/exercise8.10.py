pesan_pendek = ["Halo kawan!", "Apa kabar?", "Sedang belajar Python nih."]
pesan_terkirim = []

def kirim_pesan(daftar_pesan, daftar_terkirim):
    while daftar_pesan:
        pesan_saat_ini = daftar_pesan.pop(0)
        print(f"Mengirim pesan: {pesan_saat_ini}")
        daftar_terkirim.append(pesan_saat_ini)

kirim_pesan(pesan_pendek, pesan_terkirim)

print("\nDaftar pesan asli:", pesan_pendek)
print("Daftar terkirim:", pesan_terkirim)