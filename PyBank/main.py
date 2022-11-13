# importing the dependencies
import csv
import os

# reading the csv file
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    file = csv.reader(csvfile, delimiter=",")
    next(file)
    t=0
    n=0
    date=[]
    profit = []
    change = []
    bestmonth = ""
    worstmonth = ""

# iterating through the rows and storing the data in a list
    for row in file:
        if row[0] != "":
            t+=1
            n+=int(row[1])
            profit.append(row[1])
            date.append(row[0])

# calculating the change
    for i in range(1, t):  
        chg = int(profit[i]) - int(profit[i-1])
        change.append(chg)
 
# finding the Greatest Increase and Decrease in profit/loss  
    maximum_change = int(change.index(max(change)))
 
    minimum_change = int(change.index(min(change)))

    for k in range (len(date)):
        if (k == maximum_change+1):
            bestmonth = date[k]
        elif (k == minimum_change+1):
            worstmonth = date[k]
            
# showing the results
print("Financial Analysis")
print("------------------")
print(f"Total Months : {t}")
print(f"Total : ${n}")
print(f"Average Change : ${sum(change)/len(change):.2f}")
print(f"Greatest Increase in Profits : {bestmonth} (${max(change)})")
print(f"Greatest Decrease in Profits : {worstmonth} (${min(change)})")

# creating a text file and storing the results in it
with open('analysis/results.txt', 'w') as r:
    r.write(f'Financial Analysis\n-------------------\nTotal Months : {t}\nTotal : ${n}\nAverage Change : ${sum(change)/len(change):.2f}\nGreatest Increase in Profits : {bestmonth} (${max(change)})\nGreatest Decrease in Profits : {worstmonth} (${min(change)})')
