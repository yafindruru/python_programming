favorite_places = {
    'Ana': ['Bali', 'Yogyakarta'],
    'Budi': ['Bromo'],
    'Citra': ['Raja Ampat', 'Bandung', 'Lombok'],
}
for nama, tempat in favorite_places.items():
    print(f"Tempat favorit {nama}:")
    for t in tempat:
        print(f"\t- {t}")