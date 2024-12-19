from aoc.day19 import parse_input, part1, part2

TEST_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"
"""


def test_part1():
    assert part1(*parse_input(TEST_INPUT)) == 6


def test_part2():
    assert part2(*parse_input(TEST_INPUT)) == 16
