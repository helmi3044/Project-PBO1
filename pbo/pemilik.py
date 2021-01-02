import sqlite3
from datamanager import DataManager
from person import Person

class Pemilik(Person):
	def setDataPemilik(self, Nama, Alamat, NomorHP):
		self.setDataPerson(Nama, Alamat, NomorHP)
		IdPerson = self.getDataPerson(Nama, Alamat, NomorHP)
		self.query = 'INSERT INTO Pemilik (IdPerson) \
			values (\'%s\')' 
		self.query = self.query % (IdPerson[0][0])
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarPemilik(self):
		self.query = 'SELECT t1.IdPemilik, t2.Nama, t2.Alamat, t2.NomorHP \
			FROM Pemilik t1 \
			join person t2 on t1.IdPerson=t2.IdPerson' 
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar

	def pendapatan(self):
		self.query = 'SELECT SUM(t2.Harga * t1.Quantity) as pendapatan \
			FROM Pesanan t1 \
			join Menu t2 on t1.MenuId=t2.MenuId'
		daftar = self.executeQuery(self.query, True)
		return daftar