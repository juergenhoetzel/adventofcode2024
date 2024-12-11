import sys
from pathlib import Path


def blink_sum(xs, n):
    work = dict()
    for x in xs:
        work[x] = work.get(x, 0) + 1
    for _ in range(n):
        new_work = dict()
        for x, c in work.items():
            if x == 0:
                new_work[1] = new_work.get(1, 0) + c
            elif x == 1:
                new_work[2024] = new_work.get(2024, 0) + c
            else:
                s = str(x)
                l = len(s)
                if (l % 2) == 0:
                    left = int(s[: l // 2])
                    right = int(s[l // 2 :])
                    new_work[left] = new_work.get(left, 0) + c
                    new_work[right] = new_work.get(right, 0) + c
                else:
                    y = x * 2024
                    new_work[y] = new_work.get(y, 0) + c
        work = new_work
    return sum(work.values())


def part1(xs):
    return blink_sum(xs, 25)


def part2(xs):
    return blink_sum(xs, 75)


def main():
    xs = [int(x) for x in Path(sys.argv[1]).read_text().strip().split()]
    # xs = [int(x) for x in "125 17".split()]
    print(f"Part 1: {part1(xs)}")
    print(f"Part 2: {part2(xs)}")


if __name__ == "__main__":
    main()
