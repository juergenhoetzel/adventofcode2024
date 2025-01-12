import sys
from pathlib import Path


def parse_input(lines: list[str]) -> set[tuple[int, int]]:
    xys = [[int(s) for s in line.split(",")] for line in lines]
    return {(xy[0], xy[1]) for xy in xys}


def shortest_path(corruptions: set[tuple[int, int]], x_size, y_size):
    distances = {(x, y): sys.maxsize for x in range(x_size) for y in range(y_size) if not (x, y) in corruptions}
    distances[(0, 0)] = 0
    predecessor = dict()
    while distances:
        (x, y) = min(distances.keys(), key=distances.get)
        ucost = distances.pop((x, y))
        for pos in [
            (x2, y2)
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if 0 <= (x2 := x + d[0]) < x_size and 0 <= (y2 := y + d[1]) < y_size and (x2, y2) not in corruptions
        ]:
            if (vcost := distances.get(pos)) and ucost + 1 < vcost:
                distances[pos] = ucost + 1
                predecessor[pos] = (x, y)
    return predecessor


def part1(a, x_size, y_size):
    predecessor = shortest_path(a, x_size, y_size)
    c = 0
    pos = (x_size - 1), (y_size - 1)
    while pos := predecessor.get(pos):
        c += 1
    return c


def part2(lines: list[str], x_size, y_size):
    good_pos = 0
    bad_pos = len(lines) - 1
    while bad_pos > good_pos + 1:
        middle = (bad_pos + good_pos) // 2
        if part1(parse_input(lines[:middle]), x_size, y_size):
            good_pos = middle
        else:
            bad_pos = middle

    return lines[good_pos]


def main():
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(f"Part 1: {part1(parse_input(lines[:1024]), 71, 71)}")
    print(f"Part 2: {part2(lines, 71, 71)}")


if __name__ == "__main__":
    main()
