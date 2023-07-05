# Membuat id transaksi
id_transaksi = int(input('Masukan nomor ID anda: '))
message = f'Welcome to Super Cashire ID Pelanggan {id_transaksi}'

# Mencetak pesan selamat datang
print('*' * len(message))
print(message)
print('*' * len(message))

confirm1 = input('Apakah anda akan bertransaksi? (y/n) : ')
while confirm1 == "y":
  print('\nKetik 1 untuk add item. \nKetik 2 untuk delete item. \nKetik 3 untuk edit item. \nKetik 0 untuk membatalkan belanja')
  print('*' * 35, '\n')
  belanja = input('Masukkan pilihan anda: ')
  if belanja == "1":
    nama_item = input('Masukkan nama item: ')
    jumlah_item = int(input('Masukkan jumlah item: '))
    harga_item = int(input('Masukkan harga item: '))
    
