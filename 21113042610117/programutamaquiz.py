from modulquiz import (
    HARI_KERJA,
    hitung_jam_lembur,
    hitung_upah_lembur,
    format_rupiah,
)


def main():
    upah_perjam = int(input("Masukkan upah per jam (misal 20000): "))

    print("\nMasukkan waktu selesai lembur (format jam.menit, misal 18.15)")
    print("Jika tidak lembur, isi 16.30 atau lebih awal.\n")

    hasil = []
    total = 0
    for hari in HARI_KERJA:
        while True:
            try:
                waktu = input(f"{hari} : ")
                jam = hitung_jam_lembur(waktu)
                break
            except ValueError:
                print("  Format waktu salah, contoh yang benar: 18.15")
        upah = hitung_upah_lembur(jam, upah_perjam)
        total += upah
        hasil.append((hari, jam, upah))

    print("\n=== Rincian Upah Lembur ===")
    for hari, jam, upah in hasil:
        print(f"{hari:<6}: {jam} jam -> {format_rupiah(upah)}")
    print(f"{'Total':<6}: {format_rupiah(total)}")


if __name__ == "__main__":
    main()