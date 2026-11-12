from random import choice

kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
tiket_saya = (3, 7, "a", "e")


def tarik_empat_item():
    hasil = []
    while len(hasil) < 4:
        pilihan = choice(kumpulan)
        if pilihan not in hasil:
            hasil.append(pilihan)
    return hasil


jumlah_putaran = 0
menang = False

while not menang:
    undian = tarik_empat_item()
    jumlah_putaran += 1
    if set(undian) == set(tiket_saya):
        menang = True

print(f"Tiket saya: {tiket_saya}")
print(f"Undian yang menang: {undian}")
print(f"Butuh {jumlah_putaran} kali undian sampai tiket saya menang.")