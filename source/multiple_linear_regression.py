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

class MultipleLinearRegression:
	def __init__(self):
		'''Initializes the model for the MLR class to be used'''
		self.coefs = []

	def fit(self, X, y):
		'''
		Fitting the data by utilizing the MLR equation of finding coefficients

		Parameters:
			X (matrix): Matrix containing the training data with multiple features
			y (list): List containing the regression data for the matrix X

		'''
		
		if len(X.shape) == 1:
			X = self._reshape_x(X)

		X = self._concat(X)
		self.coefs = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

	def predict(self, X_test):
		'''
		Predicts the regression from the trained data. Iterate over the X matrix
		and applies the coefficients to each of the features and makes a prediction

		Parameters:
			X_test (matrix): A matrix containing the test set to run the prediction

		Returns:
			y_preds (list): A list of predictions for every entry in X
		'''

		b_0 = self.coefs[0]
		b_n = self.coefs[1:]
		y_pred = []

		for row in X_test:
			init_pred = b_0

			for x_i, b_i in zip(row, b_n):
				init_pred += (x_i * b_i)

			y_pred.append(init_pred)

		return y_pred

	def _reshape(self, X):
		'''Reshapes matrix X if there's only 1 feature'''
		return X.reshape(-1, 1)

	def _concat(self, X):
		'''Adds a vector of 1's to the matrix'''
		ones = np.ones(shape=X.shape[0]).reshape(-1, 1)
		return np.concatenate((ones, X), 1)
