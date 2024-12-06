import json

# Fungsi untuk menambahkan buku
def tambah_buku():
    judul = input("judul buku: ")
    penulis = input("penulis: ")
    tahun = input("tahun terbit: ")
    kategori = input("kategori: ")
    buku.append({
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "kategori": kategori,
        "status": "tersedia"
    })
    print(f"Buku '{judul}', dari penulis '{penulis}' berhasil ditambahkan ke perpustakaan Sigma!")
    simpan_data()

def hapus_buku():
    judul = input("judul buku yang ingin dihapus: ")
    for b in buku:
        if b['judul'].lower() == judul.lower():
            buku.remove(b)
            print(f"Buku '{judul}' berhasil dihapus dari perpustakaan!")
            simpan_data()
            return
    print("Buku tidak ditemukan dalam daftar!")

# Fungsi untuk cari buku ada apa engga
def cari_buku():
    kata_kunci = input("Cari judul/penulis/kategori: ").lower()
    
    hasil = [b for b in buku if kata_kunci in b['judul'].lower() or kata_kunci in b['penulis'].lower() or kata_kunci in b['kategori'].lower()]
    if hasil:
        print("Hasil pencarian:")
        for b in hasil:
            print(f"- {b['judul']} dari penulis {b['penulis']} [{b['status']}]")
    else:
        print("Buku yang dicari ga ada di daftar.")

# Fungsi untuk meminjam buku
def pinjam_buku():
    judul = input("judul buku yang ingin dipinjam: ")
    for b in buku:
        if b['judul'].lower() == judul.lower():
            if b['status'] == "tersedia":
                b['status'] = "dipinjam"
                print(f"Buku '{judul}' berhasil dipinjam!")
                simpan_data()
                return
            else:
                print(f"Buku '{judul}' sedang dipinjam.")
                return
    print("Buku tidak ada dalam daftar!")
# Fungsi untuk kembalikan buku yang dipinjam, jangan dibawa lari
def kembalikan_buku():
    judul = input("Input judul buku yang ingin dikembalikan: ")
    for b in buku:
        if b['judul'].lower() == judul.lower():
            if b['status'] == "dipinjam": 
                b['status'] = "tersedia"
                print(f"Buku '{judul}' berhasil dikembalikan, jangan lupa minjam lagi rizz!")
                simpan_data()
                return
            else:
                print(f"Buku '{judul}' sedang tidak dipinjam.")
                return
    print("Buku tidak ditemukan nich!")

# Fungsi menampilkan buku yang sedang dipinjam
def daftar_buku_dipinjam():
    hasil = [b for b in buku if b['status'] == "dipinjam"]
    if hasil:
        print("Daftar buku yang sedang dipinjam:")
        for b in hasil:
            print(f"- {b['judul']} oleh {b['penulis']} ({b['tahun']})")
    else:
        print("Tidak ada buku yang sedang dipinjam.")
# Fungsi menyimpan data ke file JSON
def simpan_data():
    with open('data_buku.json', 'w') as file:
        json.dump(buku, file, indent=4)

# Fungsi memuat data dari file JSON
def muat_data():
    try:
        with open('data_buku.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def menu():
    while True:
        print("\n==== SELAMAT DATANG DI PERPUSTAKAAN SIGMA ====")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Cari Buku berdasarkan judul/penulis/kategori")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Daftar buku yang sedang dipinjam")
        print("7. Simpan data")
        print("8. Keluar Menu")
        pilihan = input("Pilih menu dari 1-8: ")

        if pilihan == '1':
            tambah_buku()
        elif pilihan == '2':
            hapus_buku()
        elif pilihan == '3':
            cari_buku()
        elif pilihan == '4':
            pinjam_buku()
        elif pilihan == '5':
            kembalikan_buku()
        elif pilihan == '6':
            daftar_buku_dipinjam()
        elif pilihan == '7':
            simpan_data()
            print("Data sukses disimpan di file JSON.")
        elif pilihan == '8':
            print("Terima kasih telah berkunjung di perpustakaan sigma. See u >.<")
            break
        else:
            print("Input yang dimasukkan tidak valid!")

buku = muat_data()
menu()