import sqlite3
from datamanager import DataManager
from person import Person

# class pembeli merupakan turunan dari kelas person, sehingga membawa method bawaan dari class person dan class data manager
# ada 2 method yang hampir sama dgn person (set atau memasukkan data) maka terjadi overloading (paramater/signature berbeda)
class Pembeli(Person):
	def setDataPembeli(self, Nama, Alamat, NomorHP):\
		# memanggil method bawaan parent class
		self.setDataPerson(Nama, Alamat, NomorHP)
		IdPerson = self.getDataPerson(Nama, Alamat, NomorHP)
		self.query = 'INSERT INTO Pembeli (IdPerson) \
			values (\'%s\')' 
		self.query = self.query % (IdPerson[0][0])
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarPembeli(self):
		self.query = 'SELECT t2.Nama, t2.Alamat, t2.NomorHP \
			FROM  Pembeli t1 \
			join person t2 on t1.IdPerson=t2.IdPerson' 
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar