import os
import csv
import statistics

path = ("budget_data.csv")

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    csvlist = list(csvreader)

    #list to append
    dates = []
    revenues = []

    # run for loop for every row
    for dog in csvlist:
        dates.append(dog[0])
        revenues.append(int(dog[1]))

    # create a list for revenue change
    revenuechange = []

    # run loop through revenues list to find the change revenues from month
    revchange = [revenues[i + 1] - revenues[i] for i in range(len(revenues) - 1)]

    # variables
    max_change = max(revchange)
    big_loss = min(revchange)
    avg_change = statistics.mean(revchange)
    total_month = len(dates)
    max_month = None
    loss_month = None

    # for loop to find corresponding date
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == big_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])

    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"The financial analysis occured over {total_month} months")
    print(f"The average revenue change was ${avg_change}")
    print(f"The maximum revenue gain was ${max_change} and occured on {max_month}")
    print(f"The biggest revenue loss was ${big_loss} and occured on {loss_month}")