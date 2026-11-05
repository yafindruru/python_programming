pesanan_sandwich = ['tuna', 'ayam', 'keju', 'sapi panggang']
sandwich_selesai = []

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya telah membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nDaftar sandwich yang sudah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich}")