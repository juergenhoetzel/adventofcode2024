from aoc.day7 import Equation, part1, part2

test_input = [
    Equation(expected=190, xs=[10, 19]),
    Equation(expected=3267, xs=[81, 40, 27]),
    Equation(expected=83, xs=[17, 5]),
    Equation(expected=156, xs=[15, 6]),
    Equation(expected=7290, xs=[6, 8, 6, 15]),
    Equation(expected=161011, xs=[16, 10, 13]),
    Equation(expected=192, xs=[17, 8, 14]),
    Equation(expected=21037, xs=[9, 7, 18, 13]),
    Equation(expected=292, xs=[11, 6, 16, 20]),
]


def test_part1():
    assert part1(test_input) == 3749


def test_part2():
    assert part2(test_input) == 11387
