#Membuat dict penyimpanan
list_belanja = {'Nama Item': [], 'Jumlah Item': [], 'Harga Item': [], 'Total Harga': []}

# Membuat id transaksi
id_transaksi = int(input('Masukan nomor ID anda: '))
message = f'Welcome to Super Cashire ID Pelanggan {id_transaksi}'

# Mencetak pesan selamat datang
print('*' * len(message))
print(message)
print('*' * len(message))

# Mencetak perintah1
user_transaksi = Transaksi()
confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')
while confirm1 == "y":
  print('\nKetik 1 untuk add item. \nKetik 2 untuk delete item. \nKetik 3 untuk edit item. \nKetik 4 untuk cek order. \nKetik 0 untuk membatalkan belanja')
  print('*' * 35, '\n')
  belanja = input('Masukkan pilihan anda: ')
  if belanja == "1":
    nama_item = input('Masukkan nama item: ')
    jumlah_item = int(input('Masukkan jumlah item: '))
    harga_item = int(input('Masukkan harga item: '))
    user_transaksi.add_item(nama_item, jumlah_item, harga_item)
    confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

  elif belanja == "2":
    nama_item = input('Masukkan nama item yang akan dibatalkan: ')
    user_transaksi.delete_item(nama_item)
    confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

  elif belanja == "3":
    print('\nKetik "nama" untuk edit nama item. \nKetik "jumlah" untuk edit jumlah item. \nKetik "harga" untuk edit harga item.')
    print('*' * 35, '\n')
    masukan = input("Masukkan pilihan anda: ").lower()
    if masukan == "nama":
      nama_item = input('Masukkan nama item yang akan diubah: ')
      user_transaksi.update_item_name(nama_item)
      confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

    elif masukan == "jumlah":
      nama_item = input('Masukkan nama item yang akan diubah jumlahnya: ')
      user_transaksi.update_item_qty(nama_item)
      confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

    elif masukan == "harga":
      nama_item = input('Masukkan nama item yang akan diubah harganya: ')
      user_transaksi.update_item_price(nama_item)
      confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

  elif belanja == "4":
    user_transaksi.check_order()
    confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

  elif belanja == "0":
    user_transaksi.reset_transaction()
    confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')

else:
  user_transaksi.total_price()
    
