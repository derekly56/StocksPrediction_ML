'''
Multiple Linear Regression Class
--------------------------------
The MLR (Multiple Linear Regression) class that'll allow us to train our data
and predict the stock prices for the following day.

While there are other MLR classes already done for us (Scikit, Tensor, etc), I
thought it'd be fun for me to continue to learn about the behind-the-scenes.
'''

import math
import random
import numpy as np
import pandas as pd
from .helper import convert_to_epoch

class MultipleLinearRegression:
	def __init__(self):
		'''Initializes the model for the MLR class to be used'''
		self.coefs = []

	def fit(self, X, y):
		'''
		Fitting the data by utilizing the MLR equation of finding coefficients.
		First, we need to convert date-time to epoch format. Then, calculate coefs.

		Parameters:
			X (matrix): Matrix containing the training data with multiple features
			y (list): List containing the regression data for the matrix X

		'''

		if len(X.shape) == 1:
			X = self._reshape_x(X)

		nX = self._convert_to_epoch(X)
		nX = self._concat(nX)

		self.coefs = np.linalg.inv(nX.transpose().dot(nX)).dot(nX.transpose()).dot(y)
		print("coefs: " + str(self.coefs))

	def predict(self, X_test):
		'''
		Predicts the regression from the trained data. Iterate over the X matrix
		and applies the coefficients to each of the features and makes a prediction

		Parameters:
			X_test (matrix): A matrix containing the test set to run the prediction

		Returns:
			y_preds (list): A list of predictions for every entry in X
		'''

		b_0 = self.coefs[0][0]
		b_n = self.coefs[1:]
		y_pred = []

		nX_test = self._convert_to_epoch(X_test)

		for index, row in nX_test.iterrows():
			init_pred = b_0

			date, open, high = row['Date'], row['Open'], row['High']
			low, volume = row['Low'], row['Volume']
			
			input = [date, open, high, low, volume]

			for i in range(1, len(b_n)):
				init_pred += (b_n[i] * input[i])

			y_pred.append(init_pred)

		return y_pred

	def _reshape(self, X):
		'''Reshapes matrix X if there's only 1 feature'''
		return X.reshape(-1, 1)

	def _concat(self, X):
		'''Adds a vector of 1's to the matrix'''
		ones = np.ones(shape=X.shape[0]).reshape(-1, 1)
		return np.concatenate((ones, X), 1)

	def _convert_to_epoch(self, X):
		'''
		Converts the time-date to epoch and returns a new matrix

		Parameters:
			X (matrix): Matrix containing dataset with date-time

		Returns:
			nX (matrix): Matrix containing dataset with epoch
		'''

		nDate = []

		for index, row in X.iterrows():
			epoch = convert_to_epoch(row['Date'])
			nDate.append(epoch)

		nDate = pd.DataFrame(nDate, columns=['Date'])

		nX = pd.concat([nDate, X.loc[:, X.columns != 'Date']], axis=1)

		return nX
