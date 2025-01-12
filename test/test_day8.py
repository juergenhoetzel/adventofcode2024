from aoc.day8 import parse_input, part1, part2

TEST_INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".splitlines()


def test_part1():
    assert part1(parse_input(TEST_INPUT)) == 14


def test_part2():
    assert part2(parse_input(TEST_INPUT)) == 34
