pesan = "\nMasukkan topping pizza yang Anda inginkan:"
pesan += "\n(Ketik 'keluar' untuk menyelesaikan pesanan.) "

while True:
    topping = input(pesan)
    if topping.lower() == 'keluar':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")
        
while True:
        topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")
        if topping == 'quit':
            break
        print(f"Topping {topping} akan ditambahkan ke pizza Anda.")