
import geometri as geo # semua bisa dipakai
from geometri import luasLingkaran, volumeTabung

def main():
    print("Porgram menghitung volume tabung")
    jarijari = float(input("masukkan nilai jari-jari lingkaran :"))
    tinggi = float(input("masukkan tinggi tabung :"))
    print("volume tabung dengan jari jari", jarijari, "dan tinggi", tinggi, "adalah", volume)
    
if __name__ == "__main__":
    main()

jarijari = float(input("masukkan nilai jari-jari lingkaran :"))
tinggi = float(input("masukkan tinggi tabung :"))
# volume = geo.volumeTabung(geo.luasLingkaran(jarijari), tinggi)
volume = volumeTabung(luasLingkaran(jarijari), tinggi)
print("volume tabung dengan jari jari", jarijari, "dan tinggi", tinggi, "adalah", volume)
