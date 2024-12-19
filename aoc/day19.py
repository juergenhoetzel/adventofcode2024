import functools
import re
import sys
from pathlib import Path


def parse_input(s: str) -> tuple[list[str], list[str]]:
    lines = s.splitlines()
    return [s.strip() for s in lines[0].split(",")], lines[2:]


def part1(patterns: list[str], designs: list[str]):
    r = re.compile(f'^({"|".join(patterns)})+$')
    return sum((1 for design in designs if r.match(design)))


def combinations(patterns: list[str], design: str):
    @functools.cache
    def loop(s: str):
        match s:
            case "":
                return 1
            case _:
                return sum(loop(s.removeprefix(pattern)) for pattern in patterns if s.startswith(pattern))

    return loop(design)


def part2(patterns: list[str], designs: list[str]):
    return sum(combinations(patterns, design) for design in designs)


def main():
    t, d = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(t,d)}")
    print(f"Part2: {part2(t,d)}")


if __name__ == "__main__":
    main()
