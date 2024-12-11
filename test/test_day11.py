from aoc.day11 import part1

TEST_INPUT = [int(s) for s in "125 17".split()]


def test_part1():
    assert part1(TEST_INPUT) == 55312
