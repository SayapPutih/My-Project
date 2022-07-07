import json

nama_file_json = "data.json"

with open(nama_file_json, 'r') as json_file: 
    data = json.load(json_file)

def kembali():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menu_utama()

def lihat_data(): #Melihat Data
    with open(nama_file_json) as File:
        reader = json.load(File)
        print("================================================================= Data Penghuni Kos =================================================================")
        print("Nama Kamar Nama Penghuni  Jenis Kelamin     Usia       Pekerjaan      Tanggal Masuk    Status Pembayaran  Kelengkapan Dokumen")
        
        for data in reader:
            print(f"{data['Nama Kamar']}         | {data['Nama Penghuni']}         | {data['Jenis Kelamin']}            | {data['Usia']}   | {data['Pekerjaan']}    | {data['Tanggal Masuk']}     | {data['Status Pembayaran']}             | {data['Kelengkapan Dokumen']} ")
    kembali()   

def tambah_data(): #Menambah Data 
    nama_file_json = "data.json"
    reader = list()
    with open(nama_file_json) as File:
        reader = json.load(File)
    item = dict()
    item ["Nama Kamar"] = input("Masukkan Nama Kamar: ")
    item ["Nama Penghuni"] = input("Masukkan Nama Penghuni: ")
    item ["Jenis Kelamin"] = input("Masukkan Jenis Kelamin: [L/P] ")
    item ["Usia"] = input("Masukkan Usia: ")
    item ["Pekerjaan"] = input("Masukkan Pekerjaan: ")
    item ["Tanggal Masuk"] = input("Tanggal Masuk: ")
    item ["Status Pembayaran"] = input("Apakah Penghuni Sudah Bayar? (sudah/belum)")
    item ["Kelengkapan Dokumen"] = input("kelengkapan Dokumen (FC KK / FC KTP) :")
    reader.append(item)
    with open(nama_file_json, 'w') as File:
        json.dump(reader, File, indent=4)
    print("Sukses!!!")
    kembali()

def hapus_data():  #Menghapus Data
    data_baru = [] 
    delete = input("Masukkan Nama Kamar Yang Akan Dihapus")
    with open(nama_file_json, 'r') as file: 
        baca = json.load(file) 
        for item in baca: 
            if item["Nama Kamar"] == delete:
                continue
            else:
                data_baru.append(item)

    with open(nama_file_json, 'w') as file: #mengakses file json menggunakan mode write
        json.dump(data_baru, file, indent = 4) #menambahkan data dari data_baru ke file json dengan indentasi 4
    kembali()

def menu_utama(): #Menu Utama Dari Program ini
    print("[1] Tampilkan Data Kos")
    print("[2] Tambahkan Data Kos")
    print("[3] Hapus Data Kos")
    print("[0] Exit")
    print("------------------------")
    pilihan_menu = input("Pilih menu> ")
    if(pilihan_menu == "1"):
        lihat_data()
    elif(pilihan_menu == "2"):
        tambah_data()
    elif(pilihan_menu == "3"):
        hapus_data()
    elif(pilihan_menu == "0"):
        exit()
    else:
        print(f"Menu {pilihan_menu} Tidak Ada")
        kembali()
menu_utama()
