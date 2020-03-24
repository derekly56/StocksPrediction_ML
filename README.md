# Stock Prediction Model  

Here is a project that I'm utilizing the free stock data from
[Kaggle - S&P500](https://www.kaggle.com/camnugent/sandp500).

This project will be able to ingest stocks from multiple companies, transform it to the
data format that we'd like, and then run it through the ML model that I have built
(utilizing Linear Regression).

The current limitations of this project is the dataset only being available until
the year 2018. This is a learning project, for those who also want to build an easy, MLR utilizing available data from Kaggle.  

## Current Status  
* March 23rd, 2020 - Began Project - `NOT USABLE`  
* March 23rd, 2020 - Added DB, MLR - `NOT USABLE`
* March 24th, 2020 - Fixed MLR, DB - `USABLE, Data Plot not correct`

## How to Use  

### Requirements  
* Python 3
* numpy
* matplotlib
* pandas
* sqlite3

### Instructions
* git clone repo into local
* `cd` into `StocksPrediction_ML` directory
* If you do not have any of the requirements above, then run requirements. Else SKIP.
	* Run `pip install -r requirements.txt`
* If this is the first time running the program, then build the database. Else SKIP.
	* Run `python create_database.py`
	* This will take about a minute to complete. This only needs to be run once.
* Run `python main.py`
* Here is a list of [S&P 500 Companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) to query
* Enjoy!
