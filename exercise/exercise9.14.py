from random import choice

kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")

pemenang = []
while len(pemenang) < 4:
    pilihan = choice(kumpulan)
    if pilihan not in pemenang:
        pemenang.append(pilihan)

print("Tiket yang cocok dengan 4 angka/huruf berikut memenangkan hadiah:")
for item in pemenang:
    print(item)