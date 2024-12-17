from aoc.day17 import parse_input, part1

TEST_INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def test_part1():
    assert part1(parse_input(TEST_INPUT)) == "4,6,3,5,6,3,5,2,1,0"
