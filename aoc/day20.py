import dataclasses
import sys
from operator import itemgetter
from pathlib import Path

test_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


@dataclasses.dataclass
class Maze:
    size_y: int
    size_x: int
    start: tuple[int, int]
    end: tuple[int, int]
    walls: set[tuple[int, int]]


def parse_maze(s: str) -> Maze:
    lines = s.splitlines()
    size_y = len(lines)
    size_x = len(lines[0])
    start = None
    end = None
    walls = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case "#":
                    walls.add((y, x))
                case "S":
                    start = (y, x)
                case "E":
                    end = (y, x)
    assert start and end
    return Maze(size_y, size_x, start, end, walls)


def is_free(y, x, maze: Maze):
    return (y, x) not in maze.walls and y and x and y < maze.size_y and x < maze.size_x


def shortest_path(m: Maze, limit=None) -> tuple[int | None, list[tuple[int, int]]]:
    distances = {
        (y, x): 0 if (y, x) == m.start else sys.maxsize
        for y in range(m.size_y)
        for x in range(m.size_x)
        if is_free(y, x, m)
    }
    predecessor: dict[tuple[int, int], tuple[int, int]] = dict()
    while distances:
        min_pos, ucost = min(distances.items(), key=itemgetter(1))
        del distances[min_pos]
        if limit and ucost > limit:
            return None, []
        if min_pos == m.end:
            pos = min_pos
            route = [pos]
            while True:
                pos = predecessor[pos]
                route = [pos, *route]
                if pos == m.start:
                    return ucost, route

        for pos in [(min_pos[0] + d[0], min_pos[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
            if (d := distances.get(pos)) and d > ucost + 1:
                distances[pos] = ucost + 1
                predecessor[pos] = min_pos


def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def cheat_paths(path, max_cheat_points=2):
    for i in range(len(path)):
        for j in range(i, len(path)):
            if (d := manhattan_distance(path[i], path[j])) <= max_cheat_points:
                yield (i + len(path) - j + d - 1)


def part1(orig_maze: Maze):
    non_cheat_score, path = shortest_path(orig_maze)
    assert non_cheat_score
    return len([score for score in cheat_paths(path) if score <= non_cheat_score - 100])


def part2(orig_maze: Maze):
    non_cheat_score, path = shortest_path(orig_maze)
    assert non_cheat_score
    return len([score for score in cheat_paths(path, 20) if score <= non_cheat_score - 100])


def main():
    m = parse_maze(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(m)}")
    print(f"Part2: {part2(m)}")


if __name__ == "__main__":
    main()
