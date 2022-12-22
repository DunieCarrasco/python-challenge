import os
import csv

Total_Vote = 0

election_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyPoll/Resorces/election_data.csv')

election_csv = "/Users/danielcarrasco/Desktop/python-challenge/PyPoll/Resorces/election_data.csv"


with open(election_csv, "r") as read:
    csv_read = csv.reader(read, delimiter= ",")
    header = next(csv_read)
    print(header)

    for row in csv_read:
        Total_Vote = Total_Vote + 1
        

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

print(f"Election Results")
print(f"-----------------------------")
print(f"Total Vote: {Total_Vote}")
print(f"-----------------------------")
print(f"")