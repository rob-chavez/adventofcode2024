import numpy as np
FILENAME = "/Users/blackbox/Desktop/advent2"

def is_sorted(level):
    return np.array_equal(level, np.sort(level)) or np.array_equal(level, np.sort(level)[::-1])

def has_valid_gradient(level):
    diffs = np.abs(np.diff(level))
    return np.all((diffs >= 1) & (diffs <= 3))

def try_dampener(level):
    for i in range(len(level)):
        new_level = np.delete(level, i)
        if is_sorted(new_level) and has_valid_gradient(new_level):
            return True
    return False

def advent_day_2(file, dampener=False):
    count = 0
    for line in file:
        level = np.array(list(map(int, line.split())))
        if is_sorted(level) and has_valid_gradient(level):
            count += 1
        elif dampener and try_dampener(level):
            count += 1
    return count

with open(FILENAME) as f:
    result = advent_day_2(f, dampener=True)

print(result)
