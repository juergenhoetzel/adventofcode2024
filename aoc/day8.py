import sys
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


@dataclass
class AntennaMap:
    rows: int
    cols: int
    positions: dict[str, set[tuple[int, int]]]


def parse_input(lines: list[str]) -> AntennaMap:
    positions = [(c, (y, x)) for y, line in enumerate(lines) for x, c in enumerate(line) if c != "."]
    antennamap = {}
    for c, pos in positions:
        antennamap[c] = antennamap.get(c, set()) | {pos}
    return AntennaMap(len(lines), len(lines[0]), antennamap)


def positions(am: AntennaMap, mul=1) -> set[tuple[int, int]]:
    anodes_pos = set()

    def is_in_field(pos):
        y, x = pos
        return 0 <= y < am.rows and 0 <= x < am.cols

    for _, positions in am.positions.items():
        for (y1, x1), (y2, x2) in combinations(positions, 2):
            anodes_pos |= {
                pos
                for pos in [(y1 + (y1 - y2) * mul, x1 + (x1 - x2) * mul), (y2 + (y2 - y1) * mul, x2 + (x2 - x1) * mul)]
                if is_in_field(pos)
            }
    return anodes_pos


def part1(am: AntennaMap) -> int:
    return len(positions(am))


def part2(am: AntennaMap) -> int:
    anodes = set()
    for i in range(1, max(am.cols, am.rows)):
        anodes |= positions(am, i)
    for v in am.positions.values():
        anodes |= v
    return len(anodes)


def main():
    lines = parse_input(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
