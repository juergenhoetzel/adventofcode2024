import sys
from dataclasses import dataclass, field
from pathlib import Path


def perimeter_of_region(positions: set[tuple[int, int]]) -> int:
    return sum([4 - len(adjacent_positons(pos) & positions) for pos in positions])


def adjacent_positons(pos: tuple[int, int]) -> set[tuple[int, int]]:
    y, x = pos
    ret = {(y + yd, x + xd) for (yd, xd) in [(1, 0), (0, 1), (-1, 0), (0, -1)]}
    return ret


@dataclass
class Garden:
    regions: dict[str, list[set[tuple[int, int]]]] = field(default_factory=dict)

    def total_price(self):
        return sum(
            [perimeter_of_region(region) * len(region) for c, regions in self.regions.items() for region in regions]
        )


def parse_garden(lines: list[str]) -> Garden:
    garden = Garden()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if regions := garden.regions.get(c):
                if indexes := adjacent_regions((y, x), regions):
                    regions[indexes[0]].add((y, x))
                    if len(indexes) > 1:  # merge regions
                        merged = {pos for i in indexes for pos in regions[i]}
                        garden.regions[c] = [region for (i, region) in enumerate(regions) if i not in indexes]
                        garden.regions[c].append(merged)
                else:
                    regions.append({(y, x)})  # new region for this character
            else:
                garden.regions[c] = [{(y, x)}]  # first

    return garden


def adjacent_regions(pos: tuple[int, int], regions: list[set[tuple[int, int]]]) -> list[int]:
    return [i for i, region in enumerate(regions) if adjacent_positons(pos) & region]


def part1(garden: Garden):
    return garden.total_price()


def main():
    lines = parse_garden(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 1: {part1(lines)}")


if __name__ == "__main__":
    main()
