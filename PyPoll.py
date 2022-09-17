# Add our dependencies.
import csv
from email import header
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("..","Election_Analysis", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("..","Election_Analysis", "election_analysis.txt")

#1. Initialize a total vote counter

total_votes = 0

# Candidate Options
candidate_options = []

#declare the empty dictionary
candidate_votes ={}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do:read and analyze the data here.

    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)
    #print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
      
        #print the candidate name from each row

        candidate_name = row[2]
        #if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        # Begin tracking that candidate vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

with open(file_to_save,"w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n"
        )
    print(election_results, end= "")
        #save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        #print each candidate's, vote count, and percentage to the terminal.
        print(candidate_results)
        # save the candidate's results to our text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage and candidate
    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            # And, set the winning_candidate equal to the candidate's name.
            winning_percentage = vote_percentage
        
            #print the winning candidates' results to the terminal.
            winning_candidate_summary = (
                f"----------------------------\n"
                f"winner: {winning_candidate}\n"
                f"winning vote count: {winning_count:,}\n"
                f"winning percentage: {winning_percentage:.1f}%\n"
                f"----------------------------\n")
    print(winning_candidate_summary)

    #save the winning candidates's results to the text file
    txt_file.write(winning_candidate_summary)