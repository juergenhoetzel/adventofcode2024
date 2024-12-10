import sys
from pathlib import Path

import numpy as np


def parse_input(s: str):
    return np.array([[int(s) for s in line] for line in s.splitlines()])


def get_trailheads(a: np.ndarray):
    return np.argwhere(a == 0)


def paths(a: np.ndarray, y: int, x: int):
    def in_field(y, x) -> bool:
        return 0 <= y < a.shape[0] and 0 <= x < a.shape[1]

    assert a[y][x] == 0
    queue = [[(y, x)]]
    valid_paths = []
    while queue:
        path = queue.pop()
        y, x = path[0]
        height = a[y][x]
        if height == 9:
            valid_paths.append(path)
        else:
            for y2, x2 in ((y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)):
                if in_field(y2, x2) and (a[y2][x2] == height + 1):
                    queue.append([(y2, x2), *path])
    return valid_paths


def part1(map: np.ndarray):
    return sum([len({path[0] for path in paths(map, *th)}) for th in get_trailheads(map)])


def part2(map: np.ndarray):
    return sum([len(paths(map, *th)) for th in get_trailheads(map)])


def main():
    m = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(m)}")
    print(f"Part2: {part2(m)}")


if __name__ == "__main__":
    main()
