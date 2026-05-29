import locale

# Mengatur lokal ke Indonesia (Gunakan 'id_ID' untuk Windows/Linux/Mac)
try:
    locale.setlocale(locale.LC_ALL, 'id_ID')
except locale.Error:
    # Fallback jika 'id_ID' tidak didukung di sistem tertentu
    locale.setlocale(locale.LC_ALL, '')

hp_price = [
    {"Hp": "Iphone", "harga": 12000000},
    {"Hp": "Samsung", "harga": 5000000},
    {"Hp": "Oppo", "harga": 2000000},
    {"Hp": "Vivo", "harga": 2000000}
]

def display_menu():
    print("=" * 40)
    print(f"{' MENU UTAMA ':^40}")
    print("=" * 40)
    print(" 1. Lihat Seluruh Data")
    print(" 2. Tambah Data")
    print(" 3. Hapus Data")
    print(" 4. Ubah Harga")
    print(" 5. Hitung Rata-Rata Harga")
    print(" 6. Keluar")
    print("=" * 40)
        
def lihat_data():
    print("\n" + "-" * 40)
    print(f"{'DAFTAR HARGA GADGET':^40}")
    print("-" * 40)
    
    if not hp_price:
        print(f"{'⚠️  Maaf, tidak ada data untuk diproses!':^40}")
        print("-" * 40)
        return
    
    print(f"{'No.':<4} | {'Merk HP':<15} | {'Harga':<16}")
    print("-" * 40)
    
    index = 0
    for hp in hp_price:
        harga = hp["harga"]
        index += 1
        hasil = locale.currency(harga, grouping=True)
       
        print(f"{index:<3}  | {hp['Hp']:<15} | {hasil:<16}") 
    print("-" * 40)
    
def tambah_data(merk, harga):
    hp_price.append({
        "Hp": merk,
        "harga": harga
    })
    
def hapus_data(hapus):
    index = hapus - 1
    if index < 0 or index >= len(hp_price):
        print("\n❌ Nomor tidak valid! Pilih opsi yang tersedia.")
    else:
        terhapus = hp_price.pop(index)
        print(f"\n✅ Berhasil menghapus data HP: {terhapus['Hp']}")
    
def ubah_harga(index, harga_final):
    indexData = index - 1
    if harga_final <= 0:
        print("\n❌ Harga harus lebih dari 0! Perubahan dibatalkan.")
        return 
        
    hp_price[indexData]["harga"] = harga_final
    print(f"\n✅ Harga {hp_price[indexData]['Hp']} berhasil diubah!")

    indexData = index - 1
    if indexData < 0 or indexData >= len(hp_price):
        print("pilih opsi yang tersedia")
    else:
        if harga_final <= 0:
            print("Harga harus lebih dari 0!")
            return
        hp_price[index - 1]["harga"] = harga_final
    
def hitung_rata():
    harga_hp = 0
    for harga in hp_price:
        harga_hp += harga["harga"]
    rata = harga_hp / len(hp_price)
    hasil = locale.currency(rata, grouping=True)
    
    print("\n" + "=" * 40)
    print(f"{'HASIL ANALISIS HARGA':^40}")
    print("=" * 40)
    print(f" Rata-rata Harga HP : {hasil}")
    print("=" * 40)
        
def state(pilihan):
    if pilihan == "1":
        lihat_data()
        
    if pilihan == "2":
        print("\n--- TAMBAH DATA GADGET ---")
        try:
            hpMerk = input(" Masukkan nama merk HP : ")
            hargaHP = int(input(" Masukkan harga HP     : "))
            tambah_data(hpMerk, hargaHP)
            print(f"\n✅ Berhasil menambahkan {hpMerk} ke dalam data.")
        except ValueError:
            print("\n❌ Angka Tidak Valid! Harga hanya menerima input angka.")
            return
            
    if pilihan == "3":
        if not hp_price:
            print("\n❌ Tidak ada data yang bisa dihapus!")
            return
        try:
            lihat_data()
            dataRemove = int(input(" Masukkan nomor data yang ingin dihapus : "))
            hapus_data(dataRemove)
        except ValueError:
            print("\n❌ Input Salah! Hanya menerima angka nomor urut.")
            return

    if pilihan == "4":
        if not hp_price:
            print("\n❌ Tidak ada data yang bisa diubah!")
            return
        try:
            lihat_data()
            userIndex = int(input(" Pilih nomor data yang ingin diubah : "))
            
            if userIndex <= 0 or userIndex > len(hp_price):
                print("\n❌ Nomor data tidak ditemukan! Pilih opsi yang tersedia.")
                return 
            
            harga_edit = int(input(" Silahkan ubah harganya             : "))
            ubah_harga(userIndex, harga_edit)
        except ValueError:
            print("\n❌ Input Salah! Hanya menerima input angka.")
            return

    if pilihan == "5":
        if not hp_price:
            print("\n❌ Tidak ada data untuk dihitung rata-ratanya!")
            return
        hitung_rata()
    
input_list = ['1', '2', '3', '4', '5', '6']
        
def main():
    while True:
        print("\n" + "#" * 40)
        print(f"{'WELCOME TO GADGET-IN':^40}")
        print("#" * 40)
        
        display_menu()
        userChoice = input(" Silahkan pilih input yang tersedia : ")
        
        if userChoice in input_list:
            state(userChoice)
        else:
            print('\n❌ Pilihan salah! Silahkan pilih nomor input yang tersedia.')
        
        if userChoice == "6":
            print("\n" + "=" * 40)
            print(f"{'Program berhenti, Terima Kasih!':^40}")
            print("=" * 40 + "\n")
            break