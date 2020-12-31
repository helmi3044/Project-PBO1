import sqlite3
from datamanager import DataManager

#turunan dari kelas data manager
class Menu(DataManager):
	# untuk memasukkan data baru ke tabel person
	def setDataMenu(self, NamaMenu, Harga):
		self.query = 'INSERT INTO Menu (NamaMenu, Harga) \
			VALUES (\'%s\', \'%s\')' 
		self.query = self.query % (NamaMenu, Harga)
		#untuk menampilkan dilayar
		print('self.query : ', self.query )
		#diambil dari datamanager, jdi tidak perlu di declare lagi
		self.executeQuery(self.query)

	# untuk mendapatkan data	
	def getDataMenu(self, NamaMenu, Harga):
		# menghasilkan output 1 data dan dimasukkan ke var idperson
		self.query = 'SELECT MenuId FROM Menu \
			where NamaMenu=\'%s\' and Harga=\'%s\'' 
		self.query = self.query % (NamaMenu, Harga)
		print('self.query : ', self.query )
		MenuId = self.executeQuery(self.query, retVal=True)
		return MenuId

	def getDaftarMenu(self):
		self.query = 'SELECT DISTINCT NamaMenu, Harga \
			FROM  Menu'
		# ~ print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar