import os
import csv

#Variables
total_votes = 0
data={}
candidates= []
total_candidate_votes= []
pct_votes= []


#Path set for file.
csvpath = os.path.join('', 'PyPoll', 'Resources', 'election_data.csv')

#Open csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for row in csvreader:
        #Calculations for total number of vote.
        total_votes = total_votes + 1 
        if row[2] in data.keys():
            data[row[2]] = data[row[2]] + 1
        else:
            data[row[2]] = 1

#Calculations for the total of votes.
for key, value in data.items():
    candidates.append(key)
    total_candidate_votes.append(value)

#Percentage of total votes.
pct_votes =[]
for n in total_candidate_votes:
    pct_votes.append(round(n/total_votes * 100, 1))

#Use to find the winner
data = list(zip(candidates,total_candidate_votes,pct_votes))

#Selected winner
winning_candidate= []
for name in data:
    if max(total_candidate_votes) == name[1]:
        winning_candidate.append(name[0])
        winner = winning_candidate[0]


#Print report
print("Election Results")
print(total_votes)
print(candidates)
print(pct_votes)
print(total_candidate_votes)
print(winning_candidate)

#Write results to specified file.
output_file = os.path.join('','PyPoll', 'Analysis', 'Election_Results.txt')

#Open File to specify data.
with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Khan: {pct_votes[0]} ({total_candidate_votes[0]})\n")
    txtfile.write(f"Correy: {pct_votes[1]} ({total_candidate_votes[1]})\n")
    txtfile.write(f"Li: {pct_votes[2]} ({total_candidate_votes[2]})\n")
    txtfile.write(f"O'Tooley: {pct_votes[3]} ({total_candidate_votes[3]})\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")