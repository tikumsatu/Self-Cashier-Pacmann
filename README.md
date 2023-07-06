# Self-Cashier-Pacmann
![alt text](https://github.com/tikumsatu/Self-Cashier-Pacmann/blob/main/dokumentasi/mesin%20kasir.jpg?raw=true)

## Background Project
Andi adalah seorang pemilik supermarket besar di salah satu kota di indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, harga item yang dibeli dan beberapa fitur lainnya. Setelah Andi melakukan riset, Andi memiliki masalah, yaitu Andi membutuhkan programmer untuk membuat aplikasi dengan fitur-fitur yang dibutuhkan agar konsep kasir self-service dapat berjalan dengan lancar.

## Feature Requirements
Aplikasi self service untuk cashier sederhana dibuat dengan menggunakan Phyton Programming.
Fitur-fitur yang dibutuhkan adalah:
1. Fitur untuk menambahkan nama item, jumlah item dan harga item (methode add_item)
2. Fitur untuk mengubah nama item yang sudah ditambahkan (method update_item_name)
3. Fitur untuk mengubah jumlah item yang sudah ditambahkan (method update_item_qty)
4. Fitur untuk mengubah harga item yang sudah ditambahkan (methode update_item_price)
5. Fitur untuk menghapus nama item, jumlah item dan harga item yang sudah ditambahkan (method delete_item)
6. Fitur untuk membatalkan transaksi, atau menghapus semua item yang sudah ditambahkan (method reset_transaction)
7. Fitur untuk memeriksa keranjang belanja dari item yang sudah ditambahkan (method check_order)
8. Fitur untuk menampilkan nilai total belanja, nilai diskon dan nilai total pembayaran (method total_price)

## Flowchart

## Class dan Function
1. class Transaksi():
   Merupakan class yang dibangun untuk aplikasi self kasir ini
   
2. def __init__(self):
   Merupakan sebuah constructor untuk class Transaksi().
   Terdapat sebuah dict yang digunakan untuk menyimpan data masukkan.
   
3. def add_item(self, nama_item, jumlah_item, harga_item):
   Merupakan sebuah method yang digunakan untuk menambahkan item ke dalam keranjang belanja yang disimpan dalam dict list_belanja.
   Method ini menggunakan 3 inputan yaitu nama_item yang bertype string, jumlah_item yang bertype integer dan harga_item yang bertype integer.
   Jika type data yang dimasukkan tidak sesuai maka akan muncul peringatan 'Input tidak valid, silahkan input kembali dengan benar'.
   Jika method dijalankan benar maka data akan disimpan dalam dict dan ditampilkan dalam bentuk tabel
   
4. def update_item_name(self, nama_item):
   Merupakan sebuah method yang digunakan untuk mengubah nama_item yang sudah ditambahkan ke dalam dict.
   Method ini menggunakan inputan nama_item yang bertype string. Jika input bukan string maka akan muncul 'Input nama item tidak valid, silahkan input kembali dengan type data String'.
   Kemudian method akan melakukan eksekusi inputan update_nama dan bertype string. Jika method ini berhasil di jalankan maka nama_item dalam dict akan diubah sesuai dengan update_nama.
   Selanjutnya akan ditampilkan dalam bentuk tabel.
   
5. def update_item_qty(self, nama_item):
   Merupakan sebuah method yang digunakan untuk mengubah jumlah_item yang sudah ditambahkan ke dalam dict.
   Method ini menggunakan inputan nama_item yang bertype string. Jika input bukan string maka akan muncul 'Input nama item tidak valid, silahkan input kembali dengan type data String'.
   Kemudian method akan melakukan eksekusi inputan update_jumlah dan bertype integer. Jika method ini berhasil di jalankan maka jumlah_item dalam dict akan diubah sesuai dengan update_jumlah.
   Method ini juga secara otomatis akan mengubah nilai dict['Total Harga'], yang merupakan perkalian antara jumlah_item dan harga_item.
   Selanjutnya akan ditampilkan dalam bentuk tabel.
   
6. def update_item_price(self, nama_item):
   Merupakan sebuah method yang digunakan untuk mengubah harga_item yang sudah ditambahkan ke dalam dict.
   Method ini menggunakan inputan nama_item yang bertype string. Jika input bukan string maka akan muncul 'Input nama item tidak valid, silahkan input kembali dengan type data String'.
   Kemudian method akan melakukan eksekusi inputan update_harga dan bertype integer. Jika method ini berhasil di jalankan maka harga_item dalam dict akan diubah sesuai dengan update_harga.
   Method ini juga secara otomatis akan mengubah nilai dict['Total Harga'], yang merupakan perkalian antara jumlah_item dan harga_item.
   Selanjutnya akan ditampilkan dalam bentuk tabel.

7. def delete_item(self, nama_item):
    Merupakan sebuah method yang digunakan untuk menghapus satu set belanja (nama_item, jumlah_item dan harga_item).
    Method ini menggunakan inputan nama_item yang bertype string. Jika input bukan string maka akan muncul 'Input nama item tidak valid, silahkan input kembali dengan type data String'.
    Jika method ini berhasil di jalankan maka untuk 1 baris belanja dengan nama_item sesuai inputan akan dihapus dari dict.
    Selanjutnya akan ditampilkan dalam bentuk tabel.
    
8. def reset_transaction(self):
    Merupakan method yang digunakan untuk membatalkan semua transaksi. Jika method ini dijalankan maka seluruh nilai values dalam dict akan dihapus.
    Dan tampilan dalam list_belanja akan kosong dan menyisakan ['key'] saja.
    
9. def check_order(self):
    Merupakan method yang digunakan untuk memeriksa keranjang belanja dari proses yang sudah dijalankan sebelumnya.
    Dengan method ini kondisi terakhir dict list_belanja akan ditampilkan dalam bentuk tabel.
    
10. def total_price(self):
    Merupakan sebuah method yang digunakan untuk menghitung total nilai belanja, diskon yang didapat, serta total pembayaran yang harus dilakukan.
    Dalam method ini ada ketentuan tambahan, yaitu:
    - Jika total belanja lebih besar dari 500.000 maka akan mendapatkan diskon sebesar 10% dari total belanja
    - Jika total belanja lebih besar dari 300.000 maka akan mendapatkan diskon sebesar 8% dari total belanja
    - Jika total belanja lebih besar dari 200.000 maka akan mendapatkan diskon sebesar 5% dari total belanja
    - Jika belanja kurang dari sama dengan 200.000 maka tidak mendapatkan diskon
