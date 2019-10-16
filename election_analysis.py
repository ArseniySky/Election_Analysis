# Election_Analysis
#file_variable = open(election_results, 'r')
import os
import csv
print('current working directory' , os.getpwd())
file_to_load = os.path.join("analysis", "election_analysis.txt")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes=0
county_votes = {}

candidate_option = []
candidate_vote = {}

winning_candidate = ""
wining_count = 0
winning_percentage = 0


#open the election results and read the file
with open(file_to_load) as election_analysis
    file_reader = csv.reader(election_analysis)
    print('')
    #read the header row
    headers = (next(file-ready))
    #print each row in csv file
    for row in file_reader:
        print(type(row))
        

#write output
#election_results = open(file_to_load, 'r')
#election_results.close()
#print(dir(os)) 


