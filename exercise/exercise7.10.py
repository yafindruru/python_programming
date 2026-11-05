respons_liburan = {}
polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    
    respons_liburan[nama] = tempat
    
    lanjut = input("Apakah ada orang lain yang ingin merespons? (ya/tidak) ")
    if lanjut.lower() == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling ---")
for nama, tempat in respons_liburan.items():
    print(f"{nama.title()} ingin pergi ke {tempat.title()}.")
    
hasil_poll = {}
aktif = True
while aktif:
    nama = input("\nNama Anda? ")
    tempat = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda pergi? ")
    hasil_poll[nama] = tempat
    lagi = input("Ada orang lain yang mau ikut? (ya/tidak) ")
    if lagi == 'tidak':
        aktif = False
print("\n--- Hasil Poll ---")
for nama, tempat in hasil_poll.items():
    print(f"{nama} ingin pergi ke {tempat}.")