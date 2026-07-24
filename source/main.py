from config import *

class Company:
	_id_index = 0
	def __init__(self):
		Company._id_index += 1
		self.uid = Company._id_index
		self.full_name = "Stocs"

	def get_cid(self):
		print("UID:",self.uid)
		return self.uid

com1 = Company()
com1.get_cid()