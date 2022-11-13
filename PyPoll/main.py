# importing the dependencies
import csv
import os

# opening and reading the csv file
csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:
    file = csv.reader(csvfile, delimiter=",")
    next(file)
    t=0
    n=0
    votes={}  
    cnt=0

# iterating through the rows and finding the candidates and counting their votes
    for row in file:
        if row[0] != "":
            t+=1
        if row[2] not in votes.keys():
            votes[row[2]] = 1     
        else:
            votes[row[2]] += 1

# determinig the winner           
    winner = [(value, key) for key, value in votes.items()]
    
# showing the results
    print("Election Results")
    print("----------------")
    print(f"Total Votes : {t}")
    print("----------------")
    for key, value in votes.items():
        print(f"{key} : {value/t*100:.3f}% ({value})")
    print("----------------")
    print(f"winner : {max(winner)[1]}")
    print("----------------")

# creating a text file consisting the results
    with open('analysis/results.txt', 'w') as r:
        r.write(f"Election Results\n----------------\nTotal Votes : {t}\n----------------\n")
        for key, value in votes.items():
            r.write(f"{key} : {value/t*100:.3f}% ({value})\n")
        r.write(f"----------------\nwinner : {max(winner)[1]}\n----------------")