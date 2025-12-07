data_mahasiswa = []

def validasi_nim():
    while True:
        nim = input("NIM: ").strip()
        if nim.isdigit() and not any(mhs['nim'] == nim for mhs in data_mahasiswa):
            return nim
        print("NIM hanya angka atau sudah terdaftar")





