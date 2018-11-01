# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:17:24 2018

@author: Jan-Gunther Gosselke
"""

import seaborn as sns
import matplotlib.pyplot as plt

<<<<<<< HEAD
fontsize = 20

=======
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
def temp_descriptive(data):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    summary = data.describe()
    per_month = []
    for city in data.City.unique():
        for i in range(1,13):
            subset = data.loc[(data['City'] == city) & (data.Date.dt.month == i)]['Mean Temperature Actual']
            per_month.append(subset)
<<<<<<< HEAD
=======
        fontsize = 20
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
        fig, ax = plt.subplots(figsize=(25,10))
        sns.boxplot(data=per_month);
        sns.despine()
        ax.set_xlabel("Month", fontsize=fontsize)
        ax.set_title("Daily Mean Temperature by Month - " + city, fontsize=fontsize)
        ax.set_xticklabels(months)
        ax.set_ylabel("Degree Celcius",fontsize=fontsize);
        
        fig, axes = plt.subplots(nrows=4, ncols=3,
                         sharex=True, sharey=True,
                         figsize=(20,20)
                        )

        for month_i, ax in enumerate(axes.flatten()):
            subset = data[data.Date.dt.month == month_i+1]
            sns.distplot(subset['Mean Temperature Actual'], kde=True, ax=ax)
            ax.set_title(months[month_i])
            # Save the full figure...
<<<<<<< HEAD
            fig.savefig('./plots/' + city + 'monthly_temperatures.png')
    return summary

def return_histogram(data, index):
    fig, ax = plt.subplots(figsize=(25,10))
    ax.set_xlabel("Return", fontsize=fontsize)
    ax.set_title("Frequency of Returns - " + index, fontsize=fontsize)
    ax.set_ylabel("Frequency",fontsize=fontsize)
    sns.distplot(data)
    fig.savefig('./plots/' + index + '_hist.png')
=======
            fig.savefig('./plots/monthly_temperatures.png')
    return summary

def return_histogram(data):
    sns.distplot(data)
>>>>>>> 46285951fc36009db5dd11b2cb328dfb7ff6d227
