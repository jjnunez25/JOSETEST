import os
import csv
from collections import Counter

path = os.path.join("election_data.csv")

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # lists to append
    voterid = []
    county = []
    candidates = []

    for dog in csvreader:
        voterid.append(dog[0])
        county.append(dog[1])
        candidates.append(dog[2])

    canset = set(candidates)
    totalvote = len(voterid)
    cnt = Counter(candidates)

    # create a list with the unique names
    can_names = []

    for row in canset:
        can_names.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"The total number of votes was {totalvote}")
    print("----------------------------------------")

    dictionarycan = {}
    can_count = 0
    for row in can_names:
        candidate_name = str(can_names[can_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / totalvote * 100, 2)
        dictionarycan.update({candidate_name: votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)")
        can_count = can_count + 1

    winner = max(dictionarycan, key=lambda key: dictionarycan[key])

    print("Winner: ", winner)