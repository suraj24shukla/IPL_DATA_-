# IPL data visualization

## Instructions to run

- CD into project directory
```
cd dataproject-ipl-suraj_shukla
```
- Install requirements in python environment
```
pip install -r requirements.txt
```
- Run `ipl_analysis.py`
```
python ipl_analysis.py
```

## Dependencies
```
csv
matplotlib
```

## Files

### Main 
```
ipl_analysis.txt
```

### Data Sources
```
matches.csv
deliveries.csv
```

### Helpers
```
total_runs.py
top_batsman.py
umpire_analysis.py
stacked_chart.py
```

# Details

### total_runs.py
- Import and analyse `deliveries.csv`
- Plot Bar Chart for total runs scored by each team

### top_batsman.py
- Import and analyse `deliveries.csv`
- Plot Bar Chart for the runs scored by each Batsman of the team Royal Challengers Banglore

### umpire_analysis.py
- Import and analyse `matches.csv`
- Plot chart for the Country with the number of umpires from that country


### stacked_chart.py
- Import and analyse `matches.csv`
- Plot stacked bar charts for the matches played by each team, and the matches played in each season.
