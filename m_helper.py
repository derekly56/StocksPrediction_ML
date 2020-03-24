'''
Main Helper File
----------------
This file will be used as part of main.py to help clean up the clutter
'''

import matplotlib.pyplot as plt
from data.database import StockDB

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
	print()
	print("Closing Stock Prediction ML program")

def analyze_another_company():
	cont = input("Would you like to analyze another company? (Y/N)")

	while cont != 'Y' or cont != 'N':
		cont = input("Would you like to analyze another company? (Y/N)")

	if cont == 'Y':
		return True
	return False

def plot_data(X_test, y_test, y_pred, r2):
	dates = X_test['Date'].values.tolist()

	fig = plt.figure()
	ax1 = fig.add_subplot(111)

	ax1.scatter(dates, y_test, c='b', marker='o')
	ax1.plot(dates, y_pred, c='r')

	plt.title("Prediction vs True Labels")
	plt.xlabel("Dates")
	plt.ylabel("Stock Closing Price")

	plt.xticks(rotation=90)
	ax1.legend(('True Data', 'Prediction Data r2={}'.format(r2)))
	plt.show()
