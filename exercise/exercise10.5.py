from pathlib import Path

path = Path('guest_book.txt')
guest_names = []

print("Ketik 'keluar' jika sudah selesai.")
while True:
    name = input("Masukkan nama tamu: ")
    if name.lower() == 'keluar':
        break
    print(f"Halo, {name}! Nama Anda telah dicatat.")
    guest_names.append(name)

file_content = "\n".join(guest_names)
path.write_text(file_content)