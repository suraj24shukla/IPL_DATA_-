import csv
import matplotlib.pyplot as plt


def solution_3():
    umpire_country = {'JD Cloete': 'South Africa', 'PR Reiffel': 'Australia',
                      'SJA Taufel': 'Australia', 'NJ Llong': 'England',
                      'RK Illingworth': 'England', 'GAV Baxter': 'New Zealand',
                      'BG Jerling': 'South Africa', 'BR Doctrove': 'Dominican',
                      'DJ Harper': 'American', 'M Erasmus': 'South Africa',
                      'RB Tiffin': 'Zimbabwe', 'CB Gaffaney': 'New Zealand',
                      'MR Benson': 'England', 'Aleem Dar': 'Pakistan',
                      'SD Fry': 'Australia', 'AL Hill': 'New Zealand',
                      'BF Bowden': 'New Zealand', 'Asad Rauf': 'Pakistan',
                      'TH Wijewardene': 'Sri Lanka',
                      'BNJ Oxenford': 'Australia',
                      'IL Howell': 'South Africa',
                      'RE Koertzen': 'South Africa'}
    ump_dict = {}
    with open('matches.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[15] not in ump_dict:
                ump_dict[row[15]] = 1
            else:
                ump_dict[row[15]] += 1
            if row[16] not in ump_dict:
                ump_dict[row[16]] = 1
            else:
                ump_dict[row[16]] += 1
            if row[17] not in ump_dict:
                ump_dict[row[17]] = 1
            else:
                ump_dict[row[17]] += 1

    del ump_dict['']
    del ump_dict['umpire1']
    del ump_dict['umpire2']
    del ump_dict['umpire3']

    ret = {}
    for umpire in ump_dict:
        if umpire in umpire_country:
            if umpire_country[umpire] not in ret:
                ret[umpire_country[umpire]] = 1
            else:
                ret[umpire_country[umpire]] += 1

    plt.figure(figsize=(15, 9), dpi=80)
    bars = plt.bar(list(ret.keys()), list(ret.values()))
    for height in bars:
        pos = height.get_height()
        plt.text(height.get_x() + 0.32, pos + 0.01, pos)
    plt.title("Count of Umpires from different countries")
    plt.xlabel('Country', fontweight='bold')
    plt.ylabel('Count', fontweight='bold')
    plt.xticks(rotation=90)
    plt.show()
