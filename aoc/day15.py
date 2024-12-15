import sys
from pathlib import Path

import numpy as np

MOVE_MAP = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def parse_input(s: str):
    i = s.index("\n\n")
    warehouse = [list(line) for line in s[:i].splitlines()]
    return np.array(warehouse), s[i:].strip()


def move(a: np.ndarray, d=(0, 1)):
    yd, xd = d
    robot_positions = np.where(a == "@")
    sy, sx = robot_positions[0][0], robot_positions[1][0]
    y, x = sy, sx
    while len(a) > y and len(a[y]) > x:
        x += xd
        y += yd
        if a[y][x] == "#":
            return False
        if a[y][x] == ".":
            while y != sy or x != sx:
                y2, x2 = y - yd, x - xd
                a[y][x] = a[y2][x2]
                y, x = y2, x2
            a[y][x] = "."
            return True


def score(a: np.ndarray):
    return sum([y * 100 + x for y in range(len(a)) for x in range(len(a[y])) if a[y][x] == "O"])


def part1(a, movements):
    for m in movements:
        if d := MOVE_MAP.get(m):  # ignore newlines
            move(a, d)
    return score(a)


def main():
    s = Path(sys.argv[1]).read_text()
    a, movements = parse_input(s)
    print(f"Part 1: {part1(a, movements)}")


if __name__ == "__main__":
    main()
