data_mahasiswa = []

def validasi_nim():
    while True:
        nim = input("NIM: ").strip()
        if nim.isdigit() and not any(mhs['nim'] == nim for mhs in data_mahasiswa):
            return nim
        print("NIM hanya angka atau sudah terdaftar")

def validasi_nama():
    while True:
        nama = input("Nama: ").strip()
        if nama.replace(" ", "").isalpha():
            return nama
        print("Nama hanya huruf")


def validasi_angkatan():
    while True:
        angkatan = input("Angkatan: ").strip()
        # [Perbaikan: validasi angka dan panjang 4 digit (misal: 2024, 2023)
        if angkatan.isdigit() and (len(angkatan) == 4 or len(angkatan) == 2):
            return int(angkatan)
        print("Berisi angka saja! (contoh: 2024 atau 24)")

def validasi_jurusan():
    while True:
        jurusan = input("Jurusan: ").strip()
        if jurusan.replace(" ", "").isalpha():
            return jurusan
        print("Masukan Jurusan yang Valid")









