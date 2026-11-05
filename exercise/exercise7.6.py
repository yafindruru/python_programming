# 1. Variabel aktif
aktif = True
while aktif:
    topping = input("Masukkan topping (ketik 'keluar' untuk batal): ")
    if topping == 'keluar':
        aktif = False
    else:
        print(f"Menambahkan {topping}")

# 2. Break
while True:
    topping = input("Masukkan topping (ketik 'keluar' untuk batal): ")
    if topping == 'keluar':
        break
    print(f"Menambahkan {topping}")

# 3. Conditional Test
topping = ""
while topping != 'keluar':
    topping = input("Masukkan topping (ketik 'keluar' untuk batal): ")
    if topping != 'keluar':
        print(f"Menambahkan {topping}")