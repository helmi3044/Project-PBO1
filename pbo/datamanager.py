#akan menjalankan koneksi database
import sqlite3

class DataManager:
	# method konstruktor
	def __init__(self):
		#objek koneksi
		self.con = sqlite3.connect('D:/SQLiteStudio-3.2.1/data.sqlite3')
		#objek cursor
		self.cursor = self.con.cursor() # instantiate a cursor obj
	def executeQuery(self, query, retVal=False):
		# execute query
		self.cursor.execute(query)
		# variabel all result untuk menampung hasil data
		all_results = self.cursor.fetchall()
		self.con.commit()
		# apabila retval true maka di return (dihasilkan)
		if retVal:
			return all_results
