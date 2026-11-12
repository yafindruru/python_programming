from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

# Versi ringkas untuk Latihan 10-1 (tanpa variabel 'lines')
for line in contents.splitlines():
    print(line)

# Versi ringkas untuk Latihan 10-2 (tanpa variabel 'lines' dan 'modified_line')
for line in contents.splitlines():
    print(line.replace('Python', 'C'))