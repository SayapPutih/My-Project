# SayapPutih Express merupakan sebuah perusahaan jasa pengiriman barang se-Indonesia dengan berbagai pelayanan

import os
import sys
import time
import getpass

def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.1)
print('='* 40)  
ketik(
'\n             SayapPutih Express               '
'\n    Jasa pengiriman barang  24 jam'
)
print('='*40)

def loginapp() :
    print('{0:^40}'.format('Silahkan Login dahulu   '))
    print('')
    print('1. login sebagai Customer \n'
    '2. Keluar \n')

    o = input('Pilih : ')
    if o == '1' :
        u = input('Username : ')
        p = getpass.getpass()
        print('')
        print('{0:^40}'.format('Selamat datang di SayapPutih Express'))
        print('{0:^40}'.format(u))
        user = input('Apakah anda akan mengirimkan barang? y/n :')
        inputan_barang()
        
    elif o == '2':
        exit()
            

def inputan_barang():
    print('''
              Lorena Exprees      
    ------------------------------------   
      Pengiriman Tercepat se-Indonesia

           1. Reguler  [3-5 hari]
           2. Express   [1-2 hari]
           3. keluar

    ------------------------------------
    ''')
    choose = int(input('Pilihan layanan (No) ='))
    jumlah_barang = int(input('Jumlah barang yang di kirim = '))
    kapasitas_muatan = int(input('Kapasitas Max muatan  : '))
    nama = []
    berat = []
    nilai = []
    masa_jenis = []
    data = []
    # value = nilai / berat
    for b in range(jumlah_barang) :
        nama_brg = input('Masukan NAMA barang: ')
        nama.append(nama_brg)
        berat_barang = int(input('Masukkan Berat satuan barang (Kg): '))
        berat.append(berat_barang)
        nilai_barang = int(input('Masukkan HARGA barang (Rp):'))
        nilai.append(nilai_barang)
        value = nilai_barang / berat_barang
        masa_jenis.append(value)
        dict_sementara = {'Nama':nama_brg, 'Berat':berat_barang, 'Harga':nilai_barang, 'Masa jenis':value}
        data.append(dict_sementara)
        os.system('cls')
        print('_' * 79)
        print('{0} {1:^4} {0} {2:^20} {0} {3:^15} {0} {4:^15} {0} {5:^10} {0}'.format('|', 'NO', 'NAMA BARANG', 'BERAT BARANG','HARGA BARANG', 'MASA JENIS'))
        for (no, j) in enumerate(data):
        
            print('{0} {1:>4} {0} {2:^20} {0} {3:^12} {4:>2} {0} {5:<2} {6:>12} {0} {7:10} {0}'.format('|', no + 1, j['Nama'], j['Berat'], 'kg', 'Rp', j['Harga'], j['Masa jenis']))
        print('~' * 79 )
        
    operasi_knapsack(data, kapasitas_muatan)
    return kapasitas_muatan
    return data

def operasi_knapsack(data, kapasitas_muatan):
    values = []
    cap = kapasitas_muatan
    brg_masuk = []

    for i in data:
        values.append(i['Harga'])
    values.sort() 
    values.reverse()
    print(values)

    for i in values:
        for j in data:
            if i == j['Harga']:
                if j['Berat'] <= cap:
                    brg_masuk.append(j)
                    cap -= j['Berat']
                else:
                    continue
    print(brg_masuk)
    


     
    
loginapp()