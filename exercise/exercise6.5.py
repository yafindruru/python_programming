sungai = {
    "Nil": "Mesir",
    "Bengawan Solo": "Indonesia",
    "Amazon": "Brasil",
}
for nama_sungai, negara in sungai.items():
    print(f"Sungai {nama_sungai} mengalir melalui {negara}.")

print("\nNama sungai:")
for nama_sungai in sungai.keys():
    print(nama_sungai)

print("\nNama negara:")
for negara in sungai.values():
    print(negara) 