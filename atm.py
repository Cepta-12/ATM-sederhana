
# PROGRAM ATM DENGAN PIN BUATAN SENDIRI

# FUNGSI FORMAT RUPIAH
def rupiah(angka):
    return "Rp" + format(angka, ",").replace(",", ".")

saldo = 1000000

print("==============================")
print("       SELAMAT DATANG")
print("          ATM BANK")
print("==============================")

# MEMBUAT PIN
print("\n=== BUAT PIN ATM ===")

while True:
    pin_baru = input("Buat PIN baru (4 angka): ")

    if len(pin_baru) == 4 and pin_baru.isdigit():
        konfirmasi_pin = input("Masukkan ulang PIN: ")

        if pin_baru == konfirmasi_pin:
            print("PIN berhasil dibuat!")
            break
        else:
            print("PIN tidak cocok! Silakan ulangi.")
    else:
        print("PIN harus terdiri dari 4 angka!")

# LOGIN ATM
print("\n=== LOGIN ATM ===")

pin = input("Masukkan PIN Anda: ")

if pin == pin_baru:

    print("\nLogin berhasil!")

    while True:
        print("\n==============================")
        print("          MENU ATM")
        print("==============================")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")
        print("==============================")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            print("Saldo Anda:", rupiah(saldo))

        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah penarikan: Rp"))

            if jumlah > 0 and jumlah <= saldo:
                saldo -= jumlah
                print("Penarikan berhasil!")
                print("Sisa saldo: Rp",rupiah(saldo))
            else:
                print("Saldo tidak cukup atau jumlah tidak valid!")

        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah setoran: Rp"))

            if jumlah > 0:
                saldo += jumlah
                print("Setoran berhasil!")
                print("Saldo sekarang: Rp", rupiah(saldo))
            else:
                print("Jumlah setoran tidak valid!")

        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM!")
            break

        else:
            print("Pilihan tidak tersedia!")

else:
    print("PIN salah! Akses ditolak.")
