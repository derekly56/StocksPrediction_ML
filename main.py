'''
Main python function to utilize MLR (Multiple Linear Regression) on the stock
data being stored in our DB.

First, the user will select a company that they want to analyze. Then, the data
will be transformed, cleaned, and then sent to the MLR for analyzing. From here,
we can check how well the MLR did with predictions.
'''

import numpy as np
import pandas as pd
import os
from data.database import StockDB
from source.helper import query_data_to_df, split_data, r2_score
from source.multiple_linear_regression import MultipleLinearRegression

def get_company_user_input(DB):
	user_input = input("Name of S&P 500 Company to analyze (Please enter full and correct company name): ")

	while not DB.check_company(user_input):
		print("Company not found, please enter a valid company")
		print("-----------------------------------------------")
		user_input = input("Name of S&P 500 Company to analyze (Please enter full and correct company name): ")

	return user_input

def intro_display():
	print("Stock Prediction ML")
	print("-------------------")

def end_display():
	pass

def analyze_another_company():
	pass

def plot_data():
	pass

def main():
	# Initializing DB and MLR model
	db = StockDB()
	end = False

	while not end:
		# Grab stock information from DB
		user_input = get_company_user_input()
		stock_information = db.query_stock(user_input)

		# Transform data to be used by MLR
		stock_df = query_data_to_df(stock_information)
		X_train, y_train = df_to_train_dataset(stock_df)
		X_train, y_train, X_test, y_test = split_data(X_train, y_train)

		# Send to MLR to analyze
		MLR = MultipleLinearRegression()
		MLR.fit(X_train, y_train)

		y_pred = MLR.predict(X_test)
		r2 = r2_score(y_test, y_pred)

		# TO-DO


if __name__ == '__main__':
	main()
