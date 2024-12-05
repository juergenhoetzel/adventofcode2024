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


def sort_updates(order_map, updates):
    result = []
    for x in updates:
        insert_positions = [result.index(y) for y in order_map.get(x, {}) if y in result]
        if insert_positions:
            result.insert(min(insert_positions), x)
        else:
            result.append(x)
    return result


def part2(order_map, xs):
    sorted_updates = [sort_updates(order_map, updates) for updates in xs if not is_valid_order(order_map, updates)]
    return sum((updates[len(updates) // 2] for updates in sorted_updates))


def main():
    order, updates = parse_input(Path(sys.argv[1]))
    print(f"Part 1: {part1(order, updates)}")
    print(f"Part 2: {part2(order, updates)}")


if __name__ == "__main__":
    main()
