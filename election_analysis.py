# Election_Analysis
#file_variable = open(election_results, 'r')
import os
import csv
print('current working directory' , os.getcwd())
file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join( "election_analysis.txt")
#initialize total vote counter
total_votes=0
county_votes = {}
#initialize candidate option
candidate_options = []
#declare empty directory
candidate_vote = {}
#wiing candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the file
with open(file_to_load) as election_analysis:
    #read the file object with reader function
    file_reader = csv.reader(election_analysis)
    print('')
    #read and print the header row
    headers = next(file_reader)

    #print each row in csv file
    for row in file_reader:
        #add to total vote count:
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_vote[candidate_name] = 0
        # Increment vote to that candidate's count.
        candidate_vote[candidate_name] += 1
 
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
 
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_vote:
        # 2. Retrieve vote count of a candidate.
        votes  =  candidate_vote[candidate]
        # 3. Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) * 100 
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
       
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate 
 
    # Print the total votes and candidate options.
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
        
        
        
        
        
#git status
#git add .
#git status
#git commit -m "adding the election audit code."
#git push



