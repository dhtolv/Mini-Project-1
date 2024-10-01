# Login Sederhana Menggunakan Nama dan NIM
nama = input("Masukkan Nama Anda: ")

# Memasukkan NIM dan Wajib Menggunakan Angka
while True:
    try:
        print("------- Masukkan Dengan Angka -------")
        NIM = int(input("Masukkan NIM anda: "))
        print(f"Selamat Datang {nama} dengan NIM {NIM}!")
        break
    except ValueError:
        print("Maaf! NIM anda salah")

# Input Data
while True: 
    harga_barang = int(input("Masukkan Harga 1 Barang: "))
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    total = harga_barang*jumlah_barang
    total_diskon = total-25/100*total
    
    if total >= 250000:
        total = total-25/100*total
        print("Anda Mendapatkan Diskon Sebesar 25%")
        print("Jumlah Yang Harus Dibayarkan:", total_diskon)
    else:
        print("Diskon Tidak Tersedia")
        print("Jumlah Yang Harus Dibayarkan: ", total)

    Memilih = input("Apakah Anda Ingin Menghitung Ulang Harga Barang? (b/t): ")
    if Memilih.lower()!= 'b':
        print("Terimkasih Sudah Datang!")
        break