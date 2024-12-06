import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PlayerMap:
    locations: set[tuple[int, int]]
    start_pos: tuple[int, int]
    n_rows: int
    n_cols: int

    def turn(self, player_dir):
        match player_dir:
            case (-1, 0):
                return (0, 1)
            case (0, 1):
                return (1, 0)
            case (1, 0):
                return (0, -1)
            case (0, -1):
                return (-1, 0)
        raise ValueError(f"Invalid direction: {player_dir}")

    def is_in_field(self, pos: tuple[int, int]) -> bool:
        y, x = pos
        return 0 <= y < self.n_rows and 0 <= x < self.n_cols

    def walk(self) -> set[tuple[tuple[int, int], tuple[int, int]]] | None:
        pos = self.start_pos
        direction = (-1, 0)
        visited = set()
        while True:
            visited.add((pos, direction))
            new_pos = pos[0] + direction[0], pos[1] + direction[1]
            if not self.is_in_field(new_pos):
                return visited
            if new_pos in self.locations:
                direction = self.turn(direction)
            else:
                pos = new_pos
                if (pos, direction) in visited:
                    return None


def parse_input(lines: list[str]):
    locations = set()
    start_pos = (0, 0)
    for j, line in enumerate(lines):
        for i, x in enumerate(line.strip()):
            if x == "#":
                locations.add((j, i))
            elif x == "^":
                start_pos = (j, i)

    return PlayerMap(locations, start_pos, len(lines), len(lines[0]))


def part1(player_map):
    pos_dirs = player_map.walk()
    return len({pos for pos, dir in pos_dirs})


def part2(player_map: PlayerMap):
    movements = player_map.walk()
    assert movements
    orig_locations = player_map.locations
    positions = set()
    for pos, _ in movements:
        player_map.locations = {pos, *orig_locations}
        if not player_map.walk():
            positions.add(pos)
    return len(positions)


def main():
    player_map = parse_input(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 1: {part1(player_map)}")
    print(f"Part 2: {part2(player_map)}")


if __name__ == "__main__":
    main()
