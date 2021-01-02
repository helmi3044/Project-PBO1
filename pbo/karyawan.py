import sqlite3
from datamanager import DataManager
from person import Person

class Karyawan(Person):
	def setDataKaryawan(self, Nama, Alamat, NomorHP, JamKerja, HargaPerjam):
		self.setDataPerson(Nama, Alamat, NomorHP)
		IdPerson = self.getDataPerson(Nama, Alamat, NomorHP)
		self.query = 'INSERT INTO Karyawan (IdPerson, JamKerja, HargaPerjam) \
			values (\'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (IdPerson[0][0], JamKerja, HargaPerjam)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarKaryawan(self):
		self.query = 'SELECT t1.IdKaryawan, t2.Nama, t2.Alamat, t2.NomorHP, t1.JamKerja, t1.HargaPerjam \
			FROM karyawan t1 \
			join person t2 on t1.IdPerson=t2.IdPerson' 
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar

	def gaji(self):
		self.query = 'SELECT t2.Nama, (JamKerja * HargaPerjam) as gaji \
			FROM karyawan t1 \
			join person t2 on t1.IdPerson=t2.IdPerson'
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar