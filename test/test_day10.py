from aoc.day10 import parse_input, part1, part2

TEST_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def test_part1():
    assert part1(parse_input(TEST_INPUT)) == 36


def test_part2():
    assert part2(parse_input(TEST_INPUT)) == 81
