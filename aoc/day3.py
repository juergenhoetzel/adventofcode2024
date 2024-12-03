import re
import sys
from pathlib import Path

RE = re.compile(r"mul\((\d+),(\d+)\)")
RE_COND = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")


def part1(instruction_strs: list[str]) -> int:
    return sum(
        int(match.group(1)) * int(match.group(2))
        for instruction_str in instruction_strs
        for match in RE.finditer(instruction_str)
    )


def part2(instruction_strs: list[str]) -> int:
    enabled = True
    acc = 0
    for instruction_str in instruction_strs:
        for m in RE_COND.finditer(instruction_str):
            match m.group(1):
                case "do()":
                    enabled = True
                case "don't()":
                    enabled = False
                case _ if enabled:
                    acc += int(m.group(2)) * int(m.group(3))
    return acc


def main():
    part1_sum = part1(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 1: {part1_sum}")
    part2_sum = part2(Path(sys.argv[1]).read_text().splitlines())
    print(f"Part 2: {part2_sum}")


if __name__ == "__main__":
    main()
