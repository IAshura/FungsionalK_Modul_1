
def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir


def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai['uts'], nilai['uas']
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        'Mahasiswa1': {'uts': 80, 'uas': 95},
        'Mahasiswa2': {'uts': 75, 'uas': 90},
        'Mahasiswa3': {'uts': 80, 'uas': 80},
        'Mahasiswa4': {'uts': 90, 'uas': 85},
    }

    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
