# import modules
import os
import csv

#file path
election_csv = os.path.join('/Users/danielcarrasco/Desktop/python-challenge/PyPoll/Resorces/election_data.csv')

# set up variables
total_vote = 0
candidates = []
number_votes = []
percent_votes = []

# open and read csv file
with open(election_csv, "r") as read:
    csv_read = csv.reader(read, delimiter= ",")
    header = next(csv_read)

    # run loop through csv
    for row in csv_read:

        # The total number of votes cast
        total_vote = total_vote + 1

        # A complete list of candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else: 
            index = candidates.index(row[2])
            number_votes[index] = number_votes[index] + 1

# The percentage of votes
for votes in number_votes:
    percentage = (votes/total_vote) * 100
    percentage = round((percentage),3)
    percent_votes.append(percentage)

    # The winner of the election based on popular vote.
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

# print in terminal
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Vote: {total_vote}")
print(f"-----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])}% ({str(number_votes[i])})")
print(f"-----------------------------")
print(f"Winner: {winning_candidate}")
print(f"-----------------------------")

with open("PyPoll_result.txt", "w") as f:
    f.write("\nElection Results")
    f.write(f"\n-----------------------------")
    f.write(f"\nTotal Vote: {total_vote}")
    f.write(f"\n-----------------------------")
    for i in range(len(candidates)):
        f.write(f"\n{candidates[i]}: {str(percent_votes[i])}% ({str(number_votes[i])})")
    f.write(f"\n-----------------------------")
    f.write(f"\nWinner: {winning_candidate}")
    f.write(f"\n-----------------------------")
    f.close()
