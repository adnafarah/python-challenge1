import os 
import csv



csvpath = (r'C:\Users\A454\Desktop\PYHWK\PyPoll\Resources\election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    header = []
    header = next(csvreader)

    
    ccs_count = 0
    dd_count = 0
    rad_count = 0
    total_votes = 0

    for i in csvreader:
        total_votes = total_votes + 1
        if i[2] == "Charles Casper Stockham":
            ccs_count += 1
        if i[2] == "Diana DeGette":
            dd_count = dd_count + 1
        if i[2] == "Raymon Anthony Doane":
            rad_count = rad_count + 1



#file.write(print("Election Results"))
print("Total Votes: " + str(total_votes))

#calculate percentages of votes for each candidate, rounded to 3 decimal places
ccs_percentage = round(((ccs_count / total_votes) * 100), 3)
dd_percentage = round((dd_count / total_votes) * 100,3)
rad_percentage = round((rad_count / total_votes) * 100,3)

#print results for each candidate
print("Charles Casper Stockham: " + str(ccs_percentage) + "%  (" + str(ccs_count) + ")")
print("Diana DeGette: " + str(dd_percentage) + "%  (" + str(dd_count) + ")")
print("Raymon Anthony Doane: " + str(rad_percentage) + "%  (" + str(rad_count) + ")")

#getting the winner



#create a dictionary with the candidates as the keys and their no of votes as the values
poll_dict = {"Charles Casper Stockham": ccs_count,
             "Diana DeGette": dd_count,
             "Raymon Anthony Doane": rad_count}

#get the winner by returning the key with the max value
winner = max(poll_dict, key=poll_dict.get)

print("Winner: " + winner)
#print(max(poll_list))


#write results to txt file named 'pypoll.txt'

file = open(r'analysis\pypoll.txt', 'w')

file.write('Total Votes: 369711\n')
file.write('Charles Casper Stockham: 23.049%  (85213)\n')
file.write('Diana DeGette: 73.812%  (272892)\n')
file.write('Raymon Anthony Doane: 3.139%  (11606)\n')
file.write('Winner: Diana DeGette\n')
    
file.close()
