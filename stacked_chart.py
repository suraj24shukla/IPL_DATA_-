import csv
import matplotlib.pyplot as plt


def solution_4():
    TEAM = {
        'Sunrisers Hyderabad': 0,
        'Royal Challengers Bangalore': 0,
        'Mumbai Indians': 0,
        'Rising Pune Supergiant': 0,
        'Gujarat Lions': 0,
        'Kolkata Knight Riders': 0,
        'Kings XI Punjab': 0,
        'Delhi Daredevils': 0,
        'Chennai Super Kings': 0,
        'Rajasthan Royals': 0,
        'Deccan Chargers': 0,
        'Kochi Tuskers Kerala': 0,
        'Pune Warriors': 0,
        'Rising Pune Supergiants': 0
        }

    with open('matches.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        seasons = {}
        flag = 0
        for row in csv_reader:
            if flag:
                if row[1] not in seasons:
                    seasons[row[1]] = TEAM.copy()
                    seasons[row[1]][row[4]] += 1
                    seasons[row[1]][row[5]] += 1
                else:
                    seasons[row[1]][row[4]] += 1
                    seasons[row[1]][row[5]] += 1
            flag = 1

    plt.subplots(figsize=(15, 9), dpi=80)
    width = 0.5
    lis2 = list(seasons.keys())

    botval = [0]*len(TEAM)
    for j in range(len(lis2)):
        yvals = [v for v in seasons[lis2[j]].values()]
        plt.bar(list(TEAM.keys()), yvals, width, bottom=botval, label=lis2[j])
        for i in range(len(yvals)):
            botval[i] += yvals[i]

    plt.legend()
    plt.xlabel('Teams', fontweight='bold')
    plt.ylabel('Matches', fontweight='bold')
    plt.title("Matches played by teams per season")
    plt.xticks(rotation=30)
    plt.show()
