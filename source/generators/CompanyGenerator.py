from random import randint, choice
from market import company
from config.industry import Industry
from config.prefix import PREFIXES
from config.core import CORES
from config.suffix import SUFFIXES
from systems.CompanyManager import CompanyManager

class CompanyGen:
	def __init__(self):
		self.uid_index = 0
		self.create_company()

	def generate_full_name(self, industry):
		prefix = choice(PREFIXES[industry])
		core = choice(CORES[industry])
		suffix = SUFFIXES[randint(0, len(SUFFIXES))]
		full_name = prefix + core + suffix

		first_char = prefix[:1]
		second_char = core[:1]
		last_char = suffix[:1]

		ticker = first_char+second_char+last_char

		return (full_name, ticker)
	def create_company(self):
		self.uid_index += 1
		industry = Industry(randint(0,19))
		full_name, ticker = self.generate_full_name(industry)

		return company.Company(uid = self.uid_index, full_name=full_name, industry = industry, ticker= ticker)
		
