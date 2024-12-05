import sys
from pathlib import Path


def is_valid_order(order_map, xs):
    seen = set()
    for x in xs:
        if order_map.get(x, set()) & seen:
            return False
        seen.add(x)
    return True


def part1(order_map, xs):
    return sum([input[len(input) // 2] for input in xs if is_valid_order(order_map, input)])


def parse_input(path: Path):
    order_map = dict()
    with path.open() as r:
        for line in r:
            if s := line.strip():
                xy = [int(m) for m in s.split("|")]
                order_map[xy[0]] = order_map.get(xy[0], set()) | {xy[1]}
            else:
                break
        return order_map, [[int(m) for m in line.strip().split(",")] for line in r]


def main():
    part1_count = part1(*parse_input(Path(sys.argv[1])))
    print(f"Part 1: {part1_count}\n")


if __name__ == "__main__":
    main()
