#latihan fungsi A
import math

# 1. Konversi suhu Fahrenheit ke Celcius
def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9

# 2. Konversi suhu Celcius ke Fahrenheit
def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

# 3. Konversi suhu Fahrenheit ke Reamur
def fahrenheit_ke_reamur(f):
    return (f - 32) * 4/9

# 4. Konversi suhu Reamur ke Fahrenheit
def reamur_ke_fahrenheit(r):
    return (r * 9/4) + 32

# 5. Konversi suhu Celcius ke Reamur
def celcius_ke_reamur(c):
    return c * 4/5

# 6. Konversi suhu Reamur ke Celcius
def reamur_ke_celcius(r):
    return r * 5/4

# 7. Luas Lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# 8. Luas permukaan tabung
def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

# 9. Volume tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * (jari_jari ** 2) * tinggi


# --- CONTOH PEMANGGILAN BAGIAN A ---
print("--- Hasil Bagian A ---")
print(f"100 Fahrenheit = {fahrenheit_ke_celcius(100):.2f} Celcius")
print(f"37.38 Celcius = {celcius_ke_fahrenheit(37.38)}")
print(f"Luas Lingkaran (r=7) = {luas_lingkaran(7):.2f}")
print(f"Volume Tabung (r=7, t=10) = {volume_tabung(7, 10):.2f}")