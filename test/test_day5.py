from aoc.day5 import part1, part2

TEST_ORDER = {
    47: {29, 13, 61, 53},
    97: {13, 61, 53, 75, 29, 47},
    75: {29, 13, 53, 61, 47},
    61: {29, 53, 13},
    29: {13},
    53: {13, 29},
}

TEST_INPUT = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]


def test_part1():
    assert part1(TEST_ORDER, TEST_INPUT) == 143


def test_part2():
    assert part2(TEST_ORDER, TEST_INPUT) == 123
