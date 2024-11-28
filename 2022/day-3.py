# Part 1
def common(items: str) -> str:
    n = len(items) // 2
    c1 = items[:n]
    c2 = items[n:]

    for item in c1:
        if item in c2:
            return item

    raise ValueError


def value(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def badge(items1: str, items2: str, items3: str) -> str:
    for item in items1:
        if item in items2 and item in items3:
            return item

    raise ValueError


file = 'inputs/day-3.txt'

with open(file) as f:
    lines = f.readlines()

score = 0
for line in lines:
    item = common(line.split('\n')[0])
    score += value(item)

print(score)

# Part 2
score = 0
for i in range(0, len(lines), 3):
    items1 = lines[i].split('\n')[0]
    items2 = lines[i+1].split('\n')[0]
    items3 = lines[i+2].split('\n')[0]

    item = badge(items1, items2, items3)
    score += value(item)

print(score)
