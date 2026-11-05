angka_favorit = {
    'Andi': [7, 11],
    'Budi': [3, 5, 9],
    'Citra': [9],
    'Dewi': [12, 24],
    'Eko': [5, 10, 15]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama}:")
    for a in angka:
        print(f"- {a}")