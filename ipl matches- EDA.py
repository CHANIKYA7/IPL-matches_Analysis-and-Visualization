# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:04:50 2021

@author: Chani
"""

#importing all modules as required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#reading the dataset through pandas, which is shortly noted as pd
matches = pd.read_csv("C:/Users/Chani/Documents/Decodr/sample data/matches.csv")

"""info is calling function which gives the information about the dataset contain,
column_names and data_type and number of columns"""
matches.info()

"""descibe is also a calling function which gives number of integer elements as count, mean,
standard deviation, minimum value, 25% ,50%, 75% of data, maximum value and finally 
number of integer rows and columns"""
#which will describe only integer values of data
matches.describe(include = 'all')

#shape is used for to identify number of rows and columns in a dataset
matches.shape

#head function used for showing the top 5 rows of a dataset and indexing starts from 0
     # and if you want to print how amny rows want show would you like to give as attribute of head
matches.head()

##tail function used for showing the last 5 rows of a dataset
  #and if you want to print how many rows would you like to give as attribute of tail

matches.tail()

#isnull() means it's boolean expression whether True or False
#identifying the number of null values in a dataset and giving sum no.of true in a row

matches.isnull().sum()
matches.isnull().mean()

"""city, winner, player_of_match,umpire1,umpire2 and also umpire3 are having the null values """

#columns which gives the column names of a dataset and which is not a callable function
matches.columns

#removing the id column using the drop function
matches.drop("id", axis = 1,inplace = True)
matches.shape

#Season
matches.Season.unique()
matches.Season.nunique()
matches.Season.value_counts()
sns.countplot(matches.Season)
plt.xticks(rotation=90)


#city
matches.city.isnull().sum() # having 7 null values
matches.city.nunique()
matches.city.unique()
matches.city.value_counts()
sns.countplot(matches.city)
plt.xticks(rotation=90)
matches.city.fillna("other stadium",inplace = True)
matches.city.isnull().sum()

#date
matches.date.isnull().sum()
matches.date.unique()
matches.date.nunique()
matches.date.value_counts()
sns.countplot(matches.date)
plt.xticks(rotation=90)


#team1
matches.team1.nunique()
matches.team1.value_counts()
sns.countplot(matches.team1)
plt.xticks(rotation=90)


#teame2
matches.team2.nunique()
matches.team1.value_counts()
sns.countplot(matches.team2)
plt.xticks(rotation=90)


#toss_winner
matches.toss_winner.value_counts()
sns.countplot(matches.toss_winner)
plt.xticks(rotation=90)


#toss_decision
matches.toss_decision.value_counts()
matches.toss_decision.unique()

#result
matches.result.unique()
matches.result.nunique()
matches.result.value_counts()
sns.countplot(matches.result)
plt.xticks(rotation=90)


#dl_applied
matches.dl_applied.unique()
matches.dl_applied.nunique()
matches.dl_applied.value_counts()
sns.countplot(matches.dl_applied)
plt.xticks(rotation=90)

#winner
matches.winner.isnull().sum()
matches.winner.value_counts()
sns.countplot(matches.winner)
plt.xticks(rotation=90)
matches.winner.fillna("tie",inplace = True)
#matches.winner.fillna("no result", inplace = True)
matches.winner.isnull().sum()

#win_by_runs
matches.win_by_runs.isnull().sum()
matches.win_by_runs.unique()
matches.win_by_runs.nunique()
matches.win_by_runs.value_counts()
matches.win_by_runs.aggregate(max)

#win_by_wickets
matches.win_by_wickets.unique()
matches.win_by_wickets.nunique()
matches.win_by_wickets.isnull().sum()

#player_of_match
matches.player_of_match.isnull().sum() #having 4 null values
matches.player_of_match.unique()
matches.player_of_match.nunique()
matches.player_of_match.value_counts()
sns.countplot(matches.player_of_match)
plt.xticks(rotation=90)
matches.player_of_match.fillna("no result",inplace = True)
matches.player_of_match.isnull().sum() 

#venue
matches.venue.isnull().sum()
matches.venue.unique()
matches.venue.nunique()
matches.venue.value_counts()
sns.countplot(matches.venue)
plt.xticks(rotation=90)

#umpire1
matches.umpire1.isnull().sum() #having the 2 null values umpire1 is no relvant 
#for our analysis so we are going to remove the umpire1 column
matches.drop("umpire1", axis = 1, inplace = True)
matches.shape

#umpire2
matches.umpire2.isnull().sum() #having the 2 null values umpire2 is no relvant 
#for our analysis so we are going to remove the umpire2 column
matches.drop("umpire2", axis = 1, inplace = True)
matches.shape

#umpire3
matches.umpire3.isnull().sum()
matches.umpire3.isnull().mean() 
 #0.8425 % or 637 of null or 637 values present in the umpire3 column and 
#which are not relevent to data analysization of data
matches.umpire3.isnull().mean() 
matches.drop("umpire3", axis = 1, inplace = True)
matches.shape


matches.isnull().sum()










