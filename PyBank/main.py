import os
import csv

budget_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyBank/Instructions/PyBank/Resources/budget_data.csv')

with open(budget_csv, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        header = next(csv_reader)
        print(header)



# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit = 0

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period