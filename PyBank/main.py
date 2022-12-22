import os
import csv

budget_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyBank/Instructions/PyBank/Resources/budget_data.csv')

total_months = 0
total_profit = 0
profit_change =0
value = 0
dates = []
profit = []
def print_percentages(budget_data):
    month_day = str(budget_data[0])
    profit_losses = int(budget_data[1])



with open(budget_csv, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)
        print(header)

        for row in csv_reader:
            total_months = total_months + 1
            total_profit = int(total_profit) + int(row[1])

            value = int(row[1])

            dates.append(row[0])
            profit_change = int(row[1])-value
            profit.append(profit_change)
            value = int(row[1])

            greatest_increase = max(profit)
            greatest_value = profit.index(greatest_increase)
            greatest_date = dates[greatest_value]



print("Financial Analysis")
print('----------------------------------------')
print (f"Total Months: {total_months}")
print (f"Total: ${total_profit}")
print ("Average Change: ${}")
print (f"Greatest Increase in Profits: {greatest_date} ${greatest_increase}")
#print (f"Greatest Decrease in Profits: {} ${}")




# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit = 0

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period