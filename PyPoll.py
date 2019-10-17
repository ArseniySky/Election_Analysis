# Election_Analysis
#file_variable = open(election_results, 'r')
import os
import csv  
print('current working directory' , os.getcwd())
file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes=0
county_votes = {}

candidate_option = []
candidate_vote = {}

winning_candidate = ""
wining_count = 0
winning_percentage = 0
unique_list = [] 

#open the election results and read the file
with open(file_to_load) as election_analysis:
    file_reader = csv.reader(election_analysis)
    print('')
    #read the header row
    headers = next(file_reader)
    print(headers)
    #print each row in csv file
    for row in file_reader:
       # print(row[1])
        if row[1] not in unique_list: 
            unique_list.append(row[1]) 
            #print (row[1]) 
    print(unique_list) 
    
    
         

#write output
#election_results = open(file_to_load, 'r')
#election_results.close()
#print(dir(os)) 


