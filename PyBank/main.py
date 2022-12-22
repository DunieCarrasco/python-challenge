import os
import csv
# file path
budget_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyBank/Instructions/PyBank/Resources/budget_data.csv')
# set up variables
total_months = 0
total_profit = 0
profit_change =0
value = 0
greatest_increase = 0
greatest_decrease = 0
months_change = 0
dates = []
profit = []
# define variables
def print_percentages(budget_data):
    month_day = str(budget_data[0])
    profit_losses = int(budget_data[1])


# open and read csv file
with open(budget_csv, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)

        row_one = next(csv_reader)
        total_months = total_months + 1
        total_profit = int(total_profit) + int(row_one[1])
        value = int(row_one[1])
        
# run loop through csv
        for row in csv_reader:
            dates.append(row[0])

# keep track of change
            profit_change = int(row[1])-value
            profit.append(profit_change)
            value = int(row[1])

# The total number of months included in the dataset
            total_months = total_months + 1

# The net total amount of "Profit/Losses" over the entire period
            total_profit = int(total_profit) + int(row[1])

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
            average_change = round(sum(profit)/len(profit),2)

# The greatest increase in profits (date and amount) over the entire period
            greatest_increase = max(profit)
            greatest_value = profit.index(greatest_increase)
            greatest_date = dates[greatest_value]

# The greatest decrease in profits (date and amount) over the entire period
            greatest_decrease = min(profit)
            lowest_value = profit.index(greatest_decrease)
            lowest_date = dates[lowest_value]

 
# print in terminal
print("Financial Analysis")
print('----------------------------------------')
print (f"Total Months: {total_months}")
print (f"Total: ${total_profit}")
print (f"Average Change: ${average_change}")
print (f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})")
output_file = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyBank/Instructions/PyBank/Resources/budget_data.csv')





# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period


# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period