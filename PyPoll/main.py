import os
import csv


election_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyPoll/Resorces/election_data.csv')

election_csv = "/Users/danielcarrasco/Desktop/python-challenge/PyPoll/Resorces/election_data.csv"

#read = open(election_csv, "r")

#read.close()


with open(election_csv, "r") as read:
    csv_read = csv.reader(read, delimiter= ",")
    print(csv_read)
    for row in csv_read:
        print(row)
