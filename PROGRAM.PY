# Program Manajemen Data Mahasiswa
# Menggunakan semua materi yang telah dipelajari

# ==================== FUNGSI UTAMA ====================

def tampilkan_menu():
    """Menampilkan menu utama program"""
    print("\n" + "="*50)
    print("     SISTEM MANAJEMEN DATA MAHASISWA")
    print("="*50)
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Semua Data")
    print("3. Edit Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Cari Data Mahasiswa")
    print("6. Filter Data Berdasarkan IPK")
    print("7. Simpan Data ke File")
    print("8. Muat Data dari File")
    print("9. Tampilkan Statistik")
    print("0. Keluar")
    print("-"*50)
    return input("Pilih menu (0-9): ")

