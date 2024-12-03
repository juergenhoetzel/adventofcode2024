from aoc.day3 import part1, part2

TEST = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]


TEST2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


def test_day3_sum():
    assert part1(TEST) == 161


def test_day3_part2_sum():
    assert part2(TEST2) == 48
