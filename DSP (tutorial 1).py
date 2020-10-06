
"""
Created on Tue Oct  6 15:17:59 2020

@author: MussaYousef
"""

## Q1
import csv     # imports the csv module
import sys      # imports the sys module

f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
     rowCount += 1

print ('There are', rowCount , 'rows in this dataset ')

## Q2
#calculate the average value using a loop along a column

rowCount= 0 #variable to keep the row count value 
totalValue= 0  #variable to keep the column total


f= open('TB_burden_countries_2014-09-29.csv')

l=next(f) #skips the column headers as we want to omit it in our averaging
colHeaders = l.split(',') # plit the col names string 
#Average for e_prev_num_lo which has a column id 11
for row in csv.reader(f):
    try:
        val=float(row[11])
        totalValue += val
        rowCount += 1
    except ValueError:
        pass
    
    
if rowCount > 0:
    columnAverage = totalValue / rowCount
    print('column Average:',columnAverage)
    


rowCount1990=0#variable for the rows dated 1990
total1990=0 #to keep the total number of rows in 1990

rowCountount2011=0 #variable for the rows dated 2011
total2011=0 #to keep the total number of rows in 2011

f = open('TB_burden_countries_2014-09-29.csv') #opens the CSV file

l=next(f) #skips the column headers 
colHeaders=l.split(',') #split the col names 

#e_prev_num_lo is column id 11, year column id 5


for row in csv.reader(f):
    try:
        year=int(row[5])
    except valueError:
        continue 
     #if there is a missing value,we stop iteration and move on
    
    try:
        val=float(row[11])
    except ValueError:
        continue 
    # Using  an if clause to make sure that we are using the correct years
    if year == 1990:
        total1990 += val
        rowCount1990 +=1 
        
    if year == 2011:
        total2011 += val
        rowCount2011 +=1
            
    if rowCount1990 > 0:
        columnAverage = total1990 / rowCount1990
        print('Average for 1990:', columnAverage, 'with', rowCount1990,'data points.')
    
if rowCount2011 > 0:
    columnAverage = total2011/rowCount2011
print('Average for 2011',columnAverage,'with',rowCount2011,'data points.')
    