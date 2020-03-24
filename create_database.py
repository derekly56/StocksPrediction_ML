'''
Create Database File
--------------------
This file will instantiate the database ONCE so the user doesn't need to continuously
rebuild the DB. They are given the option to reset the DB, just in case some
corruption occurs
'''

from data.database import StockDB

def create_db():
	print("Initializing Database - BEGIN")
	print("---------------")

	db = StockDB()
	db._create_database()

	print()
	print("Initilizating Database - FINISHED")

def main():
	create_db()

if __name__ == '__main__':
	main()
