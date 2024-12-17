import sys
from dataclasses import dataclass
from enum import Enum
from operator import itemgetter
from pathlib import Path


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


@dataclass
class Maze:
    distance: dict[tuple[int, int], dict[Dir, int]]
    predecessor: dict[tuple[int, int], dict[Dir, tuple[int, int]]]
    # costs: dict[tuple[int, int], dict[Dir, int]]
    start_pos: tuple[int, int]
    end_pos: tuple[int, int]


def parse_input(s: str) -> Maze:
    distance = dict()
    predecessor = dict()
    a = [[c for c in line] for line in s.splitlines()]
    end_pos = None
    start_pos = None
    for y, row in enumerate(a):
        for x, c in enumerate(row):
            match c:
                case "#":
                    continue
                case "E":
                    end_pos = (y, x)
                case "S":
                    start_pos = (y, x)
            distance[(y, x)] = {d: sys.maxsize for d in Dir}
    assert start_pos and end_pos
    distance[start_pos][Dir.E] = 0
    return Maze(distance, predecessor, start_pos, end_pos)


def dijkstra(maze: Maze) -> int | None:
    while maze.distance:
        (ucost, y, x, d) = min(
            ((cost, y, x, d) for (y, x), ds in maze.distance.items() for d, cost in ds.items()), key=itemgetter(0)
        )
        if (y, x) == maze.end_pos:
            return ucost
        del maze.distance[(y, x)][d]
        turns = [Dir((d.value + x) % 4) for x in (1, -1)]
        match d:
            case Dir.N:
                move_pos = (y - 1, x)
            case Dir.S:
                move_pos = (y + 1, x)
            case Dir.W:
                move_pos = (y, x - 1)
            case Dir.E:
                move_pos = (y, x + 1)

        for pos, new_dir, cost in [(move_pos, d, 1)] + [((y, x), t, 1000) for t in turns]:
            if vcost := maze.distance.get(pos, dict()).get(new_dir):
                if (new_cost := ucost + cost) < vcost:
                    maze.distance[pos][new_dir] = new_cost
                    # maze.costs[pos][new_dir] = new_cost


def part1(m: Maze):
    return dijkstra(m)


def main():
    m = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(m)}")


if __name__ == "__main__":
    main()
