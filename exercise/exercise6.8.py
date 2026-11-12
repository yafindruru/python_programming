pets = [
    {'jenis': 'kucing', 'pemilik': 'Ana'},
    {'jenis': 'anjing', 'pemilik': 'Budi'},
    {'jenis': 'kelinci', 'pemilik': 'Citra'},
]
for pet in pets:
    for kunci, nilai in pet.items():
        print(f"{kunci}: {nilai}")
    print()