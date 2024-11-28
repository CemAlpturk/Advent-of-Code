import numpy as np

# Read file
input_path = 'inputs/day-1.txt'
with open(input_path) as f:
    lines = f.readlines()

# Process input
calories = []
val = 0
for line in lines:
    if line == '\n':
        calories.append(val)
        val = 0
    else:
        val += int(line.split('\n')[0])

calories = np.array(calories)

# Sort
sorted = np.sort(calories)
top3 = np.sum(sorted[-3:])
print(f"Sum of top3 calories: {top3}")
