#module geometri
def luasKotak (panjang, lebar):
    luaskotak = panjang*lebar
    return luaskotak

def luasLingkaran (jari_jari):
    luas = (22/7) * jari_jari * jari_jari 
    return luas
    
def volumeTabung (luasLingkaran, tinggi):
    volume = luasLingkaran*tinggi
    return volume

#fungsi utama main dan pengecekan name
def main():
    # "isi utama program"
    print("isi uatama")
    jari_jari = 7
    tinggi = 10
    
    luas_alas = luasLingkaran(jari_jari)
    # volume_tabung = volumeTabung(luas_lingkaran, tinggi)
    volume_tabung = volumeTabung(luas_alas, tinggi)
    
    print("R:", jari_jari, "dan t:", tinggi, "valume tabung:", volume_tabung)
    
print (__name__)

if __name__ == "_main_":
    main()