# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:26:09 2018

@author: Jan-Gunther Gosselke
"""
import pickle
import pandas as pd
import numpy as np
import math
import loading_data as ld
import NN
import descriptive as de
from sklearn import preprocessing


weather_path = "C:/Users/Jan-Gunther Gosselke/Google Drive/SDA/Data/Weather_ALL.csv"
stock_path = "C:/Users/Jan-Gunther Gosselke/Google Drive/SDA/Data/StockIndices.csv"
price_data_list, weather_per_city = ld.load_data(stock_path, weather_path)
return_data_list = {}
for index in price_data_list:
    return_data_list[index] = pd.DataFrame(columns=list(price_data_list[index]))
    return_data_list[index].rename(columns={'Price Close':'Return'}, inplace=True)
    for city in price_data_list[index].City.unique():
        ordered_returns = price_data_list[index][price_data_list[index]["City"] == city].sort_values(by="Date")
        ordered_returns.rename(columns={'Price Close':'Return'}, inplace=True)
        ordered_returns["Return"] = np.log(ordered_returns['Return']) - np.log(ordered_returns['Return'].shift(periods=-1))
<<<<<<< HEAD
        return_data_list[index] = pd.concat([return_data_list[index], ordered_returns]).dropna(axis=0, how = "any")
=======
        return_data_list[index] = pd.concat([return_data_list[index], ordered_returns])
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227

filename = "./price-data.pickle"
with open(filename, 'wb') as handle:
    pickle.dump(price_data_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
filename = "./retur-data.pickle"
with open(filename, 'wb') as handle:
    pickle.dump(return_data_list, handle, protocol=pickle.HIGHEST_PROTOCOL)

##Descriptive Statistics
<<<<<<< HEAD
for data in price_data_list:
    de.temp_descriptive(weather_per_city)
    
for index in return_data_list:
    print(index)
    de.return_histogram(return_data_list[index]['Return'], index)
=======
#for data in price_data_list:
#    de.temp_descriptive(weather_per_city)
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
    

    
#for data in data_list
min_max_scaler = preprocessing.MinMaxScaler()
for price_data in price_data_list:
    #Neural Net Data
<<<<<<< HEAD
    print('------\n------\n------\n' + price_data + '\n------')
=======
    print(price_data)
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
    data = price_data_list[price_data].pivot_table(index = ["Date", "Price Close"], columns='City',
                          values = ['Mean Temperature Actual',	'Low Temperature Actual',
                                    'High Temperature Actual',	'Precipitation Actual',	'Wind Speed Actual',
                                    'Relative Humidity Actual']).reset_index(level=['Price Close']).dropna(axis=0, how = "any")
    Y = data['Price Close'].to_frame().values
    X = min_max_scaler.fit_transform(data.drop("Price Close", axis = 1).values)
<<<<<<< HEAD
    print('------\n------\n------\n One hidden layers\n------')
    NN.Fully_Connected_OneL(X, Y)
    print('------\n------\n------\n Two hidden layers\n------')
    NN.Fully_Connected_TwoL(X, Y)
    
    
for return_data in return_data_list:
    #Neural Net Data
    print('------\n------\n------\n' + return_data + '\n------')
=======
    NN.FullyConected(X, Y)
    
for return_data in return_data_list:
    #Neural Net Data
    print(return_data)
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
    data = return_data_list[return_data].pivot_table(index = ["Date", "Return"], columns='City',
                          values = ['Mean Temperature Actual',	'Low Temperature Actual',
                                    'High Temperature Actual',	'Precipitation Actual',	'Wind Speed Actual',
                                    'Relative Humidity Actual']).reset_index(level=['Return']).dropna(axis=0, how = "any")
    Y = data['Return'].to_frame().values
    X = min_max_scaler.fit_transform(data.drop("Return", axis = 1).values)
<<<<<<< HEAD
    print('------\n------\n------\n One hidden layers\n------')
    NN.Fully_Connected_OneL(X, Y)
    print('------\n------\n------\n Two hidden layers\n------')
    NN.Fully_Connected_TwoL(X, Y)
=======
    NN.FullyConected(X, Y)
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
