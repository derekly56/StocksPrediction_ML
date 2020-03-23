'''
Database Class
--------------
This class will create a DB project utilizing sqlite3. It will be able to store
data from our individual stocks and then run queries on that DB.
'''

import sqlite3
from sqlite3 import Error
import pandas as pd

clear_stock_table = '''
					DROP TABLE IF EXISTS Stocks
					'''

create_stock_table = '''
					 CREATE TABLE IF NOT EXISTS Stocks (
					 	id INTEGER PRIMARY KEY,
						StockName
					 )
'''

class StockDB:
	def __init__(self):
		'''Initializes Stocks DB'''

		self.db_name = 'stocksDB.db'
		self.tickers = self._get_company_tickers()

	def _get_company_tickers(self):
		'''Creates a dictionary that holds company names matching to tickers'''

		path = 'company_names.csv'
		company_ticks = {}

		df = pd.read_csv(path)

		for index, row in df.iterrows():
			c_name, c_ticker = row['Name'], row['Symbol']
			company_ticks[c_name] = c_ticker

		return company_ticks

	def create_connection(self, db):
		'''
		Creates a connection to the stocks DB

		Parameters:
			db (string): Name of DB

		Returns:
			Conn (db object): Connector object to the DB
		'''

		connector = None

	    try:
	        conn = sqlite3.connect(db_file)
	    except Error as e:
	        print(e)

		return connector

	def close_connection(self, connector):
		'''Closes a finished session of DB'''

		connector.close()

	def query_stock(self, stock):
		'''
		Queries for the stock data given the stock tickers

		Parameters:
			stock (str): Ticker name of stock

		Returns:
			information (List<list>): A list of list of data for the  given
									  stock ticker
		'''

		pass
