bahasa_favorit = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

peserta_polling = ['jen', 'budi', 'sarah', 'andi', 'phil']

for orang in peserta_polling:
    if orang in bahasa_favorit.keys():
        print(f"Terima kasih telah mengikuti polling, {orang.title()}!")
    else:
        print(f"Halo {orang.title()}, silakan ikuti polling bahasa favorit kami.")