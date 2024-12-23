import sys
from itertools import combinations
from pathlib import Path


def neighbors(connections: list[tuple[str, str]]):
    d = {}
    for fst, snd in connections:
        d[fst] = d.get(fst, set()) | {snd}
        d[snd] = d.get(snd, set()) | {fst}
    return d


def parse_input(s: str):
    pairs = [tuple(xs[:2]) for line in s.splitlines() if len(xs := line.split("-")) == 2]
    return neighbors(pairs)


def interconnected(n: dict[str, set[str]]):
    return set(
        [tuple(sorted([k, fst, snd])) for k, st in n.items() for fst, snd in combinations(st, 2) if snd in n[fst]]
    )


def part1(n: dict[str, set[str]]):
    return len({t for t in interconnected(n) for s in t if s.startswith("t")})


def main():
    d = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(d)}")


if __name__ == "__main__":
    main()
