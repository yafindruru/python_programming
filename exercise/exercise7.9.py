pesanan_sandwich = ['pastrami', 'tuna', 'ayam', 'pastrami', 'keju', 'pastrami']
sandwich_selesai = []

print("Maaf, restoran kami kehabisan pastrami hari ini.\n")

while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya telah membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)