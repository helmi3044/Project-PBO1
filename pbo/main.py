import sqlite3
import datamanager
import person
from menu import Menu
from pembeli import Pembeli
from pemilik import Pemilik
from karyawan import Karyawan
from pesanan import Pesanan

cust = Pembeli() # buat objek
own = Pemilik()
emp = Karyawan()
menulist = Menu()
order = Pesanan()
jalan = True # buat var diisi true

# beberapa method dan function
def beranda():
	print(''' SELAMAT DATANG DI DAPUR MAMA
	masuk sebagai? :
	1. Pembeli
	2. Pemilik
	3. Karyawan
	4. Exit
	''')
	utama = int(input('masukkan pilihan : '))
	return utama

def tampilkanPilihan1():
	print('-----------------')
	print('''catatan !! : Setiap mau pesan harus isi data pembeli dulu ya :)
	Pilih menu: 
	1. Tambah data Pembeli
	2. Daftar Menu
	3. Pesan Menu
	4. exit
	''')
	pilihan = input('Masukkan pilihan: ')
	if pilihan == '1':
		tambahDatacust()
		return tampilkanPilihan1()
	elif pilihan == '2':
		tampilkanDaftarmenu()
		return tampilkanPilihan1()
	elif pilihan == '3':
		tambahpesanan()
		return tampilkanPilihan1()
	elif pilihan == '4':
		return beranda
	return pilihan

def tambahDatacust():
	global cust
	print('\nTambah data pembeli:') 
	Nama = input('masukkan nama : ')
	Alamat = input('masukkan alamat : ')
	NomorHP = input('masukkan nomor hp : ')
	cust.setDataPembeli(Nama, Alamat, NomorHP)
	print('\n')

def tampilkanDaftarmenu():
	global menulist
	print('\nDaftar Menu:')
	daftarmenu = menulist.getDaftarMenu()
	for menu_row in daftarmenu:
		print(menu_row)
	print('\n')

def tambahpesanan():
	global order
	print('\nSilahkan Pesan Makanan:')
	NamaMenu = input('Masukkan nama menu: ')
	Harga = input('Masukkan harga: ')
	Quantity = input('Pesan berapa ? : ')
	order.setDataPesanan(NamaMenu, Harga, Quantity)
	print('\n')
	lagi = input('apakah mau tambah lagi? (ya/tidak) : ')
	if lagi == 'ya':
		totalharga()
		return tambahpesanan()
	elif lagi == 'tidak':
		totalharga()
	return lagi

def totalharga():
	global order
	print('\nHitung total harga pesanan:')
	bayar = order.total()
	print('total harga pesanan : ', bayar)

def tampilkanPilihan2():
	print('-----------------')
	print('''Pilih menu:
	1. Tampilkan daftar Pemilik
	2. Tambah data Pemilik
	3. Cek pendapatan
	4. Tampilkan daftar pembeli
	5. Tampilkan daftar Karyawan
	6. Gaji Karyawan
	7. Exit
	''')
	pilihan2 = input('Masukkan pilihan: ')
	if pilihan2 == '1':
		tampilkanDaftarown()
		return tampilkanPilihan2()
	elif pilihan2 == '2':
		tambahDataown()
		return tampilkanPilihan2()
	elif pilihan2 == '3':
		cekpenghasilan()
		return tampilkanPilihan2()
	elif pilihan2 == '4':
		tampilkanDaftarcust()
		return tampilkanPilihan2()
	elif pilihan2 == '5':
		tampilkanDaftaremp()
		return tampilkanPilihan2()
	elif pilihan2 == '6':
		fee()
		return tampilkanPilihan2()
	elif pilihan2 == '7':
		return beranda
	return pilihan2

def tampilkanDaftarown():
	global own
	print('\nPemilik:')
	daftarown = own.getDaftarPemilik()
	for own_row in daftarown:
		print(own_row)
	print('\n')

def tambahDataown():
	global own
	print('\nTambah data pemilik:')
	Nama = input('Masukkan nama: ')
	Alamat = input('Masukkan alamat: ')
	NomorHP = input('Masukkan nomor HP : ')
	own.setDataPemilik(Nama, Alamat, NomorHP)
	print('\n')

def cekpenghasilan():
	global own
	print('\n---------------')
	penghasilan = own.pendapatan()
	print('penghasilan anda sebesar : ', penghasilan)
	print('\n')

def tampilkanDaftarcust():
	global cust # memanfaatkan var global yg sdh didefinisikan diatas
	print('\nDaftar Pembeli:')
	daftarcust = cust.getDaftarPembeli() #menampung luaran dri func get
	for cust_row in daftarcust:
		print(cust_row)
	print('\n')

def tampilkanPilihan3():
	print('-----------------')
	print('''Pilih menu:
	1. Tampilkan daftar Karyawan
	2. Tambah data Karyawan
	3. gaji Karyawan
	4. Tambah Daftar Menu
	5. Daftar Pesanan
	6. Exit 
	''')
	pilihan3 = input('Masukkan pilihan: ')
	if pilihan3 == '1':
		tampilkanDaftaremp()
		return tampilkanPilihan3()
	elif pilihan3 == '2':
		tambahDataemp()
		return tampilkanPilihan3()
	elif pilihan3 == '3':
		fee()
		return tampilkanPilihan3()
	elif pilihan3 == '4':
		tambahDatamenu()
		return tampilkanPilihan3()
	elif pilihan3 == '5':
		daftarpesanan()
		return tampilkanPilihan3()
	elif pilihan3 == '6':
		return beranda
	return pilihan3

def tampilkanDaftaremp():
	global emp
	print('\nKaryawan:')
	daftaremp = emp.getDaftarKaryawan()
	for emp_row in daftaremp:
		print(emp_row)
	print('\n')

def tambahDataemp():
	global emp
	print('\nTambah data Karyawan')
	Nama = input('Masukkan nama : ')
	Alamat = input('Masukkan alamat : ')
	NomorHP = input('Masukkan nomor HP : ')
	JamKerja = input('Masukkan Jam Kerja : ')
	HargaPerjam = input('Masukkan Harga Per Jam : ')
	emp.setDataKaryawan (Nama, Alamat, NomorHP, JamKerja, HargaPerjam)
	print('\n')

def fee():
	global emp
	print('\nHitung gaji Karyawan:')
	hitung = emp.gaji()
	for fee_row in hitung:
		print(fee_row)
	print('\n')

def tambahDatamenu():
	global menulist
	print('\nTambah daftar menu:')
	NamaMenu = input('Masukkan nama menu: ')
	Harga = input('Masukkan harga: ')
	menulist.setDataMenu(NamaMenu, Harga)
	print('\n')

def daftarpesanan():
	print('-----------------')
	print('daftar pesanan :')
	global order
	daftarpesanan = order.getDaftarPesanan()
	for pesanan_row in daftarpesanan:
		print(pesanan_row)
	print('\n')

while jalan == True:
	utama = beranda()
	if utama == 1:
		tampilkanPilihan1()
	elif utama == 2:
		tampilkanPilihan2()
	elif utama == 3:
		tampilkanPilihan3()
	elif utama == 4:
		break
