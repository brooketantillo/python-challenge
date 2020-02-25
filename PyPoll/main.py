# modules
import os
import csv

# set file path
election_data_csv = os.path.join('..', 'PyPoll', 'election_data.csv')
path_output = os.path.join('..', 'PyPoll', 'election_data.txt')

# set up different variables
total_votes = 0
candidate = ""
candidate_votes = {}

# open csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # start the loop for total votes
    for line in csvreader:
        total_votes = total_votes + 1
        candidate = line[2]
        #print(candidate)

        # set conditional for total votes
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# set variables for percent and winners
winners_votes = 0
winner = ""
candidate_percent = {}

# start loop for list of candidates, percentage of votes, total votes, and winner
for running_candidate, vote_tally in candidate_votes.items():
    candidate_percent[running_candidate] = (vote_tally / total_votes)*100   
    if vote_tally > winners_votes:
        winners_votes = vote_tally
        winner = running_candidate

print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
for running_candidate, vote_tally in candidate_votes.items():
    print(f"{running_candidate}: {candidate_percent[running_candidate]}% ({vote_tally})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")

# export text file
with open(path_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------------------\n")
    for running_candidate, vote_tally in candidate_votes.items():
        txt_file.write(f"{running_candidate}: {candidate_percent[running_candidate]}% ({vote_tally})\n")
    txt_file.write("----------------------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("----------------------------------------\n")
      