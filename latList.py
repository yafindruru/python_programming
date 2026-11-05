import math

# Menerima input jumlah bilangan dari pengguna
n = int(input("Masukkan jumlah bilangan yang ingin diinput: "))
angka_list = []

# Menyimpan input bilangan ke dalam List menggunakan pengulangan
for i in range(n):
    nilai = float(input(f"Masukkan bilangan ke-{i+1}: "))
    angka_list.append(nilai)

# 1. Menghitung Total menggunakan iterasi
total = 0
jumlah_data = 0
for angka in angka_list:
    total += angka
    jumlah_data += 1

# 2. Menghitung Rata-rata
rata_rata = total / jumlah_data

# 3. Menghitung Standar Deviasi secara manual (rumus populasi)
jumlah_kuadrat_selisih = 0
for angka in angka_list:
    jumlah_kuadrat_selisih += (angka - rata_rata) ** 2

standar_deviasi = math.sqrt(jumlah_kuadrat_selisih / jumlah_data)

print("\n--- Hasil Perhitungan ---")
print(f"List Bilangan   : {angka_list}")
print(f"Total           : {total}")
print(f"Rata-rata       : {rata_rata}")
print(f"Standar Deviasi : {standar_deviasi:.2f}")

# Inisialisasi nilai minimum dan maksimum dari elemen pertama list
nilai_min = angka_list[0]
nilai_max = angka_list[0]

# Mencari nilai minimum dan maksimum menggunakan iterasi (perulangan)
for angka in angka_list:
    if angka < nilai_min:
        nilai_min = angka
    if angka > nilai_max:
        nilai_max = angka

print(f"Nilai Minimum   : {nilai_min}")
print(f"Nilai Maksimum  : {nilai_max}")

# Daftar pilihan topping yang tersedia
daftar_topping = ["Keju", "Coklat", "Kacang", "Pisang", "Kismis"]

print("=== MENU TOPPING MARTABAK MANIS ===")
for i, topping in enumerate(daftar_topping, 1):
    print(f"{i}. {topping}")

pesanan_topping = []
print("\nPilih topping yang Anda inginkan (ketik 'selesai' jika sudah cukup):")

while True:
    pilihan = input("Masukkan nama topping: ").capitalize()
    
    if pilihan == "Selesai":
        break
    elif pilihan in daftar_topping:
        if pilihan not in pesanan_topping:
            pesanan_topping.append(pilihan)
            print(f"-> {pilihan} berhasil ditambahkan.")
        else:
            print("-> Topping tersebut sudah ada di dalam pesanan Anda.")
    else:
        print("-> Maaf, topping tidak tersedia di menu.")

print("\n=== RINGKASAN PESANAN ANDA ===")
if len(pesanan_topping) > 0:
    print("Martabak Manis dengan kombinasi topping:")
    for topping in pesanan_topping:
        print(f" - {topping}")
    print(f"Total macam topping: {len(pesanan_topping)}")
else:
    print("Anda memesan Martabak Polos (tanpa topping).")
    
# Membuat list awal
buah = ["Apel", "Jeruk", "Mangga"]
print("List awal:", buah)

# 1. append(): Menambahkan elemen di akhir list
buah.append("Pisang")
print("Setelah append('Pisang'):", buah)

# 2. insert(): Menambahkan elemen pada indeks tertentu
buah.insert(1, "Anggur")
print("Setelah insert(1, 'Anggur'):", buah)

# 3. remove(): Menghapus elemen berdasarkan nama nilainya
buah.remove("Jeruk")
print("Setelah remove('Jeruk'):", buah)

# 4. pop(): Menghapus dan mengembalikan elemen berdasarkan indeks (default terakhir)
buah_terakhir = buah.pop()
print(f"Setelah pop() [menghapus {buah_terakhir}]:", buah)

# 5. sort(): Mengurutkan elemen list secara ascending (alfabetis)
buah.sort()
print("Setelah sort():", buah)

# 6. reverse(): Membalikkan urutan elemen di dalam list
buah.reverse()
print("Setelah reverse():", buah)

# 7. len(): Mengetahui jumlah elemen (panjang) list
print("Jumlah elemen dalam list:", len(buah))