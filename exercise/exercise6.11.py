cities = {
    'surakarta': {
        'country': 'Indonesia',
        'population': '520 ribu',
        'fact': 'dikenal juga dengan nama Solo, pusat budaya Jawa.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': '14 juta',
        'fact': 'salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': '2,1 juta',
        'fact': 'rumah bagi Menara Eiffel.',
    },
}
for kota, info in cities.items():
    print(f"\n{kota.title()}")
    print(f"  Negara   : {info['country']}")
    print(f"  Populasi : {info['population']}")
    print(f"  Fakta    : {info['fact']}")