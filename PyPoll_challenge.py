# Election_Analysis
#file_variable = open(election_results, 'r')
import os
import csv  
print('current working directory' , os.getcwd())
file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join( "election_analysis.txt")
#defining empty variables
total_votes=0
candidate_unique = []
candidate_vote = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
county_unique = [] 
county_vote = {}

#open the election results and read the file
with open(file_to_load) as election_analysis:
    file_reader = csv.reader(election_analysis)
    #read the header row
    headers = next(file_reader)
    #print(headers)
    #loop each row in csv file
    for row in file_reader:
        #count total votes:
        total_votes +=1
       # Get county name for each vote
        county_name=row[1]
        #find the unique counties; if unique start counting from 0
        if county_name not in county_unique: 
            county_unique.append(county_name) 
            county_vote[county_name] = 0
        # Increment vote to that counties count.
        county_vote[county_name]  += 1 
        # Get candidate name for each vote
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_unique:
            # Add it to the list of candidates.
            candidate_unique.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_vote[candidate_name] = 0
        # Increment vote to that candidate's count.
        candidate_vote[candidate_name] += 1   
    #print(county_unique) 
    #print(county_vote)
    #print(candidate_vote)
    #find the county name with highest vote and the vote count
    max_value = [(value, key) for key, value in county_vote.items()]
    highest_county_vote=max(max_value)[1]
    print("The county with highest vote turnout is "+ highest_county_vote)
    
    #find the candidate name with highest vote and the vote count
    max_value2= [(value, key) for key, value in candidate_vote.items()]
    highest_candidate_vote=max(max_value2)[1]
    winner_vote=max(max_value2)[0]
    print("The Candidate with highest vote is "+ highest_candidate_vote)
    print("Winner vote is "+ str(winner_vote ))

with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for counties in county_vote:
        vote = county_vote[counties]
        county_results = (f"{counties}: {vote/total_votes*100:.1f}% ({vote:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        # Save the candidate results to our text file.
        txt_file.write(county_results) 
        
    election_results2 = (
        f"\n---------------------------\n"
        f"Largest County Turnout: {highest_county_vote}\n"
        f"---------------------------\n\n")
    print(election_results2, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results2)

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
        f"----------------------------")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)






#git status
#git add .
#git status
#git commit -m "adding the election audit code."
#git push



