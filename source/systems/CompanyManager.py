from random import randint, choice
from market.company import Company
from config.industry import Industry
from config.prefix import PREFIXES
from config.core import CORES
from config.suffix import SUFFIXES

class CompanyManager:
	def __init__(self):
		self.companies = list()
		self.companies_by_uid = dict()
		self.uid_index = 0

	def create_company(self):
		self.uid_index += 1
		industry = Industry(randint(0,19))

		prefix = choice(PREFIXES[industry])
		core = choice(CORES[industry])
		suffix = SUFFIXES[randint(0, len(SUFFIXES)-1)]

		full_name = prefix + core + suffix

		first_char = prefix[:1]
		second_char = core[:1]
		last_char = suffix[:1]

		ticker = first_char+second_char+last_char

		company =  Company(uid = self.uid_index, full_name = full_name, industry = industry, ticker= ticker)

		self.companies.append(company)
		self.companies_by_uid[company.uid] = company

		print("companies_list:",self.companies)
		print("companies_by_uid:", self.companies_by_uid)
		print(company)
		print(company.uid)
		print(company.full_name)
		print(company.ticker)
		print(company.industry)
