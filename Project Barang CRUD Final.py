loop = True
barang = []
harga = []
print("====================================")
print("=     Aplikasi Daftar Barang       =")
print("====================================")
print("=============== MENU ===============")
print("= 1. Cetak Informasi Daftar Barang =")
print("= 2. Tambahkan Data Barang         =")
print("= 3. Ubah Data Dalam Daftar Barang =")
print("= 4. Menghapus Data Barang         =")
print("= 5. Hitung Jumlah Jenis Barang    =")
print("= 6. Hitung Jumlah Total Barang    =")
print("= 7. Hitung Jumlah stock per Barang=")
print("= 8. Save Data                     =")
print("= 9. Load Data                     =")
print("= 10. Keluar (Exit)                =")
print("====================================")
while(loop):  
  try:           
    menu = int(input('Masukkan menu yang dipilih: '))
    if menu == 1:
      if len(barang)==0:
        print('Data Kosong')
      else:
        print(barang)
        print(harga)
        print("Total value barang adalah Rp. ", sum(harga), ",-" )
    elif menu == 2:
      tambah = (input('Masukkan nama barang: '))
      tambahharga = int(input('Masukkan harga barang: '))
      tambahnew = tambah.title()
      angka=['0','1','2','3','4','5','6','7','8','9']
      if(tambahnew[0] in angka):
        print('Data yang kamu masukkan salah')
      elif(tambahnew in barang):
        print('Data yang kamu masukkan sudah ada, tetap tambahkan? (Y/N): ')
        konfirm = input('Y/N: ').upper()
        if konfirm == 'Y':
          barang.append(tambahnew)
          harga.append(tambahharga)
          print('Data Tersimpan')
        elif konfirm == 'N':
          print('Data Tidak Tersimpan')
        else:
          print('Input salah hanya menerima Y/N')
      else:
        barang.append(tambahnew)
        harga.append(tambahharga)
        print('Data Tersimpan')
    elif menu == 3:
      ubah = str(input('Masukkan nama barang yang akan diganti: '))
      ubahnew = ubah.title()
      if(ubahnew in barang):
        barangbaru = input('Masukkan barang pengganti: ')
        hargabaru = int(input('Masukkan harga barang pengganti: '))
        barangbarunew = barangbaru.title()
        for i,item in enumerate(barang):
          if item == ubahnew:
            barang[i] = barangbarunew
            harga[i] = hargabaru
            print('Data telah diperbaharui')
      else:
        print('Data tidak ditemukan')
    elif menu == 4:
      hapus = input('Masukkan barang yang akan dihapus: ')
      hapusnew = hapus.title()
      if(hapusnew in barang):
        for i,item in enumerate(barang):
          if item == hapusnew:
            barang.remove(hapusnew)
            harga.remove(harga[i])
            print('Barang telah dihapus')
      else:
        print('Data tidak ditemukan')
    elif menu == 5:
      print('Jumlah jenis barang saat ini: ',len(set(barang)))
    elif menu == 6:
      print('Total barang saat ini:', len(barang))
    elif menu == 7:
      stock = input('Masukkan nama barang yang ingin dihitung stocknya')
      stocknew = stock.title()
      if(stocknew in barang):
        jmlstock = barang.count(stocknew)
        print('jumlah stock ',stocknew,'adalah: ',jmlstock)
      else:
        print('Data tidak ditemukan')
    elif menu == 8:
      import pickle
      with open('barang', 'wb') as f:
        pickle.dump(barang, f)
      with open('harga', 'wb') as p:
        pickle.dump(harga, p)
        print('Data berhasil tersimpan')
    elif menu == 9:
      import pickle
      with open('barang', 'rb') as f:
        barang = pickle.load(f)
      with open('harga', 'rb') as p:
        harga = pickle.load(p)
        print('Data loaded')
    elif menu == 10:
      print('Terima Kasih Telah Menggunakan Aplikasi ini')
      loop = False
    else:
      print('Menu yang kamu masukkan tidak tersedia')
  except:
    print('Data yang kamu masukkan salah')
  