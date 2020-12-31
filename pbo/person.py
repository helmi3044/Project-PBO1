import sqlite3
from datamanager import DataManager

#turunan dari kelas data manager
class Person(DataManager):
	# untuk memasukkan data baru ke tabel person
	def setDataPerson(self, Nama, Alamat, NomorHP):
		self.query = 'INSERT INTO Person (Nama, Alamat, NomorHP) \
			VALUES (\'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (Nama, Alamat, NomorHP)
		#untuk menampilkan dilayar
		print('self.query : ', self.query )
		#diambil dari datamanager, jdi tidak perlu di declare lagi
		self.executeQuery(self.query)

	# untuk mendapatkan data	
	def getDataPerson(self, Nama, Alamat, NomorHP):
		# menghasilkan output 1 data dan dimasukkan ke var idperson
		self.query = 'SELECT IdPerson FROM Person \
			where Nama=\'%s\' and Alamat=\'%s\' and NomorHP=\'%s\'' 
		self.query = self.query % (Nama, Alamat, NomorHP)
		print('self.query : ', self.query )
		IdPerson = self.executeQuery(self.query, retVal=True)
		return IdPerson
