kota = {
    'Jakarta': {
        'negara': 'Indonesia',
        'populasi': '10 juta',
        'fakta': 'Ibukota negara dan pusat bisnis.',
        'julukan': 'kota metropolitan'
    },
    "Yogyakarta": {
        "negara": 'Indonesia',
        "populasi": '373ribu',
        "fakta": "Kota pelajar dan pusat budaya Jawa.",
        "julukan": "Kota Pelajar"
    },
    'Tokyo': {
        'negara': 'Jepang',
        'populasi': '14 juta',
        'fakta': 'Memiliki sistem kereta api tersibuk di dunia.',
        'julukan': 'kota tak pernah tidur'
    },
    'Paris': {
        'negara': 'Prancis',
        'populasi': '2,1 juta',
        'fakta': 'Terkenal dengan Menara Eiffel.',
        'julukan': 'City of Love'
    }
}

for nama_kota, info in kota.items():
    print(f"\n{nama_kota} ({info['julukan']}):")
    print(f"\tNegara: {info['country']}")
    print(f"\tPopulasi: {info['population']}")
    print(f"\tFakta: {info['fact']}")

# (Sama seperti 6-11, namun format cetakan diubah menjadi kapital atau digabungkan ke dalam string dinamis yang lebih kompleks)    
for nama_kota, info in kota.items():
    print(f"{nama_kota.upper()} terletak di {info['negara']} dengan populasi sekitar {info['populasi']}. Fakta unik: {info['fakta']}")