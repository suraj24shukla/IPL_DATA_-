import csv
import matplotlib.pyplot as plt


def solution_1():
    total_runs = {}
    batsman = {}
    with open("deliveries.csv", 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["batting_team"] not in total_runs:
                total_runs[line["batting_team"]] = 0
            else:
                total_runs[line["batting_team"]] += int(line["total_runs"])
            if line["batting_team"] == "Royal Challengers Bangalore":
                if line["batsman"] not in batsman:
                    batsman[line["batsman"]] = 0
                else:
                    batsman[line["batsman"]] += int(line["batsman_runs"])

    li = sorted(total_runs.items())
    x, y = zip(*li)
    plt.figure(figsize=(15, 7))
    plt.barh(x, y, align='center')
    plt.title("Total runs scored by teams")
    plt.xlabel("Overall Runs", fontweight='bold')
    plt.ylabel("Teams", fontweight='bold')
    plt.show()
