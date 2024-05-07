# Inisialisasi daftar belanjaan
daftar_belanjaan = []

# Fungsi untuk menambahkan item ke daftar belanjaan
# Putra Strata Tandika Setyawan (2311104050)
def tambah_item(items):
    new_items = items.split(",")  # Pisahkan item yang dimasukkan dengan koma
    for item in new_items:
        item = item.strip()  # Hilangkan spasi di awal dan akhir item
        daftar_belanjaan.append(item)
        print(f"{item} telah ditambahkan ke daftar belanjaan.")

# Fungsi untuk mencari item dalam daftar belanjaan
# Aulia Jasifa BR Ginting (2311104060)
def cari_item(item):
    if item in daftar_belanjaan:
        print(f"{item} ada dalam daftar belanjaan.")
    else:
        print(f"{item} tidak ada dalam daftar belanjaan.")

# Fungsi untuk menghapus item dari daftar belanjaan
# Alya Rabani (2311104076)
def hapus_item(item):
    if item in daftar_belanjaan:
        daftar_belanjaan.remove(item)
        print(f"{item} telah dihapus dari daftar belanjaan.")
    else:
        print(f"{item} tidak ada dalam daftar belanjaan.")

# Fungsi untuk menghapus semua item dari daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def hapus_semua_item():
    daftar_belanjaan.clear()
    print("Semua item telah dihapus dari daftar belanjaan.")

# Fungsi untuk menampilkan daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def tampilkan_daftar():
    if not daftar_belanjaan:
        print("Daftar belanjaan kosong.")
    else:
        print("Daftar Belanjaan:")
        for item in daftar_belanjaan:
            print("-", item)

# Fungsi untuk menyortir daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def sortir_belanjaan():
    daftar_belanjaan.sort()
    print("daftar belanjaan telah di urutkan")

#Dimastian Aji Wibowo (2311104058)
# Fungsi untuk menghitung jumlah total item dalam daftar belanjaan
def hitung_jumlah_item():
    jumlah_item = len(daftar_belanjaan)
    print(f"Jumlah total item dalam daftar belanjaan adalah {jumlah_item}.")

# Fungsi utama
def main():
    while True:
        print("\nPilihan:")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Cari item")
        print("4. Tampilkan daftar belanjaan")
        print("5. Sortir daftar belanjaan")
        print("6. Hapus semua item dari daftar belanjaan")
        print("7. Hitung jumlah total item")
        print("8. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            items = input("Masukkan nama item (pisahkan dengan koma untuk menambahkan beberapa item sekaligus): ")
            tambah_item(items)
        elif pilihan == "2":
            item = input("Masukkan nama item yang ingin dihapus: ")
            hapus_item(item)
        elif pilihan == "3":
            item = input("Masukkan nama item yang ingin dicari: ")
            cari_item(item)
        elif pilihan == "4":
            tampilkan_daftar()
        elif pilihan == "5":
            sortir_daftar()
        elif pilihan == "6":
            hapus_semua_item()
        elif pilihan == "7":
            hitung_jumlah_item()
        elif pilihan == "8":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
