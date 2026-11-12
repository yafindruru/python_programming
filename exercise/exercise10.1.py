from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

# Cara 1: Membaca dan mencetak seluruh isi file sekaligus
print("--- Seluruh Isi File ---")
print(contents)

# Cara 2: Menyimpan baris ke dalam list lalu melakukan perulangan (loop)
print("\n--- Per Baris Menggunakan List ---")
lines = contents.splitlines()
for line in lines:
    print(line)