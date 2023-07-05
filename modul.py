from tabulate import tabulate

class Transaksi():
  """
  Sebuah class dengan nama Transaksi untuk self-cashier
  """

  def __init__(self):
    """
    Sebuah constructor untuk class Transaksi
    """

    self.list_belanja = {'Nama Item': [], 'Jumlah Item': [], 'Harga Item': [], 'Total Harga': []}
    """
    Sebuach dict yang digunakan untuk menyimpan daftar belanja dengan menggunakan keys ['Nama Item'], ['Jumlah Item'], ['Harga Item'], dan ['Total Harga']
    """

  def add_item(self, nama_item, jumlah_item, harga_item):
    """
    Sebuah method yang digunakan untuk menambahkan item ke dalam list_belanja.

    Attributes:
    -----------
    nama_item: str
        akan ditambahkan ke dalam list_belanja dengan keys ['Nama Item']
    jumlah_item: int
        akan ditambahkan ke dalam list_belanja dengan keys ['Jumlah Item']
    harga_item: int
        akan ditambahkan ke dalam list_belanja dengan keys ['Harga Item']
    list_belanja dengan keys ['Total Harga']
        akan ditambahkan nilai dari perkalian antara jumlah_item dan harga_item
    -----------

    Setiap selesai melakukan add_item, data dict list_belanja yang terupdate akan di tampilkan dalam bentuk tabel
    """

    if isinstance(nama_item, str) and isinstance(jumlah_item, int) and isinstance(harga_item, int):
      self.list_belanja['Nama Item'].append(nama_item.lower())
      self.list_belanja['Jumlah Item'].append(jumlah_item)
      self.list_belanja['Harga Item'].append(harga_item)
      self.list_belanja['Total Harga'].append(jumlah_item * harga_item)
      print('\nDaftar belanja anda: ')
      print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
    else:
      print('Input tidak valid, silahkan input kembali dengan benar')

  def update_item_name(self, nama_item):
    """
    Sebuah method yang digunakan untuk melakukan update/revisi nama item yang sudah ada di dalam dict list_belanja

    Attributes :
    ------------
    nama_item: str
        yang berisi nama_item yang akan diupdate dalam dict list_belanja
    update_nama: str
        digunakan untuk mengganti nama_item yang sudah ada sebelumnya di dalam dict list_belanja
    edit_nama
        menyimpan lokasi/posisi index dari nama_item yang akan diupdate

    Setiap selesai melakukan update_item_name, data dict list_belanja yang terupdate akan ditampilkan dalam bentuk tabel
    """
    if isinstance(nama_item, str):
      if nama_item.lower() in self.list_belanja.get('Nama Item'):
        update_nama = input('Masukkan nama item baru: ').lower()
        if isinstance(update_nama, str):
          edit_nama = self.list_belanja['Nama Item'].index(nama_item.lower())
          self.list_belanja['Nama Item'][edit_nama] = update_nama
          print('Nama Item berhasil diubah')
          print('\nDaftar belanja anda: ')
          print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
        else:
          print('Update nama yang anda masukkan tidak valid')
      else:
        print('Item tidak ditemukan dalam daftar belanja anda')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
    else:
        print('Input nama item tidak valid, silahkan input kembali dengan type data String')

  def update_item_qty(self, nama_item):
    """
    Sebuah method yang digunakan untuk melakukan update/revisi jumlah item yang sudah ada dalam dict list_belanja

    Attributes :
    ------------
    nama_item: str
        yang berisi nama_item yang akan diupdate jumlah itemnya dalam dict list_belanja
    update_jumlah: int
        digunakan untuk mengganti jumlah_item yang sudah ada sebelumnya di dalam dict list_belanja
    edit_jumlah
        menyimpan lokasi/posisi index dari nama_item yang akan diupdate

    Setiap selesai melakukan update_item_qty, data dict list_belanja yang terupdate akan ditampilkan dalam bentuk tabel
    """
    if isinstance(nama_item, str):
      if nama_item.lower() in self.list_belanja.get('Nama Item'):
        update_jumlah = int(input('Masukkan jumlah item baru: '))
        edit_jumlah = self.list_belanja['Nama Item'].index(nama_item.lower())
        self.list_belanja['Jumlah Item'][edit_jumlah] = update_jumlah
        self.list_belanja['Total Harga'][edit_jumlah] = update_jumlah * self.list_belanja['Harga Item'][edit_jumlah]
        print('Jumlah Item berhasil diubah')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
      else:
        print('Item tidak ditemukan dalam daftar belanja anda')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
    else:
      print('Input nama item tidak valid, silahkan input kembali dengan type data String')

  def update_item_price(self, nama_item):
    """
    Sebuah method yang digunakan untuk melakukan update/revisi harga item yang sudah ada dalam dict list_belanja

    Attributes:
    -----------
    nama_item: str
        yang berisi nama_item yang akan diupdate harga itemnya dalam dict list_belanja
    update_harga: int
        digunakan untuk mengganti harga_item yang sudah ada sebelumnya di dalam dict list_belanja
    edit_harga
        menyimpan lokasi/posisi index dari nama_item yang akan diupdate

    Setiap selesai melakukan update_item_price, data dict list_belanja yang terupdate akan ditampilkan dalam bentuk tabel
    """
    if isinstance(nama_item, str):
      if nama_item.lower() in self.list_belanja.get('Nama Item'):
        update_harga = int(input('Masukkan harga item baru: '))
        edit_harga = self.list_belanja['Nama Item'].index(nama_item.lower())
        self.list_belanja['Harga Item'][edit_harga] = update_harga
        self.list_belanja['Total Harga'][edit_harga] = update_harga * self.list_belanja['Jumlah Item'][edit_harga]
        print('Jumlah Item berhasil diubah')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
      else:
        print('Item tidak ditemukan dalam daftar belanja anda')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
    else:
      print('Input nama item tidak valid, silahkan input kembali dengan type data String')

  def delete_item(self, nama_item):
    """
    Sebuah method yang digunakan untuk menghapus nama_item beserta jumlah dan harga item dalam data dict list_belanja

    Attributes:
    -----------
    nama_item: str
        yang berisi nama_item yang akan dihapus dalam dict list_belanja
    del_item
        menyimpan lokasi/posisi index dari nama_item yang akan dihapus

    Setiap selesai melakukan delete_item, data dict list_belanja yang terupdate akan ditampilkan dalam bentuk tabel
    """
    if isinstance(nama_item, str):
      if nama_item.lower() in self.list_belanja.get('Nama Item'):
        del_item = self.list_belanja['Nama Item'].index(nama_item.lower())
        for key in list(self.list_belanja.keys()):
          del self.list_belanja[key][del_item]
        print('Item berhasil dibatalkan','\n')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
      else:
        print("Item tidak ditemukan dalam keranjang belanja anda",'\n')
        print('\nDaftar belanja anda: ')
        print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')
    else:
      print('Input nama item tidak valid, silahkan input kembali dengan type data String')

  def reset_transaction(self):
    """
    Sebuah method yang digunakan untuk membatalkan seluruh transaksi, seluruh data values dalam dict list_belanja akan dihapus
    """
    for key in self.list_belanja:
      del self.list_belanja[key][:]
    print('Seluruh transaksi dibatalkan','\n')
    print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')

  def check_order(self):
    """
    Sebuah method yang digunakan untuk memeriksa keranjang belanja yang sudah masuk dalam data dict list_belanja
    """
    print('\nDaftar belanja anda: ')
    print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')

  def total_price(self):
    """
    Sebuah method yang digunakan untuk menghitung total belanja, diskon yang didapatkan dan total yang harus dibayarkan

    Attributes:
    diskon
        menampilkan besaran diskon yang didapatkan dalam persen
    disc
        menampilkan hasil perhitungan diskon dan total harga belanja
    pay
        menampilkan jumlah yang harus dibayar setelah dikurangi dengan diskon
    """
    if sum(self.list_belanja['Total Harga']) > 500_000:
      diskon = "Selamat anda mendapatkan diskon 10 %"
      disc = 0.1 * sum(self.list_belanja['Total Harga'])
      pay = 0.9 * sum(self.list_belanja['Total Harga'])
    elif sum(self.list_belanja['Total Harga']) > 300_000:
      diskon = "Selamat anda mendapatkan diskon 8 %"
      disc = 0.08 * sum(self.list_belanja['Total Harga'])
      pay = 0.92 * sum(self.list_belanja['Total Harga'])
    elif sum(self.list_belanja['Total Harga']) > 200_000:
      diskon = "Selamat anda mendapatkan diskon 5 %"
      disc = 0.05 * sum(self.list_belanja['Total Harga'])
      pay = 0.95 * sum(self.list_belanja['Total Harga'])
    else:
      diskon = "Mohon maaf anda tidak mendapatkan diskon"
      disc = 0
      pay = sum(self.list_belanja['Total Harga'])

    print('\nDaftar belanja anda: ')
    print(tabulate(self.list_belanja, headers = self.list_belanja.keys()),'\n')

    print('*' * 55)

    print('Total belanja anda : Rp ', sum(self.list_belanja['Total Harga']))
    print(diskon, 'total diskon belanja anda: Rp ', disc)
    print('Total tagihan belanja anda : Rp  ', pay)
