
from aoc.day9 import part1,parse_input
TEST_INPUT = "2333133121414131402"


def test_part1():
    blocks = parse_input(TEST_INPUT)
    assert part1(blocks) == 1928
