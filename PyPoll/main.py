# modules
import os
import csv

# set file path
election_data_csv = os.path.join('..', 'PyPoll', 'election_data.csv')

# set up different variables
total_votes = 0
candidate = ""
candidate_votes = {}
winners_votes = 0
winner = ""
candidate_percent = {}

# open csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # start the loop for the data
    for line in csvreader:
        total_votes = total_votes + 1
        candidate = line[2]
        #print(candidate)

        # set conditional for total votes
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1


output = (
    f"\nElection Votes\n"
    f"----------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------------\n"
)

print(output)
      