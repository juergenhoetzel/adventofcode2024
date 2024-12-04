from aoc.day4 import part1, part2

ROWS = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip().splitlines()


def test_part1():
    assert part1(ROWS) == 18


def test_part2():
    assert part2(ROWS) == 9
