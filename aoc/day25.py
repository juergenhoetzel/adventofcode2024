import sys
from pathlib import Path


def parse_input(s: str):
    lock_keys = s.split("\n\n")
    return [
        {(y, x) for y, line in enumerate(item.splitlines()) for x, c in enumerate(line) if c == "#"}
        for item in lock_keys
    ]


def part1(lock_keys: list[set[tuple[int, int]]]):
    return sum([0 if (key & lock) else 1 for key in lock_keys if (6, 0) in key for lock in lock_keys if (0, 0) in lock])


def main():
    lock_keys = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part 1: {part1(lock_keys)}")


if __name__ == "__main__":
    main()
