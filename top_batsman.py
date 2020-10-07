import csv
import matplotlib.pyplot as plt


def solution_2():
    rcb = []
    with open('deliveries.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[2] == 'Royal Challengers Bangalore'):
                rcb.append(row)

    runs_map = {}
    for entry in rcb:
        if entry[6] not in runs_map:
            runs_map[entry[6]] = int(entry[15])
        else:
            runs_map[entry[6]] += int(entry[15])

    runs_map = sorted(runs_map.items(), key=lambda x: x[1], reverse=True)

    names = []
    runs = []
    for i, tup in enumerate(runs_map):
        names.append(tup[0])
        runs.append(tup[1])

    plt.figure(figsize=(15, 9), dpi=80)
    # Plotting runs for top 10 batsmen
    bars = plt.bar(names[:10], runs[:10])
    for height in bars:
        pos = height.get_height()
        plt.text(height.get_x() + 0.25, pos + 1, pos)
    plt.title("Top Batsmen from Royal Challengers Bangalore")
    plt.xlabel('Batsman', fontweight='bold')
    plt.ylabel('Runs', fontweight='bold')
    plt.xticks(rotation=90)
    plt.show()
