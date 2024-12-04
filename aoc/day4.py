import sys
from pathlib import Path


def count_xmas(rows: list[str], y, x) -> int:
    count = 0
    for x_diff in [-1, 0, 1]:
        for y_diff in [-1, 0, 1] if x_diff else [-1, 1]:
            for i in range(0, 4):
                y2 = y + y_diff * i
                x2 = x + x_diff * i
                if y2 < 0 or y2 >= len(rows) or x2 < 0 or x2 >= len(rows[y]) or rows[y2][x2] != "XMAS"[i]:
                    break
            else:
                count += 1
    return count


def part2(rows: list[str]) -> int:
    def is_x_mas(y, x):
        return rows[y][x] + rows[y + 1][x + 1] + rows[y + 2][x + 2] in ("MAS", "SAM") and rows[y][x + 2] + rows[y + 1][
            x + 1
        ] + rows[y + 2][x] in ("MAS", "SAM")

    return sum((1 for y in range(len(rows) - 2) for x in range(len(rows[0]) - 2) if is_x_mas(y, x)))


def part1(rows: list[str]):
    return sum([count_xmas(rows, y, x) for y in range(len(rows)) for x in range(len(rows[0]))])


def main():
    rows = Path(sys.argv[1]).read_text().splitlines()
    print(f"Part 1: {part1(rows)}\nPart 2: {part2(rows)}")


if __name__ == "__main__":
    main()
