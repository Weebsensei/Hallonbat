from itertools import combinations
import openpyxl
import pandas as pd
file = 'F1 Fantasy.xlsx'
data = pd.ExcelFile(file)
ps = openpyxl.load_workbook(file, data_only=True)
sheet = ps['Blad2']

# Python script to generate every possible Team for a F1 Fantasy League.
# Total number of possible combinations were over 20k (ish).

budget = 125
drivers = []

# Add all drivers with name, "value", and cost
# Name is name of driver. (duh)
# Value is "Killgissning" of potential championship points. (We love guesstimates)
# Cost is the cost of the driver. (duh)
for row in range(3, 23) :
    drivers.append({
        "d": sheet['G' + str(row)].value, 
        "v": sheet['H' + str(row)].value, 
        "c": sheet['K' + str(row)].value})

# List for all possible combinations 
valid_combinations = []
for r in range(1, len(drivers) + 1) :
    for combo in combinations(drivers, r):
        total_cost = sum(item["c"] for item in combo)
        # Check that combination is within budget
        if total_cost <= budget :
            total_value = sum(item["v"] for item in combo)
            # Filter out worst expected performers
            if total_value >= 450 : # (We love guesstimates)
                combo_names = frozenset(item["d"] for item in combo)
                valid_combinations.append((combo_names, total_value, total_cost))

# Sort after number of drivers in team (Useful later)
valid_combinations.sort(key=lambda x: -len(x[0]))

# Filter out subsets
filtered_combinations = []
for combo, value, cost in valid_combinations:
    # Check if team is a subset of previous team
    # This filters teams containing (A, B, C) if there is already a team containing (A, B, C, D)
    if not any(existing_combo.issuperset(combo) for existing_combo, _, _ in filtered_combinations):
        filtered_combinations.append((combo, value, cost))

# Sort filtered teams on potential "Value"
filtered_combinations.sort(key=lambda x: -x[1])

df = pd.DataFrame(filtered_combinations)
print(df)

# Print top 20 best expected teams. (We love guesstimates)
for i in range(0, 20) :
      print(filtered_combinations[i])

