import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Robot:
    x: int
    y: int
    xd: int
    yd: int


def parse_robots(s: str) -> list[Robot]:
    return [Robot(*[int(s) for s in m]) for m in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", s)]


def step(robots: list[Robot], size_x, size_y) -> list[Robot]:
    return [Robot((robot.x + robot.xd) % size_x, (robot.y + robot.yd) % size_y, robot.xd, robot.yd) for robot in robots]


def partition_robots(robots: list[Robot], size_x, size_y):
    mid_y = (size_y - 1) // 2
    mid_x = (size_x - 1) // 2
    groups: dict[tuple[bool, bool], set[Robot]] = dict()
    for robot in robots:
        if robot.x == mid_x or robot.y == mid_y:
            continue
        group = (robot.x < mid_x, robot.y < mid_y)
        groups[group] = groups.get(group, set()) | {robot}
    return groups


def part1(robots: list[Robot], size_x, size_y):
    for _ in range(100):
        robots = step(robots, size_x, size_y)
    part_dict = partition_robots(robots, size_x, size_y)
    prod = 1
    for p_robots in part_dict.values():
        prod *= len(p_robots)
    return prod


def has_christimas_tree(robots: list[Robot], size_x, size_y) -> bool:
    vert = {x: set() for x in range(size_x)}
    hori = {y: set() for y in range(size_y)}
    for robot in robots:
        vert[robot.x].add(robot.y)
        hori[robot.y].add(robot.x)

    return (
        len([c for c in vert.values() if len(c) > size_y // 4]) >= 2
        and len([c for c in hori.values() if len(c) > size_x // 4]) >= 2
    )


def part2(robots: list[Robot], size_x, size_y) -> int:
    i = 0
    while not has_christimas_tree(robots, size_x, size_y):
        robots = step(robots, size_x, size_y)
        i += 1
    return i


def main():
    robots = parse_robots(Path(sys.argv[1]).read_text())
    print(f"Part 1: {part1(robots, 101, 103)}")
    print(f"Part 2: {part2(robots, 101, 103)}")


if __name__ == "__main__":
    main()
