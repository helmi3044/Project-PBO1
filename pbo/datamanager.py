#akan menjalankan koneksi database dgn sqlite3
import sqlite3

class DataManager:
	# method konstruktor
	def __init__(self):
		#objek koneksi
		self.con = sqlite3.connect('D:/SQLiteStudio-3.2.1/data.sqlite3')
		#objek cursor
		self.cursor = self.con.cursor() # instantiate a cursor obj

	def executeQuery(self, query, retVal=False): #buat method untuk execute query, retval true berarti hasilnya harus ditampung (select), insert, up, del tdak perlu karena tdak ada output data
		#query masuk paramater
		# execute query
		self.cursor.execute(query)
		# variabel all result untuk menampung hasil data
		all_results = self.cursor.fetchall()
		self.con.commit()
		# apabila retval true (ada sekian data yg disimpan di all result) maka di return (dihasilkan)
		if retVal:
			return all_results

	def setDataMenu(self, NamaMenu, Harga): #method abstrak
		pass

	def setDataPerson(self, Nama, Alamat, NomorHP):
		pass
