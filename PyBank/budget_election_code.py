#Importing os and csv 
import os
import csv


# Creating the variables
t_month = 0
t_rev = 0
g_inc = 0
g_dec = 0
g_inc_date = ''
g_dec_date = ''


#Creating the file path
csvpath = os.path.join('/Users/scottcaruso/Resources/budget_data.csv')
data = []
#Open the csv file and set it to file
with open(csvpath, newline='') as file:
     csvreader =  csv.reader(file, delimiter=',')
#skipping the header row 
     next(csvreader)
#starting the for loop 
     for row in csvreader:
         
#Find the totl of Months
        t_month = t_month + 1 
#Find the total revenue
        t_rev = t_rev +int(row[1])
#Find Average Change

        ave_change = (t_rev/t_month)
#Find Greatest Increase in profits 
        if int(row[1]) >= g_inc:
              g_inc = int(row[1])
              g_inc_date = row[0]
#Find Greatest Decrease in Profits 
        if int(row[1]) <= g_dec:
              g_dec = int(row[1])
              g_dec_date = row[0]
        
        data.append(row)

differences = []
for i, row in enumerate(data):
#Find the totl of Months
     
     if i==0:
         continue
     j = i-1
     diff = int(row[1]) - int(data[j][1])
     
     differences.append(diff)
ave_change = (sum(differences)/len(differences))

       
######################################################
#Printing results 
print('Financial Analysis')
print('------------------------------------')
print('Total months: ' + str(t_month))
print(f'Total: ' + '$' + str(t_rev))
print('Average Change: ' + str(ave_change))
print('Greatest Increase in Profits: ' + g_inc_date + ' ' + '$' + str(g_inc))
print('Greatest Decrease in Profits: ' + g_dec_date + ' ' + '$' + str(g_dec))