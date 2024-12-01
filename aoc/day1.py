import sys
from pathlib import Path

import numpy as np


def day1(locations_path: Path) -> int:
    locations = np.sort(np.genfromtxt(locations_path, dtype=int), axis=0)
    return sum([abs(row[0] - row[1]) for row in locations])


def day1_part2(locations_path: Path) -> int:
    locations = np.genfromtxt(locations_path, dtype=int)
    counts = dict(zip(*np.unique([i for i in locations.T[1]], return_counts=True)))
    return sum([i * counts.get(i, 0) for i in locations.T[0]])


def main():
    print(day1(Path(sys.argv[1])))
    print(day1_part2(Path(sys.argv[1])))


if __name__ == "__main__":
    main()
