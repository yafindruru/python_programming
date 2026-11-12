glosarium = {
    'variabel': 'Tempat untuk menyimpan nilai data.',
    'list': 'Kumpulan item yang berurutan dan dapat diubah.',
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value).',
    'string': 'Serangkaian karakter teks.',
    'boolean': 'Tipe data yang hanya memiliki nilai True atau False.'
}

print(f"Variabel:\n  {glosarium['variabel']}\n")
print(f"List:\n  {glosarium['list']}\n")
print(f"Dictionary:\n  {glosarium['dictionary']}\n")
print(f"String:\n  {glosarium['string']}\n")
print(f"Boolean:\n  {glosarium['boolean']}\n")

glosarium = {
    'variable': 'tempat menyimpan nilai dengan sebuah nama.',
    'string': 'rangkaian karakter, ditulis di dalam tanda kutip.',
    'list': 'kumpulan item berurutan yang bisa diubah.',
    'loop': 'perulangan untuk menjalankan kode berkali-kali.',
    'comment': 'catatan dalam kode yang diabaikan oleh Python.',
    # 5 istilah tambahan (6-4)
    'tuple': 'kumpulan item berurutan yang tidak bisa diubah.',
    'dictionary': 'kumpulan pasangan kunci-nilai.',
    'function': 'blok kode yang bisa dipanggil berulang kali.',
    'boolean': 'tipe data bernilai True atau False.',
    'index': 'nomor posisi sebuah item di dalam list.',
}
for kata, arti in glosarium.items():
    print(f"{kata.title()}:\n\t{arti}\n")