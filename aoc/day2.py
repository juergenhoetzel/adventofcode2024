import sys
from pathlib import Path


def load_reports(report_path: Path) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in report_path.read_text().splitlines() if line]


def is_safe(levels: list[int]) -> bool:
    differences = [(j - i) for (i, j) in zip(levels, levels[1:])]
    return all([1 <= d <= 3 for d in differences]) or all([-3 <= d <= -1 for d in differences])


def unsafe_level_index(levels: list[int], min_level=1, max_level=3) -> int | None:
    for i in range(len(levels) - 1):
        if not min_level <= (levels[i + 1] - levels[i]) <= max_level:
            return i


def is_safe_dampened(levels: list[int]) -> bool:
    for ranges in [(1, 3), (-3, -1)]:
        i = unsafe_level_index(levels, *ranges)
        if i is None:
            return True
        elif unsafe_level_index(levels[:i] + levels[i + 1 :], *ranges) is None:
            return True
        elif unsafe_level_index(levels[: i + 1] + levels[i + 2 :], *ranges) is None:
            return True
    return False


def count_report_safe(report_path: Path, is_safe_fn=is_safe) -> int:
    reports = load_reports(report_path)
    return sum([is_safe_fn(levels) for levels in reports])


def main():
    print(count_report_safe(Path(sys.argv[1])))
    print(count_report_safe(Path(sys.argv[1]), is_safe_dampened))


if __name__ == "__main__":
    main()
