import sys
from dataclasses import dataclass
from operator import add, mul
from pathlib import Path


@dataclass
class Equation:
    expected: int
    xs: list[int]


def parse_input(lines):
    def parse_line(line):
        match line.split(": "):
            case [ss, xs]:
                return Equation(int(ss), [int(x) for x in xs.split()])
            case _:
                raise ValueError(f"Invalid input: {line}")

    return [parse_line(line) for line in lines]


def is_valid(equation, ops=[mul, add]):
    def loop(current, xs):
        if equation.expected < current:
            return False
        match xs:
            case []:
                return current == equation.expected
            case [x, *xs]:
                return any((loop(op(current, x), xs) for op in ops))

    return loop(equation.xs[0], equation.xs[1:])


def part1(equations):
    return sum([equation.expected for equation in equations if is_valid(equation)])


def part2(equations):
    def concat(x, y):
        return int(str(x) + str(y))

    return sum([equation.expected for equation in equations if is_valid(equation, ops=[mul, add, concat])])


def main():
    equations = parse_input(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 1: {part1(equations)}")
    print(f"Part 2: {part2(equations)}")


if __name__ == "__main__":
    main()
