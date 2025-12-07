data_mahasiswa = []

def validasi_npm():
    while True:
        npm = input("NPM: ").strip()
        if npm.isdigit() and not any(mhs['npm'] == npm for mhs in data_mahasiswa):
            return npm
        print("NPM hanya angka atau sudah terdaftar")
        
def validasi_nama():
    while True:
        nama = input("Nama: ").strip()
        if nama.replace(" ", "").isalpha(): 
            return nama
        print("Nama hanya huruf")


def validasi_angkatan():
    while True:
        angkatan = input("Angkatan: ").strip()
        # Perbaikan: validasi angka dan panjang 4 digit (misal: 2024, 2023)
        if angkatan.isdigit() and (len(angkatan) == 4 or len(angkatan) == 2):
            return int(angkatan)
        print("Berisi angka saja! (contoh: 2024 atau 24)")

def validasi_jurusan():
    while True:
        jurusan = input("Jurusan: ").strip()
        if jurusan.replace(" ", "").isalpha():
            return jurusan
        print("Masukkan Jurusan Yang Valid")
        
def tambah_mahasiswa():
    print("\n=== TAMBAH DATA ===")
    data_mahasiswa.append({
        'npm': validasi_npm(),
        'nama': validasi_nama(),
        'jurusan': validasi_jurusan(),
        'angkatan': validasi_angkatan()
    })
    print("Data berhasil ditambah!")

def tampilkan_semua():
    print("\n=== SEMUA DATA ===")
    if not data_mahasiswa:
        print("Data kosong.")
        return
    i = 1
    for mhs in data_mahasiswa:
        print(f"{i}. NPM: {mhs['npm']}")
        print(f"   Nama: {mhs['nama']}")
        print(f"   Jurusan: {mhs['jurusan']}")
        print(f"   Angkatan: {mhs['angkatan']}")
        print("-" * 20)
        i += 1

def cari_data():
    print("\n=== CARI DATA ===")
    keyword = input("Cari (NPM/Nama): ").lower()
    hasil = [mhs for mhs in data_mahasiswa if keyword in mhs['npm'] or keyword in mhs['nama'].lower()]
    if not hasil:
        print("Data tidak ditemukan.")
        return
    print(f"Ditemukan {len(hasil)} data:")
    i = 1
    for mhs in hasil:
        print(f"{i}. NPM: {mhs['npm']}, Nama: {mhs['nama']}")
        i += 1

def hapus_data():
    print("\n=== HAPUS DATA ===")
    npm_hapus = input("NPM yang dihapus: ")
    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i]['npm'] == npm_hapus:
            if input(f"Hapus {data_mahasiswa[i]['nama']}? (y/n): ").lower() == 'y':
                data_mahasiswa.pop(i)
                print("Data dihapus!")
            return
    print("NPM tidak ditemukan.")
    
def edit_data():
    print("\n=== EDIT DATA ===")
    npm_cari = input("NPM yang diedit: ")
    for mhs in data_mahasiswa:
        if mhs['npm'] == npm_cari:
            print(f"Data ditemukan: {mhs['nama']}")
            
            # Tampilkan menu edit
            print("\nPilih data yang akan diedit:")
            print("1. Nama")
            print("2. Jurusan")
            print("3. Angkatan")
            print("4. Semua data")
            print("5. Batal")
            
            pilihan_edit = input("Pilih (1-5): ")
            
            if pilihan_edit == '1':
                print(f"\nEdit Nama (saat ini: {mhs['nama']})")
                mhs['nama'] = validasi_nama()
                
            elif pilihan_edit == '2':
                print(f"\nEdit Jurusan (saat ini: {mhs['jurusan']})")
                mhs['jurusan'] = validasi_jurusan()
                
            elif pilihan_edit == '3':
                print(f"\nEdit Angkatan (saat ini: {mhs['angkatan']})")
                mhs['angkatan'] = validasi_angkatan()
                
            elif pilihan_edit == '4':
                print("\nEdit semua data:")
                mhs['nama'] = validasi_nama()
                mhs['jurusan'] = validasi_jurusan()
                mhs['angkatan'] = validasi_angkatan()
                
            elif pilihan_edit == '5':
                print("Edit data dibatalkan.")
                return
            else:
                print("Pilihan tidak valid.")
                return
                
            print("Data berhasil diupdate!")
            return
            
    print("NPM tidak ditemukan.")


def simpan_ke_file():
    print("\n=== SIMPAN DATA KE FILE ===")
    if not data_mahasiswa:
        print("Tidak ada data untuk disimpan!")
        return

    nama_file = input("Masukkan nama file: ").strip()
    if not nama_file.endswith('.txt'):
        nama_file += '.txt'

    # Asumsi: direktori dapat ditulis dan tidak ada error
    with open(nama_file, 'w', encoding='utf-8') as file:
        file.write("="*50 + "\nDATA MAHASISWA\n" + "="*50 + "\n\n")
        i = 1
        for mhs in data_mahasiswa:
            file.write(f"DATA KE-{i}\nNPM: {mhs['npm']}\nNama: {mhs['nama']}\n")
            file.write(f"Jurusan: {mhs['jurusan']}\nAngkatan: {mhs['angkatan']}\n" + "-"*30 + "\n\n")
            i += 1
        file.write(f"\nTotal Data: {len(data_mahasiswa)} mahasiswa\n")
        file.write(f"Tanggal: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"Data berhasil disimpan ke '{nama_file}'!")

def main():
    menu = {
        '1': tambah_mahasiswa,
        '2': tampilkan_semua,
        '3': cari_data,
        '4': edit_data,
        '5': hapus_data,
        '6': simpan_ke_file
    }
    
    while True:
        print("\n" + "="*40 + "\nPROGRAM MANAJEMEN DATA MAHASISWA\n" + "="*40)
        for i in range(1, 7): 
            menu_text = [
                "Tambah Data", "Tampilkan Semua", "Cari Data", 
                "Edit Data", "Hapus Data", "Simpan ke File"
            ]
            print(f"{i}. {menu_text[i-1]}")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '0':
            if data_mahasiswa and input("Simpan data sebelum keluar? (y/n): ").lower() == 'y':
                simpan_ke_file()
            print("Program selesai.")
            break
        menu.get(pilihan, lambda: print("Pilihan tidak valid."))()

main()
