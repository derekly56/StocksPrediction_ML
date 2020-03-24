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
import glob
from data.database import StockDB
from source.helper import query_data_to_df, split_data, r2_score, df_to_train_dataset
from source.multiple_linear_regression import MultipleLinearRegression
from .m_helper import get_company_user_input, analyze_another_company
from .m_helper import intro_display, end_display, plot_data

def main():
	intro_display()

	# Initializing DB and MLR model
	db = StockDB()
	analyzing = True

	while analyzing:
		# Grab stock information from DB
		user_input = get_company_user_input(db)
		stock_information = db.query_stock(user_input)

		# Transform data to be used by MLR
		stock_df = query_data_to_df(stock_information)
		X_train, y_train = df_to_train_dataset(stock_df)
		X_train, y_train, X_test, y_test = split_data(X_train, y_train)

		# Send to MLR to analyze
		MLR = MultipleLinearRegression()
		MLR.fit(X_train, y_train)

		y_pred = MLR.predict(X_test)
		r2 = r2_score(y_test.values.tolist(), y_pred)

		plot_data(X_test, y_test.values.tolist(), y_pred, r2)

		analyzing = analyze_another_company()

	end_display()

if __name__ == '__main__':
	main()
