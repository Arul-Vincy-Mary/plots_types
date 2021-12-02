# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:39:21 2020

@author: Admin
"""

import os
os.chdir("E:/python")
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cars_data = pd.read_csv('to.csv',index_col=0,na_values =["??"])
cars_data.dropna(axis=0,inplace=True)
 
##scatter plot
 sns.set(style="darkgrid")
 sns.regplot(x= cars_data['Age'],y=cars_data['Price']) 
 sns.regplot(x= cars_data['Age'],y=cars_data['Price'],fit_reg=False) 
 sns.regplot(x= cars_data['Age'],y=cars_data['Price'],marker='*',fit_reg=False) 
 sns.lmplot(x='Age', y='Price',data =cars_data,fit_reg=False,hue='FuelType',
                                                legend=True,palette="Set1")
 ##histogram
 sns.distplot(cars_data['Age'])  
 sns.distplot(cars_data['Age'],kde=False) 
 ##fixed no.of bins
 sns.distplot(cars_data['Age'],kde=False,bins=5) 

 ##Bar plot 
 sns.countplot(x="FuelType",data=cars_data) 
 sns.countplot(x="FuelType",data=cars_data,hue="Automatic") 
 cars_data2 = pd.read_csv('to.csv',index_col=0,na_values=["??"]) 
 cars_data2.dropna(axis=0,inplace=True)
 pd.crosstab(index=cars_data['Automatic'],
             columns=cars_data2['FuelType'],
             dropna=True) 

 ##Box and Whiskers plot
 sns.boxplot(y=cars_data["Price"]) 
 sns.boxplot(x=cars_data['FuelType'],y=cars_data["Price"])
 sns.boxplot(x='FuelType',y=cars_data["Price"],hue="Automatic",data=cars_data)

##pairwise plot      
sns.pairplot(cars_data,kind="scatter",hue="FuelType")
plt.show()
 
 sns.pairplot(cars_data)
 plt.show()