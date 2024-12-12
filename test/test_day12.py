from aoc.day12 import parse_garden

TEST_INPUT = """AAAA
BBCD
BBCC
EEEC
""".splitlines()

TEST_INPUT2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".splitlines()

TEST_INPUT3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".splitlines()


def test_part1():
    assert parse_garden(TEST_INPUT).total_price() == 140
    assert parse_garden(TEST_INPUT2).total_price() == 772
    assert parse_garden(TEST_INPUT3).total_price() == 1930


def test_part2():
    assert parse_garden(TEST_INPUT).total_price_sides() == 80
    assert parse_garden(TEST_INPUT3).total_price_sides() == 1206
