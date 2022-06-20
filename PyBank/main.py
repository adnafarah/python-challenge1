#import dependencies - os module and csv module
import os
import csv

#set path to csv file 
csvpath = (r'C:\Users\A454\Desktop\PYHWK\PyBank\Resources\budget_data.csv')

#create empty list for profit/loss changes that will be calculated later
changes_list = []

#open csvfile using context manager
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    #get header - put it in an empty list
    header = []
    #use next() function to skip the header in the analysis
    header = next(csvreader)
    print(header)

    #calculating changes in profit/loss

    
    #skip the first row, as no changes to be calculated at this point
    first_line = next(csvreader)
    
    #store previous change as a variable so we can subtract it to calculate changes
    prev = int(first_line[1])
    totalpl = int(first_line[1])

    #initialise the 'total months' variable
    total_months = 0

    #start a loop
    for line in csvreader:
        totalpl += int(line[1]) #calculating total profit/loss
        changes_list.append(int(line[1]) - prev) #building list that contains the changes in profit/loss over period
        prev = int(line[1]) #next iteration


#load csv again as csvreaders as we cant iterate over it again
        
with open(csvpath) as csvfile:
    csvreaders = csv.reader(csvfile, delimiter=',')

    #skip header row
    header = next(csvreaders)
    
    total_months = 0
    for line in csvreaders:
        total_months = total_months + 1

#Printing the analysis

print("Financial Analysis")

#print total months
print("Total Months: " + str(total_months))

#print net total profit/loss over entire period
print("Total: $" + str(totalpl)) 

#defining function to calculate average of values in the list passed through it 
def average(list):
    return sum(list) / len(list)

#calculate the average profit/loss change using the previously defined function
average_change = round(average(changes_list), 2)
print("Average Change: $" + str(average_change))

#the max value of the list will be the greatest increase - using round() function to round to 2 dec places
greatest_increase= round(max(changes_list), 2)
print("Greatest increase in Profits: $" + str(greatest_increase))

#the min value of the list will be the greatest decrease - using round() function to round to 2 dec places
greatest_decrease = round(min(changes_list), 2)
print("Greatest Decrease in Profits: $" + str(greatest_decrease))


#create a txt file named 'pybank.txt' to print results 
file = open(r'analysis\pybank.txt', 'w')

file.write('Financial Analysis\n')
file.write('Total Months: 86\n')
file.write('Total: $22564198\n')
file.write('Average Change: $-8311.11\n')
file.write('Greatest increase in Profits: $1862002\n')
file.write('Greatest Decrease in Profits: $-1825558\n')

file.close()
