glosarium = {
    'variabel': 'Tempat untuk menyimpan nilai data.',
    'list': 'Kumpulan item yang berurutan dan dapat diubah.',
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value).',
    'string': 'Serangkaian karakter teks.',
    'boolean': 'Tipe data yang hanya memiliki nilai True atau False.',
    'set': 'Kumpulan item tidak terurut dan unik.',
    'tuple': 'Kumpulan item berurutan yang tidak dapat diubah (immutable).',
    'loop': 'Blok kode yang dijalankan berulang kali.',
    'fungsi': 'Blok kode yang dapat digunakan kembali untuk tugas tertentu.',
    'integer': 'Tipe data untuk bilangan bulat.'
}

for kata, arti in glosarium.items():
    print(f"{kata.title()}:\n  {arti}\n")
    
glosarium = {
    "string": "Serangkaian karakter yang diapit tanda kutip.",
    "list": "Kumpulan item yang tersusun dalam urutan tertentu.",
    "integer": "Bilangan bulat, tanpa bagian desimal.",
    "float": "Bilangan desimal, seperti 3,14.",
    "comment": "Catatan di dalam kode yang tidak dijalankan Python.",
    "loop": "Perulangan yang menjalankan blok kode berkali-kali.",
    "dictionary": "Kumpulan pasangan kunci-nilai.",
    "tuple": "List yang tidak bisa diubah setelah dibuat.",
    "boolean": "Nilai kebenaran, True atau False.",
    "variable": "Nama yang merujuk pada suatu nilai.",
}
for kata, arti in glosarium.items():
    print(f"{kata}:\n\t{arti}\n") 