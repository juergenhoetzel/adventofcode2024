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


def shortest_path(m: Maze, limit=None) -> int | None:
    distances = {
        (y, x): 0 if (y, x) == m.start else sys.maxsize
        for y in range(m.size_y)
        for x in range(m.size_x)
        if is_free(y, x, m)
    }

    while distances:
        min_pos, ucost = min(distances.items(), key=itemgetter(1))
        del distances[min_pos]
        if limit and ucost > limit:
            return
        if min_pos == m.end:
            return ucost
        for pos in [(min_pos[0] + d[0], min_pos[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
            if (d := distances.get(pos)) and d > ucost + 1:
                distances[pos] = ucost + 1


def part1(orig_maze: Maze):
    non_cheat_score = shortest_path(orig_maze)
    assert non_cheat_score
    count = 0
    to_check = len(orig_maze.walls)
    c = 0
    for remove_pos in orig_maze.walls:
        walls = orig_maze.walls - {remove_pos}
        m = dataclasses.replace(orig_maze, walls=walls)
        if shortest_path(m, non_cheat_score - 100):
            count += 1
        c += 1
        print("Done:", 100 * c / to_check)
    return count


def main():
    m = parse_maze(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(m)}")


if __name__ == "__main__":
    main()
