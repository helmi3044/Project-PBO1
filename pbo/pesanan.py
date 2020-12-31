import sqlite3
from datamanager import DataManager
from menu import Menu

# class pesanan merupakan turunan dari kelas menu, sehingga membawa method bawaan dari class menu dan class data manager
# ada 2 method yang hampir sama dgn menu (set atau memasukkan data) maka terjadi overloading (paramater/signature berbeda)
class Pesanan(Menu):
	def setDataPesanan(self, NamaMenu, Harga, Quantity):\
		# memanggil method bawaan parent class
		self.setDataMenu(NamaMenu, Harga)
		MenuId = self.getDataMenu(NamaMenu, Harga)
		self.query = 'INSERT INTO Pesanan (MenuId, Quantity) \
			values (\'%s\', \'%s\')' 
		self.query = self.query % (MenuId[0][0], Quantity)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarPesanan(self):
		self.query = 'SELECT t2.NamaMenu, t2.Harga, t1.Quantity \
			FROM  Pesanan t1 \
			join Menu t2 on t1.MenuId=t2.MenuId' 
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar

	def total(self):
		self.query = 'SELECT t2.NamaMenu, t1.Quantity, (t2.Harga * t1.Quantity) as TotalHarga \
			FROM Pesanan t1 \
			join Menu t2 on t1.MenuId=t2.MenuId \
			Order by t2.MenuId Desc LIMIT 1'
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar