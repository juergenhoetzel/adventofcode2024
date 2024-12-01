import sys
from pathlib import Path

import numpy as np


def day1(locations_path: Path) -> int:
    locations = np.sort(np.genfromtxt(locations_path, dtype=int), axis=0)
    return sum([abs(row[0] - row[1]) for row in locations])


def main():
    print(day1(Path(sys.argv[1])))


if __name__ == "__main__":
    main()
