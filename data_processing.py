# import main libraries

import pandas as pd # data manipulation
import numpy as np # data manipulation
import yfinance as yf # get financials of the companies
import pymongo # connect to MongoDB
from pymongo import MongoClient # connect to MongoDB
import json # convert data to json



def extract_ticker():
    # extract the ticker data
    
    msft = yf.Ticker('MSFT')
    zion = yf.Ticker('ZION')
    ibm = yf.Ticker('IBM')
    jnj = yf.Ticker('JNJ')
    mcd = yf.Ticker('MCD')
    # create a dictionary to store the data
    dct2 = {'Company_name': [msft.info['longName'], zion.info['longName'], ibm.info['longName'], jnj.info['longName'], mcd.info['longName']],
                    'Company_ticker': [msft.info['symbol'], zion.info['symbol'], ibm.info['symbol'], jnj.info['symbol'], mcd.info['symbol']],
                    'Closed_price': [msft.info['previousClose'], zion.info['previousClose'], ibm.info['previousClose'], jnj.info['previousClose'], mcd.info['previousClose']],
                    'Company_info': [msft.info['longBusinessSummary'], zion.info['longBusinessSummary'], ibm.info['longBusinessSummary'], jnj.info['longBusinessSummary'], mcd.info['longBusinessSummary']],
                    'Company_PE': [msft.info['trailingPE'], zion.info['trailingPE'], ibm.info['trailingPE'], jnj.info['trailingPE'], mcd.info['trailingPE']],
                    'Company_cash_flow': [msft.info['operatingCashflow'], zion.info['operatingCashflow'], ibm.info['operatingCashflow'], jnj.info['operatingCashflow'], mcd.info['freeCashflow']],
                    'Company_dividend': [msft.info['dividendRate'], zion.info['dividendRate'], ibm.info['dividendRate'], jnj.info['dividendRate'], mcd.info['dividendRate']]}
        
    # create a dataframe to store the data
    df = pd.DataFrame(dct2)
    # return the dataframe
    return df


def transform_data():
    # create a dataframe to store the data
    df_transformed = extract_ticker() # call the extract function
    # round the values of the dataset to 2 decimal places
    df_transformed = df_transformed.round(2)
    
    # convert the dataframe into a json file
    json_file = df_transformed.to_json('yahoo_data.json' ,indent=4, orient='records')
    return json_file




def load_mongo():
    # load the json file into mongodb
    # create a client object
    client = MongoClient('mongodb+srv://jdegbun:BA6rRLlNLc4lvWRo@cluster0.avypgbd.mongodb.net/?retryWrites=true&w=majority') # insert your connection string and your personal user and password of your MongoDB account
    # get a database named "stockdb"
    db1 = client.financial_companies_etl_python_mongo

    # get a collection named "yahoo_data_test_json"
    collection_main = db1.yahoo_data_test_json
    # load a json file into mongodb
    with open('yahoo_data.json') as file:
        file_data = json.load(file)
    # insert_many is used else insert_one is used
    if isinstance(file_data, list):
        # empty the collection
        collection_main.delete_many({})
        # insert the data into the collection
        collection_main.insert_many(file_data)
    else:
        collection_main.insert_one(file_data)
    return True