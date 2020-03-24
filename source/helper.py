'''
Helper file
-----------
This file will have functions that'll help with the MLR process, such as data
handling/transformation from the database, and other helpful functionalities.
'''

import math
import pandas as pd
import numpy as np
import random

def query_data_to_df(query_information):
	'''
	Given information from the query, convert it to a dataframe to be utilized
	by the MLR model

	Parameters:
		query_information (list<list>): Information of queried stock data

	Returns:
		df (DataFrame): Dataframe containing all the correct columns
	'''

	if query_information:
		cols = ['id','Name', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
		df = pd.DataFrame(query_information, columns = cols)

		return df
	else:
		return None

def df_to_train_dataset(df):
	'''
	Given the dataframe, convert to training dataset to be utilized by MLR

	Parameters:
		df (dataframe): Dataframe containing query information

	Returns:
		x_train (matrix): matrix of training data
		y_train (list): list of corresponding stock closing price
	'''
	x_cols = ['Date', 'Open', 'High', 'Low', 'Volume']
	y_cols = ['Close']

	x_train = df[x_cols].tolist()
	y_train = df[y_cols].tolist()

	return x_train, y_train

def split_data(x_train, y_train, split_size=0.1):
	'''
	Given the training data set, split it into the split_size and return a training
	set and a testing set. We will be utilizing the built-in python random functionality
	to select split_size * len(x_train) amount of items to be in the testing dataset

	Parameters:
		x_train (list<list>): Dataset containing the stock information
		y_train (list): Dataset containing the stock prices (labels)

	Returns:
		x_train (list<list>): (1 - split_size) of the original dataset
		y_train (list): (1 - split_size) of the original dataset labels
		x_test (list<list>): split_size of the original dataset to be used as test
		y_test (list): split_size of the original dataset to be used as test, labels
	'''

	if len(x_train) == len(y_train):
		random.seed()

		nx_train, ny_train, nx_test, ny_test = [], [], [], []

		test_size = round(len(x_train) * split_size)
		train_size = len(x_train) - test_size

		rand_index = random.sample(list(enumerate(x_train)), test_size)
		indexes = {idx: val for idx, val in rand_index}

		for i in range(len(x_train)):
			if i in indexes:
				nx_test.append(indexes[i])
				ny_test.append(y_train[i])
			else:
				nx_train.append(x_train[i])
				ny_train.append(y_train[i])

		return nx_train, ny_train, nx_test, ny_test
	else:
		return None, None, None, None

def r2_score(y_true, y_pred):
	'''
	Calculates r2 score

	Parameters:
		y_true (list): list of true labels
		y_pred (list): list of prediction label

	Returns:
		r2 (float): r2 score of between true and prediction labels
	'''

	y_avg = np.average(y_true)

	numerator = 0
	denominator = 0

	for i in range(len(y_true)):
		numerator += ((y_true[i] - y_pred[i]) ** 2)
		denominator += ((y_true[i] - y_avg) ** 2)

	return numerator/denominator
