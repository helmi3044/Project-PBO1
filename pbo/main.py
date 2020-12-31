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
	silahkan pilih salah satu :
	1. Data Pembeli
	2. Data Pemilik
	3. Data Karyawan
	4. Daftar Menu
	5. Pesan
	6. Data Pesanan Hari ini
	7. Exit
	''')
	utama = int(input('masukkan pilihan : '))
	return utama

def tampilkanPilihan1():
	print('-----------------')
	print('''Pilih menu: 
	1. Tampilkan daftar Pembeli
	2. Tambah data Pembeli
	''')
	pilihan = input('Masukkan pilihan: ')
	if pilihan == '1':
		tampilkanDaftarcust()
	elif pilihan == '2':
		tambahDatacust()
	return pilihan

def tampilkanDaftarcust():
	global cust # memanfaatkan var global yg sdh didefinisikan diatas
	print('\nDaftar Pembeli:')
	daftarcust = cust.getDaftarPembeli() #menampung luaran dri func get
	for cust_row in daftarcust:
		print(cust_row)
	print('\n')

def tambahDatacust():
	global cust
	print('\nTambah data pembeli:') 
	Nama = input('masukkan nama : ')
	Alamat = input('masukkan alamat : ')
	NomorHP = input('masukkan nomor hp : ')
	cust.setDataPembeli(Nama, Alamat, NomorHP)
	print('\n')

def tampilkanPilihan2():
	print('-----------------')
	print('Pilih menu:')
	print('1. Tampilkan daftar Pemilik')
	print('2. Tambah data Pemilik')
	print('3. Cek pendapatan')
	pilihan2 = input('Masukkan pilihan: ')
	if pilihan2 == '1':
		tampilkanDaftarown()
	elif pilihan2 == '2':
		tambahDataown()
	elif pilihan2 == '3':
		cekpenghasilan()
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

def tampilkanPilihan3():
	print('-----------------')
	print('Pilih menu:')
	print('1. Tampilkan daftar Karyawan')
	print('2. Tambah data Karyawan')
	print('3. gaji Karyawan')
	pilihan3 = input('Masukkan pilihan: ')
	if pilihan3 == '1':
		tampilkanDaftaremp()
	elif pilihan3 == '2':
		tambahDataemp()
	elif pilihan3 == '3':
		fee()
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

def tampilkanPilihan4():
	print('-----------------')
	print('Pilih menu:')
	print('1. Tampilkan daftar menu')
	print('2. Tambah daftar menu')
	pilihan2 = input('Masukkan pilihan: ')
	if pilihan2 == '1':
		tampilkanDaftarmenu()
	elif pilihan2 == '2':
		tambahDatamenu()
	return pilihan2

def tampilkanDaftarmenu():
	global menulist
	print('\nDaftar Menu:')
	daftarmenu = menulist.getDaftarMenu()
	for menu_row in daftarmenu:
		print(menu_row)
	print('\n')

def tambahDatamenu():
	global menulist
	print('\nTambah daftar menu:')
	NamaMenu = input('Masukkan nama menu: ')
	Harga = input('Masukkan harga: ')
	menulist.setDataMenu(NamaMenu, Harga)
	print('\n')

def tampilkanPilihan5():
	print('-----------------')
	print('Pilih menu:')
	print('1. Pesan makanan')
	print('2. Total harga pesanan')
	pilihan2 = input('Masukkan pilihan: ')
	if pilihan2 == '1':
		tambahpesanan()
	elif pilihan2 == '2':
		totalharga()
	return pilihan2

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
		return tambahpesanan()
	elif lagi == 'tidak':
		return lagi()
	
def totalharga():
	global order
	print('\nHitung total harga pesanan:')
	bayar = order.total()
	print('total harga pesanan : ', bayar)

def tampilkanPilihan6():
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
		tampilkanPilihan4()
	elif utama == 5:
		tampilkanPilihan5()
	elif utama == 6:
		tampilkanPilihan6()
	elif utama == 7:
		break