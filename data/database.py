'''
Database Class
--------------
This class will create a DB project utilizing sqlite3. It will be able to store
data from our individual stocks and then run queries on that DB.
'''

import sqlite3
from sqlite3 import Error
import pandas as pd
import os
import glob

CLEAR_STOCK_TABLE = '''
					DROP TABLE IF EXISTS Stocks;
					'''

CREATE_STOCK_TABLE = '''
					 CREATE TABLE IF NOT EXISTS Stocks (
						id INTEGER PRIMARY KEY,
						StockName varchar(30),
						Date DATETIME,
						Open DOUBLE,
						High DOUBLE,
						Low DOUBLE,
						Close DOUBLE,
						Volume INTEGER
					 );
					 '''

INSERT_STOCK_TABLE = '''
					 INSERT INTO Stocks(StockName, Date, Open, High, Low, Close, Volume)
					 VALUES (?,?,?,?,?,?,?);
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

	def _create_database(self, name):
		'''
		Creates a DB object that stores all of the stock information from the
		individual_stocks folder (500 companies).

		Parameters:
			name (str): Name of DB
		'''

		path_to_stocks = os.getcwd() + '/individual_stocks/*.csv'
		stock_file_names = glob.glob(path_to_stocks)

		db_conn = sqlite3.connect(name)
		c = db_conn.cursor()

		c.execute(CLEAR_STOCK_TABLE)
		c.execute(CREATE_STOCK_TABLE)

		for file_name in stock_file_names:
			s_information = self._grab_stock_information(file_name)
			c.executemany(INSERT_STOCK_TABLE, s_information)
			db_conn.commit()

		c.close()

	def _grab_stock_information(self, filename):
		'''
		Opens up the file and returns a list of tuple of stock information in
		the following format:

		(StockName, Date, Open, High, Low, Close, Volume)

		Parameters:
			filename (str): Name of file to grab stock information

		Returns:
			stock_information (list<list>): A list of list of stock information
		'''

		stock_information = []

		df = pd.read_csv(filename)

		for index, row in df.iterrows():
			info_tuple = (row.Name, row.date, row.open, row.high, row.low, row.close, row.volume)
			stock_information.append(info_tuple)

		return stock_information

	def create_connection(self):
		'''
		Creates a connection to the stocks DB

		Parameters:
			db (str): Name of DB

		Returns:
			Conn (db object): Connector object to the DB
		'''

		connector = None

		try:
			connector = sqlite3.connect(self.db_name)
		except Error as e:
			print(e)

		return connector

	def query_stock(self, company_name):
		'''
		Queries for the stock data given the company name

		Parameters:
			company_name (str): Company name

		Returns:
			information (List<list>): A list of list of data for the given
									  company name
		'''
		stock = self.tickers[company_name]
		QUERY = '''SELECT * FROM Stocks where Stockname = '{0}';'''.format(stock)
		conn = self.create_connection()
		c = conn.cursor()

		c.execute(QUERY)
		query_information = c.fetchall()
		c.close()

		return query_information

	def check_company(self, company_name):
		'''Checks if the company is valid for S&P 500'''
		if company_name not in self.tickers:
			return False

		return True
