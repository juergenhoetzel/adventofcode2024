import sys
import re
from pathlib import Path


def parse_input(s: str) -> tuple[list[str], list[str]]:
    lines = s.splitlines()
    return [s.strip() for s in lines[0].split(",")], lines[2:]


def part1(patterns: list[str], designs: list[str]):
    r = re.compile(f'^({"|".join(patterns)})+$')
    return sum((1 for design in designs if r.match(design)))


def main():
    t, d = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(t,d)}")


if __name__ == "__main__":
    main()
